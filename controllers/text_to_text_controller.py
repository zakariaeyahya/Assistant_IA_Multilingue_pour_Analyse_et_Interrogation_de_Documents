# File: controllers/text_to_text_controller.py

from services.services_seamless.seamless_translator import SeamlessTranslator
from services.services_function.pdf_extraction import extract_text_from_pdf
from services.services_function.language_mapping import get_language_code

class TextToTextController:
    def __init__(self, groq_api_key):
        self.translator = SeamlessTranslator()
        self.groq_api_key = groq_api_key

    def process(self, question, src_lang, pdf_lang, target_lang, pdf_path):
        pdf_content = extract_text_from_pdf(pdf_path)
        
        # Convert language names to codes
        src_lang_code = get_language_code(src_lang)
        pdf_lang_code = get_language_code(pdf_lang)
        target_lang_code = get_language_code(target_lang)
        
        # Translate question if needed
        if src_lang_code != pdf_lang_code:
            translated_question = self.translator.translate_text(question, src_lang_code, pdf_lang_code)
        else:
            translated_question = question
        
        # Use Groq for answering (placeholder - implement actual Groq interaction)
        response_pdf_lang = self._get_groq_response(translated_question, pdf_content, pdf_lang)
        
        # Translate response if needed
        if pdf_lang_code != target_lang_code:
            translated_response = self.translator.translate_text(response_pdf_lang, pdf_lang_code, target_lang_code)
        else:
            translated_response = response_pdf_lang
        
        return translated_question, translated_response

    def _get_groq_response(self, question, context, lang):
        # Placeholder for Groq API interaction
        # Implement the actual Groq API call here
        return f"This is a placeholder response in {lang} to the question: {question}"