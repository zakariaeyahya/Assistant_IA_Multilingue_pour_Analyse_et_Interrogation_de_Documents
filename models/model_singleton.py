# File: models/model_singleton.py

import logging
from services.services_seamless.seamless_translator import SeamlessTranslator
from services.services_seamless.seamless_speech_to_text import SeamlessSpeechToText
from services.services_seamless.seamless_text_to_speech import SeamlessTextToSpeech

logger = logging.getLogger(__name__)

class ModelSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logger.info("Initializing ModelSingleton")
            cls._instance = super(ModelSingleton, cls).__new__(cls)
            cls._instance.translator = SeamlessTranslator()
            cls._instance.speech_to_text = SeamlessSpeechToText()
            cls._instance.text_to_speech = SeamlessTextToSpeech()
        return cls._instance