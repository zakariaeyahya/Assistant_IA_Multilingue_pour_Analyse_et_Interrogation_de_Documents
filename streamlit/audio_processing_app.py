# File: streamlit/audio_processing_app.py

import streamlit as st
import os
import sys
import tempfile
from streamlit_option_menu import option_menu
import soundfile as sf
import numpy as np
from scipy.io import wavfile
import io
import requests

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
import streamlit as st
import requests
import base64
import io
# Import necessary modules
from controllers.text_to_audio_controller import TextToAudioController
from controllers.audio_to_text_controller import AudioToTextController
from controllers.audio_to_audio_controller import AudioToAudioController
from controllers.text_to_text_controller import TextToTextController

# Define the Groq API key and FFmpeg path
GROQ_API_KEY = "GROQ_API"
FFMPEG_PATH = "FFMPEG_PATH"
API_BASE_URL = "http://localhost:8000"  # Adjust this to your API's address
def normalize_audio(audio_array):
    if audio_array.size == 0:
        st.warning("Le tableau audio est vide.")
        return np.array([], dtype=np.int16)

    # Ensure audio is mono
    if len(audio_array.shape) > 1 and audio_array.shape[0] > 1:
        audio_array = np.mean(audio_array, axis=0)
    
    # Avoid division by zero
    max_abs_val = np.max(np.abs(audio_array))
    if max_abs_val == 0:
        st.warning("Le tableau audio ne contient que des zéros.")
        return np.zeros(audio_array.shape, dtype=np.int16)

    # Normalize to [-1, 1] range
    audio_array = audio_array / max_abs_val
    
    # Convert to int16 range
    audio_array_int16 = (audio_array * 32767).astype(np.int16)
    
    return audio_array_int16
def process_text_to_audio(question, src_lang, pdf_lang, target_lang, pdf_files):
    url = "http://localhost:8000/process-text-to-audio/"
    files = [('pdf_files', (file.name, file.getvalue(), 'application/pdf')) for file in pdf_files]
    data = {
        'question': question,
        'src_lang': src_lang,
        'pdf_lang': pdf_lang,
        'target_lang': target_lang
    }
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        result = response.json()
        st.success("✅ Texte converti en audio avec succès !")
        
        if src_lang != pdf_lang:
            st.markdown(f"### 🔄 Question traduite en {pdf_lang} :")
            st.markdown(f'<div class="output-box">{result["translated_question"]}</div>', unsafe_allow_html=True)
        
        st.markdown(f"### 💬 Réponse en {target_lang} :")
        st.markdown(f'<div class="output-box">{result["translated_response"]}</div>', unsafe_allow_html=True)
        
        # Decode base64 audio and play
        audio_bytes = base64.b64decode(result["audio"])
        st.audio(audio_bytes, format="audio/wav")
    else:
        st.error(f"❌ Une erreur est survenue lors de la conversion : {response.text}")

def process_audio_to_text(audio_file, audio_lang, pdf_lang, target_lang, pdf_files):
    url = "http://localhost:8000/process-audio-to-text/"
    files = [('pdf_files', (file.name, file.getvalue(), 'application/pdf')) for file in pdf_files]
    files.append(('audio_file', ('audio_file.wav', audio_file.read(), 'audio/wav')))
    data = {
        'audio_lang': audio_lang,
        'pdf_lang': pdf_lang,
        'target_lang': target_lang
    }
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        result = response.json()
        st.success("✅ Audio traité avec succès !")
        
        st.markdown("### 📝 Transcription originale :")
        st.markdown(f'<div class="output-box">{result["transcription"]}</div>', unsafe_allow_html=True)
        
        if audio_lang != pdf_lang:
            st.markdown(f"### 🔄 Transcription traduite en {pdf_lang} :")
            st.markdown(f'<div class="output-box">{result["translated_transcription"]}</div>', unsafe_allow_html=True)
        
        st.markdown(f"### 💬 Réponse en {pdf_lang} :")
        st.markdown(f'<div class="output-box">{result["response_pdf_lang"]}</div>', unsafe_allow_html=True)
        
        if pdf_lang != target_lang:
            st.markdown(f"### 🔄 Réponse traduite en {target_lang} :")
            st.markdown(f'<div class="output-box">{result["translated_response"]}</div>', unsafe_allow_html=True)
    else:
        st.error(f"❌ Une erreur est survenue lors du traitement : {response.text}")

