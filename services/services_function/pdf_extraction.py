# File: services/services_function/pdf_extraction.py

from PyPDF2 import PdfReader
import logging
import os

logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path):
    if not os.path.isfile(pdf_path):
        logger.error(f"File not found: {pdf_path}")
        return ""
    
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            return "\n".join(page.extract_text() for page in reader.pages)
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")
        return ""