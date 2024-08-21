from transformers import AutoProcessor, SeamlessM4Tv2Model
import torch
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SeamlessSpeechToText:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Using device: {self.device}")
        self.processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
        self.model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large").to(self.device)
        logger.info("SeamlessSpeechToText initialized")

    def speech_to_text(self, audio_array, src_lang):
        logger.info(f"Processing audio of shape {audio_array.shape} for language {src_lang}")
        try:
            # Ensure audio is in the correct format (16kHz, float32)
            if audio_array.dtype != np.float32:
                audio_array = audio_array.astype(np.float32)
            
            if len(audio_array.shape) > 1:
                audio_array = np.mean(audio_array, axis=1)
            
            # Normalize audio
            audio_array = audio_array / np.max(np.abs(audio_array))

            # Prepare inputs
            inputs = self.processor(audios=audio_array, sampling_rate=16000, return_tensors="pt").to(self.device)
            logger.debug(f"Input shape: {inputs['input_features'].shape}")

            # Generate transcription
            with torch.no_grad():
                outputs = self.model.generate(**inputs, tgt_lang=src_lang, generate_speech=False)
            
            logger.debug(f"Output type: {type(outputs)}")
            logger.debug(f"Output attributes: {dir(outputs)}")

            # Check if the output has a 'sequences' attribute
            if hasattr(outputs, 'sequences'):
                # Decode the output sequences
                transcription = self.processor.batch_decode(outputs.sequences, skip_special_tokens=True)[0]
            else:
                # If 'sequences' is not available, try to decode the entire output
                transcription = self.processor.batch_decode(outputs, skip_special_tokens=True)[0]

            logger.info(f"Transcription: '{transcription[:100]}...'")  # Log first 100 chars

            return transcription

        except Exception as e:
            logger.error(f"Error in speech_to_text: {str(e)}", exc_info=True)
            return f"Transcription error: {str(e)}"