def process_audio_to_audio(audio_file, audio_lang, pdf_lang, target_lang, pdf_files):
    url = "http://localhost:8000/process-audio-to-audio/"
    files = [('pdf_files', (file.name, file.getvalue(), 'application/pdf')) for file in pdf_files]
    files.append(('audio_file', ('audio_file.wav', audio_file.read(), 'audio/wav')))
    data = {
        'audio_lang': audio_lang,
        'pdf_lang': pdf_lang,
        'target_lang': target_lang
    }
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        result = response.json()
        st.success("✅ Audio traité avec succès !")
        
        st.markdown("### 📝 Transcription originale :")
        st.markdown(f'<div class="output-box">{result["transcription"]}</div>', unsafe_allow_html=True)
        
        if audio_lang != pdf_lang:
            st.markdown(f"### 🔄 Transcription traduite en {pdf_lang} :")
            st.markdown(f'<div class="output-box">{result["translated_transcription"]}</div>', unsafe_allow_html=True)
        
        st.markdown(f"### 💬 Réponse en {pdf_lang} :")
        st.markdown(f'<div class="output-box">{result["response_pdf_lang"]}</div>', unsafe_allow_html=True)
        
        if pdf_lang != target_lang:
            st.markdown(f"### 🔄 Réponse traduite en {target_lang} :")
            st.markdown(f'<div class="output-box">{result["translated_response"]}</div>', unsafe_allow_html=True)

        if result["response_audio"]:
            st.markdown(f"### 🔊 Audio de réponse en {target_lang} :")
            audio_bytes = base64.b64decode(result["response_audio"])
            st.audio(audio_bytes, format="audio/wav")
        else:
            st.warning("Aucun audio de réponse n'a été généré.")
    else:
        st.error(f"❌ Une erreur est survenue lors du traitement : {response.text}")
