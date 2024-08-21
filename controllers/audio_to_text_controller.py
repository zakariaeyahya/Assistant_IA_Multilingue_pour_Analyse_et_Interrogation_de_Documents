# File: controllers/audio_to_text_controller.py

from services.services_seamless.seamless_speech_to_text import SeamlessSpeechToText
from services.services_seamless.seamless_translator import SeamlessTranslator
from services.services_function.pdf_extraction import extract_text_from_pdf
from services.services_function.language_mapping import get_language_code
from services.services_function.audio_conversion import convert_opus_to_wav
import numpy as np
import soundfile as sf

class AudioToTextController:
    def __init__(self, groq_api_key, ffmpeg_path):
        self.speech_to_text = SeamlessSpeechToText()
        self.translator = SeamlessTranslator()
        self.groq_api_key = groq_api_key
        self.ffmpeg_path = ffmpeg_path

    def process(self, audio_path, audio_lang, pdf_lang, target_lang, pdf_path):
        # Convert opus to wav if necessary
        if audio_path.lower().endswith('.opus'):
            audio_path = convert_opus_to_wav(audio_path, self.ffmpeg_path)
        
        # Read audio file
        audio_array, sample_rate = sf.read(audio_path)
        if len(audio_array.shape) > 1:
            audio_array = np.mean(audio_array, axis=1)
        
        pdf_content = extract_text_from_pdf(pdf_path)
        
        # Convert language names to codes
        audio_lang_code = get_language_code(audio_lang)
        pdf_lang_code = get_language_code(pdf_lang)
        target_lang_code = get_language_code(target_lang)
        
        # Transcribe audio
        transcription = self.speech_to_text.speech_to_text(audio_array, audio_lang_code)
        
        # Translate transcription if needed
        if audio_lang_code != pdf_lang_code:
            translated_transcription = self.translator.translate_text(transcription, audio_lang_code, pdf_lang_code)
        else:
            translated_transcription = transcription
        
        # Use Groq for answering (placeholder - implement actual Groq interaction)
        response_pdf_lang = self._get_groq_response(translated_transcription, pdf_content, pdf_lang)
        
        # Translate response if needed
        if pdf_lang_code != target_lang_code:
            translated_response = self.translator.translate_text(response_pdf_lang, pdf_lang_code, target_lang_code)
        else:
            translated_response = response_pdf_lang
        
        return transcription, translated_transcription, response_pdf_lang, translated_response

    def _get_groq_response(self, question, context, lang):
        # Placeholder for Groq API interaction
        # Implement the actual Groq API call here
        return f"This is a placeholder response in {lang} to the transcription: {question}"