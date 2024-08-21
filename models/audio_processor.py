# File: models/audio_processor.py

import logging
from models.model_singleton import ModelSingleton
from services.services_function.pdf_extraction import extract_text_from_pdf
from services.services_function.language_mapping import get_language_code, get_language_name
from langchain_groq import ChatGroq
import numpy as np

logger = logging.getLogger(__name__)

class AudioProcessor:
    def __init__(self, groq_api_key):
        self.model_singleton = ModelSingleton()
        self.groq_api_key = groq_api_key
        self.llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0, groq_api_key=groq_api_key)
        logger.info("AudioProcessor initialized. Models loaded.")
        
        # Vérification de l'initialisation
        if hasattr(self.model_singleton, 'translator') and hasattr(self.model_singleton, 'speech_to_text') and hasattr(self.model_singleton, 'text_to_speech'):
            logger.info("All components (translator, speech_to_text, text_to_speech) successfully initialized in AudioProcessor")
        else:
            logger.error("One or more components not found in ModelSingleton")

    def process_text_to_audio(self, question, src_lang, pdf_lang, target_lang, pdf_path):
        try:
            pdf_content = extract_text_from_pdf(pdf_path)
            logger.info(f"PDF content extracted: {pdf_content[:100]}...")  # Log first 100 chars
            
            src_lang_code = get_language_code(src_lang)
            pdf_lang_code = get_language_code(pdf_lang)
            target_lang_code = get_language_code(target_lang)
            
            translated_question = self.model_singleton.translator.translate_text(question, src_lang_code, pdf_lang_code) if src_lang_code != pdf_lang_code else question
            logger.info(f"Translated question: {translated_question[:100]}...")
            
            response_pdf_lang = self._get_groq_response(translated_question, pdf_content, pdf_lang)
            logger.info(f"Groq response: {response_pdf_lang[:100]}...")
            
            translated_response = self.model_singleton.translator.translate_text(response_pdf_lang, pdf_lang_code, target_lang_code) if pdf_lang_code != target_lang_code else response_pdf_lang
            logger.info(f"Translated response: {translated_response[:100]}...")
            
            audio_array = self.model_singleton.text_to_speech.text_to_speech(translated_response, target_lang_code)
            logger.info(f"Audio generated: shape={audio_array.shape}, dtype={audio_array.dtype}")
            
            return translated_question, translated_response, audio_array
        except Exception as e:
            logger.error(f"Error in process_text_to_audio: {str(e)}", exc_info=True)
            return str(e), str(e), np.array([])

    def process_audio_to_text(self, audio_array, audio_lang, pdf_lang, target_lang, pdf_path):
        try:
            pdf_content = extract_text_from_pdf(pdf_path)
            logger.info(f"PDF content extracted: {pdf_content[:100]}...")  # Log first 100 chars
            
            audio_lang_code = get_language_code(audio_lang)
            pdf_lang_code = get_language_code(pdf_lang)
            target_lang_code = get_language_code(target_lang)
            
            logger.info(f"Processing audio: shape={audio_array.shape}, dtype={audio_array.dtype}")
            transcription = self.model_singleton.speech_to_text.speech_to_text(audio_array, audio_lang_code)
            logger.info(f"Transcription: {transcription[:100]}...")  # Log first 100 chars
            
            translated_transcription = self.model_singleton.translator.translate_text(transcription, audio_lang_code, pdf_lang_code) if audio_lang_code != pdf_lang_code else transcription
            logger.info(f"Translated transcription: {translated_transcription[:100]}...")
            
            response_pdf_lang = self._get_groq_response(translated_transcription, pdf_content, pdf_lang)
            logger.info(f"Groq response: {response_pdf_lang[:100]}...")
            
            translated_response = self.model_singleton.translator.translate_text(response_pdf_lang, pdf_lang_code, target_lang_code) if pdf_lang_code != target_lang_code else response_pdf_lang
            logger.info(f"Translated response: {translated_response[:100]}...")
            
            return transcription, translated_transcription, response_pdf_lang, translated_response
        except Exception as e:
            logger.error(f"Error in process_audio_to_text: {str(e)}", exc_info=True)
            return str(e), str(e), str(e), str(e)

    def process_audio_to_audio(self, audio_array, audio_lang, pdf_lang, target_lang, pdf_path):
        try:
            transcription, translated_transcription, response_pdf_lang, translated_response = self.process_audio_to_text(
                audio_array, audio_lang, pdf_lang, target_lang, pdf_path
            )
            
            target_lang_code = get_language_code(target_lang)
            response_audio = self.model_singleton.text_to_speech.text_to_speech(translated_response, target_lang_code)
            logger.info(f"Response audio generated: shape={response_audio.shape}, dtype={response_audio.dtype}")
            
            return transcription, translated_transcription, response_pdf_lang, translated_response, response_audio
        except Exception as e:
            logger.error(f"Error in process_audio_to_audio: {str(e)}", exc_info=True)
            return str(e), str(e), str(e), str(e), np.array([])

    def process_text_to_text(self, question, src_lang, pdf_lang, target_lang, pdf_path):
        try:
            pdf_content = extract_text_from_pdf(pdf_path)
            logger.info(f"PDF content extracted: {pdf_content[:100]}...")  # Log first 100 chars
            
            src_lang_code = get_language_code(src_lang)
            pdf_lang_code = get_language_code(pdf_lang)
            target_lang_code = get_language_code(target_lang)
            
            translated_question = self.model_singleton.translator.translate_text(question, src_lang_code, pdf_lang_code) if src_lang_code != pdf_lang_code else question
            logger.info(f"Translated question: {translated_question[:100]}...")
            
            response_pdf_lang = self._get_groq_response(translated_question, pdf_content, pdf_lang)
            logger.info(f"Groq response: {response_pdf_lang[:100]}...")
            
            translated_response = self.model_singleton.translator.translate_text(response_pdf_lang, pdf_lang_code, target_lang_code) if pdf_lang_code != target_lang_code else response_pdf_lang
            logger.info(f"Translated response: {translated_response[:100]}...")
            
            return translated_question, translated_response
        except Exception as e:
            logger.error(f"Error in process_text_to_text: {str(e)}", exc_info=True)
            return str(e), str(e)

    def _get_groq_response(self, question, context, lang):
        prompt = f"""
        Question traduite : {question}
        Contexte : {context}

        Vous êtes un assistant virtuel spécialisé dans la fourniture d'informations sur le projet décrit dans le contexte donné.
        Votre rôle est de fournir des informations précises et pertinentes basées uniquement sur le contenu du PDF.
        Veuillez répondre à la requête de l'utilisateur en {lang} en utilisant uniquement les informations disponibles dans le contexte.
        Si l'information pour répondre à la question n'est pas présente dans le contexte, veuillez l'indiquer clairement.
        """
        
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            logger.error(f"Error in _get_groq_response: {str(e)}", exc_info=True)
            return f"Groq response error: {str(e)}"