def main():
    # CSS personnalisé pour le style
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        color: #1E90FF;
        font-weight: bold;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #4CAF50;
        border-radius: 5px;
    }
    .output-box {
        background-color: #f0f0f0;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Titre avec style personnalisé
    st.markdown('<p class="big-font">Application de Traitement Audio & Texte</p>', unsafe_allow_html=True)

    # Menu pour sélectionner le type d'entrée
    page = option_menu("Menu Principal", ["Texte en Audio", "Audio en Texte", "Audio en Audio", "Text to Text"],
                       icons=["chat", "mic", "speaker", "chat"], menu_icon="cast", default_index=0)

    # Option "Texte en Audio"
    if page == "Texte en Audio":
        st.markdown("### 📝 Entrez votre question et sélectionnez les fichiers PDF")
        question = st.text_area("Entrez la question :")
        src_lang = st.selectbox("Sélectionnez la langue de votre question:", ["français", "anglais", "arabe", "darija"])
        pdf_lang = st.selectbox("Sélectionnez la langue des documents PDF:", ["français", "anglais", "arabe", "darija"])
        target_lang = st.selectbox("Sélectionnez la langue de la réponse audio:", ["français", "anglais", "arabe", "darija"])
        pdf_files = st.file_uploader("Sélectionnez un ou plusieurs fichiers PDF", type=["pdf"], accept_multiple_files=True)

        if st.button("🚀 Convertir en Audio"):
            if question and pdf_files:
                process_text_to_audio(question, src_lang, pdf_lang, target_lang, pdf_files)
            else:
                st.warning("⚠️ Veuillez entrer une question et sélectionner au moins un fichier PDF.")

    elif page == "Audio en Texte":
        st.markdown("### 📂 Téléchargez les fichiers Audio et PDF")
        audio_file = st.file_uploader("Téléchargez le fichier Audio (WAV, OPUS, ou MP3)", type=["wav", "opus", "mp3"])
        audio_lang = st.selectbox("Sélectionnez la langue de votre audio:", ["français", "anglais", "arabe", "darija"])
        pdf_lang = st.selectbox("Sélectionnez la langue des documents PDF:", ["français", "anglais", "arabe", "darija"])
        target_lang = st.selectbox("Sélectionnez la langue de la réponse:", ["français", "anglais", "arabe", "darija"])
        pdf_files = st.file_uploader("Téléchargez un ou plusieurs fichiers PDF", type=["pdf"], accept_multiple_files=True)

        if st.button("🚀 Traiter l'Audio"):
            if audio_file and pdf_files:
                process_audio_to_text(audio_file, audio_lang, pdf_lang, target_lang, pdf_files)
            else:
                st.warning("⚠️ Veuillez télécharger un fichier audio et au moins un fichier PDF.")

    elif page == "Audio en Audio":
        st.markdown("### 🎙️ Téléchargez un fichier audio et des fichiers PDF")
        audio_file = st.file_uploader("Téléchargez un fichier audio (WAV, MP3)", type=["wav", "mp3"])
        audio_lang = st.selectbox("Sélectionnez la langue de votre audio:", ["français", "anglais", "arabe", "darija"])
        pdf_lang = st.selectbox("Sélectionnez la langue des documents PDF:", ["français", "anglais", "arabe", "darija"])
        target_lang = st.selectbox("Sélectionnez la langue de la réponse audio:", ["français", "anglais", "arabe", "darija"])
        pdf_files = st.file_uploader("Téléchargez un ou plusieurs fichiers PDF", type=["pdf"], accept_multiple_files=True)

        if st.button("🚀 Traiter l'Audio"):
            if audio_file and pdf_files:
                process_audio_to_audio(audio_file, audio_lang, pdf_lang, target_lang, pdf_files)
            else:
                st.warning("⚠️ Veuillez télécharger un fichier audio et au moins un fichier PDF.")


    # Option "Text to Text"
    elif page == "Text to Text":
        st.markdown("### 📝 Entrez votre question et téléchargez un ou plusieurs fichiers PDF")
        question = st.text_input("Entrez votre question:")
        src_lang = st.selectbox("Sélectionnez la langue de votre question:", ["français", "anglais", "arabe", "darija"])
        pdf_lang = st.selectbox("Sélectionnez la langue des documents PDF:", ["français", "anglais", "arabe", "darija"])
        target_lang = st.selectbox("Sélectionnez la langue de la réponse:", ["français", "anglais", "arabe", "darija"])
        pdf_files = st.file_uploader("Téléchargez un ou plusieurs fichiers PDF", type=["pdf"], accept_multiple_files=True)

        if st.button("🚀 Traiter la question"):
            if question and pdf_files:
                with st.spinner('Traitement de la question en cours...'):
                    files = [('pdf_files', (file.name, file.getvalue(), 'application/pdf')) for file in pdf_files]
                    data = {
                        'question': question,
                        'src_lang': src_lang,
                        'pdf_lang': pdf_lang,
                        'target_lang': target_lang
                    }
                    response = requests.post(f"{API_BASE_URL}/process-text-to-text/", files=files, data=data)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.success("✅ Question traitée avec succès !")
                        
                        if src_lang != pdf_lang:
                            st.markdown(f"### 🔄 Question traduite en {pdf_lang} :")
                            st.markdown(f'<div class="output-box">{result["translated_question"]}</div>', unsafe_allow_html=True)
                        
                        st.markdown(f"### 💬 Réponse en {target_lang} :")
                        st.markdown(f'<div class="output-box">{result["translated_response"]}</div>', unsafe_allow_html=True)
                    else:
                        st.error(f"❌ Une erreur s'est produite lors du traitement : {response.text}")
            else:
                st.warning("⚠️ Veuillez entrer une question et télécharger au moins un fichier PDF.")

if __name__ == "__main__":
    main()
