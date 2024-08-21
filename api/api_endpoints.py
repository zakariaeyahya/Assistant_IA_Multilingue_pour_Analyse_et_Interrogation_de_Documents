# File: api/api_endpoints.py

from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from models.audio_processor import AudioProcessor
from services.services_function.audio_conversion import convert_opus_to_wav
import os
import tempfile
import soundfile as sf
import numpy as np
import librosa
import logging
import base64
import io
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Utilisez des raw strings pour les chemins Windows
FFMPEG_PATH = r"FFMPEG_PATH"

# Initialisation d'AudioProcessor avec vérification
try:
    audio_processor = AudioProcessor("GROQ_API")
    logger.info("AudioProcessor successfully initialized in api_endpoints")
except Exception as e:
    logger.error(f"Failed to initialize AudioProcessor: {str(e)}")
    raise

@app.post("/process-text-to-audio/")
async def process_text_to_audio(
    question: str = Form(...),
    src_lang: str = Form(...),
    pdf_lang: str = Form(...),
    target_lang: str = Form(...),
    pdf_files: List[UploadFile] = File(...)
):
    pdf_paths = []
    try:
        for pdf_file in pdf_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(await pdf_file.read())
                pdf_paths.append(temp_pdf.name)

        translated_question, translated_response, audio_array = audio_processor.process_text_to_audio(
            question, src_lang, pdf_lang, target_lang, pdf_paths
        )
        
        # Convert audio_array to WAV format
        buffer = io.BytesIO()
        sf.write(buffer, audio_array, 16000, format='WAV')
        buffer.seek(0)
        audio_bytes = buffer.getvalue()
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')

        return JSONResponse({
            "translated_question": translated_question,
            "translated_response": translated_response,
            "audio": audio_base64
        })
    except Exception as e:
        logger.error(f"Error in process_text_to_audio endpoint: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        for path in pdf_paths:
            os.unlink(path)

@app.post("/process-audio-to-text/")
async def process_audio_to_text(
    audio_lang: str = Form(...),
    pdf_lang: str = Form(...),
    target_lang: str = Form(...),
    audio_file: UploadFile = File(...),
    pdf_files: List[UploadFile] = File(...)
):
    audio_path = ""
    pdf_paths = []
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.filename)[1]) as temp_audio:
            temp_audio.write(await audio_file.read())
            audio_path = temp_audio.name

        for pdf_file in pdf_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(await pdf_file.read())
                pdf_paths.append(temp_pdf.name)

        if audio_path.lower().endswith('.opus'):
            audio_path = convert_opus_to_wav(audio_path, FFMPEG_PATH)

        audio_array, sample_rate = sf.read(audio_path)
        logger.info(f"Audio loaded: shape={audio_array.shape}, dtype={audio_array.dtype}, sample_rate={sample_rate}")

        if sample_rate != 16000:
            audio_array = librosa.resample(y=audio_array, orig_sr=sample_rate, target_sr=16000)
            logger.info(f"Audio resampled to 16kHz: shape={audio_array.shape}")

        audio_array = audio_array.astype(np.float32)

        transcription, translated_transcription, response_pdf_lang, translated_response = audio_processor.process_audio_to_text(
            audio_array, audio_lang, pdf_lang, target_lang, pdf_paths
        )

        return JSONResponse({
            "transcription": transcription,
            "translated_transcription": translated_transcription,
            "response_pdf_lang": response_pdf_lang,
            "translated_response": translated_response
        })
    except Exception as e:
        logger.error(f"Error in process_audio_to_text endpoint: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if audio_path:
            os.unlink(audio_path)
        for path in pdf_paths:
            os.unlink(path)

@app.post("/process-audio-to-audio/")
async def process_audio_to_audio(
    audio_lang: str = Form(...),
    pdf_lang: str = Form(...),
    target_lang: str = Form(...),
    audio_file: UploadFile = File(...),
    pdf_files: List[UploadFile] = File(...)
):
    audio_path = ""
    pdf_paths = []
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.filename)[1]) as temp_audio:
            temp_audio.write(await audio_file.read())
            audio_path = temp_audio.name

        for pdf_file in pdf_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(await pdf_file.read())
                pdf_paths.append(temp_pdf.name)

        if audio_path.lower().endswith('.opus'):
            audio_path = convert_opus_to_wav(audio_path, FFMPEG_PATH)

        audio_array, sample_rate = sf.read(audio_path)
        logger.info(f"Audio loaded: shape={audio_array.shape}, dtype={audio_array.dtype}, sample_rate={sample_rate}")

        if sample_rate != 16000:
            audio_array = librosa.resample(y=audio_array, orig_sr=sample_rate, target_sr=16000)
            logger.info(f"Audio resampled to 16kHz: shape={audio_array.shape}")

        audio_array = audio_array.astype(np.float32)

        transcription, translated_transcription, response_pdf_lang, translated_response, response_audio = audio_processor.process_audio_to_audio(
            audio_array, audio_lang, pdf_lang, target_lang, pdf_paths
        )

        if response_audio is not None and isinstance(response_audio, np.ndarray):
            # Convert numpy array to WAV format
            buffer = io.BytesIO()
            sf.write(buffer, response_audio, 16000, format='WAV')
            buffer.seek(0)
            response_audio_bytes = buffer.getvalue()
            response_audio_base64 = base64.b64encode(response_audio_bytes).decode('utf-8')
        else:
            logger.warning("Response audio is None or not a numpy array")
            response_audio_base64 = None

        return JSONResponse({
            "transcription": transcription,
            "translated_transcription": translated_transcription,
            "response_pdf_lang": response_pdf_lang,
            "translated_response": translated_response,
            "response_audio": response_audio_base64
        })
    except Exception as e:
        logger.error(f"Error in process_audio_to_audio endpoint: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if audio_path:
            os.unlink(audio_path)
        for path in pdf_paths:
            os.unlink(path)

@app.post("/process-text-to-text/")
async def process_text_to_text(
    question: str = Form(...),
    src_lang: str = Form(...),
    pdf_lang: str = Form(...),
    target_lang: str = Form(...),
    pdf_files: List[UploadFile] = File(...)
):
    pdf_paths = []
    try:
        for pdf_file in pdf_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(await pdf_file.read())
                pdf_paths.append(temp_pdf.name)

        translated_question, translated_response = audio_processor.process_text_to_text(
            question, src_lang, pdf_lang, target_lang, pdf_paths
        )

        return JSONResponse({
            "translated_question": translated_question,
            "translated_response": translated_response
        })
    except Exception as e:
        logger.error(f"Error in process_text_to_text endpoint: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        for path in pdf_paths:
            os.unlink(path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
