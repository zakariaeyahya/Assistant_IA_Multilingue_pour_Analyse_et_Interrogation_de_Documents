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
GROQ_API_KEY = "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"
FFMPEG_PATH = "C:\\Users\\HP\\anaconda3\\pkgs\\ffmpeg-4.3.1-ha925a31_0\\Library\\bin\\ffmpeg.exe"
API_BASE_URL = "http://localhost:8000"  # Adjust this to your API's address
import streamlit as st
from streamlit_option_menu import option_menu
import requests
import base64
import os
import sys
import tempfile
import soundfile as sf
import numpy as np
from scipy.io import wavfile
import io

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Configurations et constantes
API_BASE_URL = "http://localhost:8000"
SUPPORTED_LANGUAGES = ["français", "anglais", "arabe", "darija"]

# Fonction pour le style CSS
def load_css():
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

# Fonction utilitaire pour normaliser l'audio
def normalize_audio(audio_array):
    if audio_array.size == 0:
        st.warning("Le tableau audio est vide.")
        return np.array([], dtype=np.int16)

    if len(audio_array.shape) > 1 and audio_array.shape[0] > 1:
        audio_array = np.mean(audio_array, axis=0)
    
    max_abs_val = np.max(np.abs(audio_array))
    if max_abs_val == 0:
        st.warning("Le tableau audio ne contient que des zéros.")
        return np.zeros(audio_array.shape, dtype=np.int16)

    audio_array = audio_array / max_abs_val
    audio_array_int16 = (audio_array * 32767).astype(np.int16)
    
    return audio_array_int16

# Fonctions pour chaque page
def page_accueil():
    st.markdown('<p class="big-font">Bienvenue dans l\'Application de Traitement Audio & Texte</p>', unsafe_allow_html=True)
    st.write("Cette application vous permet de réaliser diverses opérations de traitement de texte et d'audio.")
    st.write("Utilisez le menu de navigation pour accéder aux différentes fonctionnalités :")
    st.write("- **Text to Text** : Traduisez du texte et obtenez des réponses basées sur des documents PDF.")
    st.write("- **Text to Speech** : Convertissez du texte en audio dans différentes langues.")
    st.write("- **Speech to Text** : Transcrivez de l'audio en texte et obtenez des traductions.")
    st.write("- **À Propos** : Informations sur l'application et son utilisation.")
    
    st.info("Pour commencer, sélectionnez une option dans le menu à gauche.")

def page_text_to_text():
    st.markdown("### 📝 Text to Text")
    question = st.text_input("Entrez votre question:")
    src_lang = st.selectbox("Langue de la question:", SUPPORTED_LANGUAGES)
    pdf_lang = st.selectbox("Langue des documents PDF:", SUPPORTED_LANGUAGES)
    target_lang = st.selectbox("Langue de la réponse:", SUPPORTED_LANGUAGES)
    pdf_files = st.file_uploader("Téléchargez un ou plusieurs fichiers PDF", type=["pdf"], accept_multiple_files=True)

    if st.button("🚀 Traiter"):
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
def page_text_to_speech():
    st.markdown("### 🗣️ Text to Speech")
    
    text_input = st.text_area("Entrez le texte à convertir en audio:", height=150)
    src_lang = st.selectbox("Langue du texte:", SUPPORTED_LANGUAGES)
    pdf_lang = st.selectbox("Langue des documents PDF:", SUPPORTED_LANGUAGES)  # Ajout de cette ligne
    target_lang = st.selectbox("Langue de l'audio:", SUPPORTED_LANGUAGES)
    pdf_files = st.file_uploader("Téléchargez un ou plusieurs fichiers PDF de référence (optionnel)", type=["pdf"], accept_multiple_files=True)

    if st.button("🚀 Convertir en Audio"):
        if text_input:
            with st.spinner('Conversion du texte en audio en cours...'):
                files = [('pdf_files', (file.name, file.getvalue(), 'application/pdf')) for file in pdf_files] if pdf_files else []
                data = {
                    'question': text_input,
                    'src_lang': src_lang,
                    'pdf_lang': pdf_lang,  # Modification de cette ligne
                    'target_lang': target_lang
                }
                
                try:
                    response = requests.post(f"{API_BASE_URL}/process-text-to-audio/", files=files, data=data)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.success("✅ Texte converti en audio avec succès !")
                        
                        if 'translated_question' in result and src_lang != target_lang:
                            st.markdown(f"### 🔄 Texte traduit en {target_lang} :")
                            st.markdown(f'<div class="output-box">{result["translated_question"]}</div>', unsafe_allow_html=True)
                        
                        if 'translated_response' in result:
                            st.markdown(f"### 💬 Réponse (si applicable) :")
                            st.markdown(f'<div class="output-box">{result["translated_response"]}</div>', unsafe_allow_html=True)
                        
                        if 'audio' in result:
                            st.markdown(f"### 🔊 Audio généré :")
                            audio_bytes = base64.b64decode(result["audio"])
                            st.audio(audio_bytes, format="audio/wav")
                        else:
                            st.warning("Aucun audio n'a été généré.")
                    else:
                        st.error(f"❌ Une erreur s'est produite lors de la conversion : {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Erreur de connexion à l'API : {str(e)}")
        else:
            st.warning("⚠️ Veuillez entrer du texte à convertir en audio.")

    # Ajout d'informations supplémentaires
    with st.expander("ℹ️ Comment utiliser cette fonctionnalité"):
        st.write("""
        1. Entrez le texte que vous souhaitez convertir en audio dans la zone de texte.
        2. Sélectionnez la langue du texte d'entrée.
        3. Sélectionnez la langue des documents PDF de référence .
        4. Choisissez la langue dans laquelle vous voulez que l'audio soit généré.
        5. Si vous avez des documents PDF de référence, vous pouvez les télécharger (facultatif).
        6. Cliquez sur le bouton 'Convertir en Audio' pour lancer le processus.
        7. Une fois le traitement terminé, vous pourrez écouter l'audio généré directement dans l'application.
        """)
# Modifiez les fonctions page_speech_to_text() et page_speech_to_speech() comme suit:

def page_speech_to_text():
    st.markdown("### 🎙️ Speech to Text")
    
    audio_file = st.file_uploader("Téléchargez un fichier audio (WAV, MP3, OPUS)", type=["wav", "mp3", "opus"])
    audio_lang = st.selectbox("Langue de l'audio:", SUPPORTED_LANGUAGES)
    pdf_lang = st.selectbox("Langue des documents PDF:", SUPPORTED_LANGUAGES)
    target_lang = st.selectbox("Langue de la transcription:", SUPPORTED_LANGUAGES)
    pdf_files = st.file_uploader("Téléchargez un ou plusieurs fichiers PDF de référence (optionnel)", type=["pdf"], accept_multiple_files=True)

    if st.button("🚀 Transcrire"):
        if audio_file:
            with st.spinner('Transcription de l\'audio en cours...'):
                # Afficher l'audio d'entrée
                st.markdown("### 🎵 Audio d'entrée:")
                st.audio(audio_file, format=f"audio/{audio_file.type}")
                
                files = [('audio_file', (audio_file.name, audio_file.getvalue(), f'audio/{audio_file.type}'))]
                if pdf_files:
                    files.extend([('pdf_files', (file.name, file.getvalue(), 'application/pdf')) for file in pdf_files])
                
                data = {
                    'audio_lang': audio_lang,
                    'pdf_lang': pdf_lang,
                    'target_lang': target_lang
                }
                
                try:
                    response = requests.post(f"{API_BASE_URL}/process-audio-to-text/", files=files, data=data)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.success("✅ Audio transcrit avec succès !")
                        
                        if 'transcription' in result:
                            st.markdown("### 📝 Transcription originale :")
                            st.markdown(f'<div class="output-box">{result["transcription"]}</div>', unsafe_allow_html=True)
                        
                        if 'translated_transcription' in result and audio_lang != target_lang:
                            st.markdown(f"### 🔄 Transcription traduite en {target_lang} :")
                            st.markdown(f'<div class="output-box">{result["translated_transcription"]}</div>', unsafe_allow_html=True)
                        
                        if 'response_pdf_lang' in result:
                            st.markdown(f"### 💬 Réponse basée sur les PDF (si applicable) :")
                            st.markdown(f'<div class="output-box">{result["response_pdf_lang"]}</div>', unsafe_allow_html=True)
                        
                        if 'translated_response' in result and audio_lang != target_lang:
                            st.markdown(f"### 🔄 Réponse traduite en {target_lang} :")
                            st.markdown(f'<div class="output-box">{result["translated_response"]}</div>', unsafe_allow_html=True)
                        
                        # Ajout de l'audio de sortie correspondant à la transcription
                        if 'output_audio' in result:
                            st.markdown(f"### 🔊 Audio de la transcription en {target_lang} :")
                            audio_bytes = base64.b64decode(result["output_audio"])
                            st.audio(audio_bytes, format="audio/wav")
                    else:
                        st.error(f"❌ Une erreur s'est produite lors de la transcription : {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Erreur de connexion à l'API : {str(e)}")
        else:
            st.warning("⚠️ Veuillez télécharger un fichier audio à transcrire.")

    # Mise à jour des informations d'utilisation
    with st.expander("ℹ️ Comment utiliser cette fonctionnalité"):
        st.write("""
        1. Téléchargez un fichier audio (formats supportés : WAV, MP3, OPUS).
        2. Sélectionnez la langue de l'audio.
        3. Sélectionnez la langue des documents PDF de référence (si applicable).
        4. Choisissez la langue dans laquelle vous voulez que la transcription soit faite.
        5. Si vous avez des documents PDF de référence, vous pouvez les télécharger (facultatif).
        6. Cliquez sur le bouton 'Transcrire' pour lancer le processus.
        7. Une fois le traitement terminé, vous pourrez :
           - Écouter l'audio d'entrée original
           - Voir la transcription originale et, si applicable, sa traduction
           - Écouter l'audio généré correspondant à la transcription
           - Voir une réponse basée sur les PDF fournis, si applicable
        """)

def page_speech_to_speech():
    st.markdown("### 🎙️🔊 Speech to Speech")
    
    audio_file = st.file_uploader("Téléchargez un fichier audio (WAV, MP3, OPUS)", type=["wav", "mp3", "opus"])
    audio_lang = st.selectbox("Langue de l'audio d'entrée:", SUPPORTED_LANGUAGES)
    pdf_lang = st.selectbox("Langue des documents PDF:", SUPPORTED_LANGUAGES)
    target_lang = st.selectbox("Langue de l'audio de sortie:", SUPPORTED_LANGUAGES)
    pdf_files = st.file_uploader("Téléchargez un ou plusieurs fichiers PDF de référence (optionnel)", type=["pdf"], accept_multiple_files=True)

    if st.button("🚀 Traiter et Convertir"):
        if audio_file:
            with st.spinner('Traitement de l\'audio en cours...'):
                # Afficher l'audio d'entrée
                st.markdown("### 🎵 Audio d'entrée:")
                st.audio(audio_file, format=f"audio/{audio_file.type}")
                
                files = [('audio_file', (audio_file.name, audio_file.getvalue(), f'audio/{audio_file.type}'))]
                if pdf_files:
                    files.extend([('pdf_files', (file.name, file.getvalue(), 'application/pdf')) for file in pdf_files])
                
                data = {
                    'audio_lang': audio_lang,
                    'pdf_lang': pdf_lang,
                    'target_lang': target_lang
                }
                
                try:
                    response = requests.post(f"{API_BASE_URL}/process-audio-to-audio/", files=files, data=data)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.success("✅ Audio traité et converti avec succès !")
                        
                        if 'transcription' in result:
                            st.markdown("### 📝 Transcription originale :")
                            st.markdown(f'<div class="output-box">{result["transcription"]}</div>', unsafe_allow_html=True)
                        
                        if 'translated_transcription' in result and audio_lang != target_lang:
                            st.markdown(f"### 🔄 Transcription traduite en {target_lang} :")
                            st.markdown(f'<div class="output-box">{result["translated_transcription"]}</div>', unsafe_allow_html=True)
                        
                        if 'response_pdf_lang' in result:
                            st.markdown(f"### 💬 Réponse basée sur les PDF (si applicable) :")
                            st.markdown(f'<div class="output-box">{result["response_pdf_lang"]}</div>', unsafe_allow_html=True)
                        
                        if 'translated_response' in result and audio_lang != target_lang:
                            st.markdown(f"### 🔄 Réponse traduite en {target_lang} :")
                            st.markdown(f'<div class="output-box">{result["translated_response"]}</div>', unsafe_allow_html=True)
                        
                        if 'response_audio' in result:
                            st.markdown(f"### 🔊 Audio généré en {target_lang} :")
                            audio_bytes = base64.b64decode(result["response_audio"])
                            st.audio(audio_bytes, format="audio/wav")
                        else:
                            st.warning("Aucun audio de réponse n'a été généré.")
                    else:
                        st.error(f"❌ Une erreur s'est produite lors du traitement : {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Erreur de connexion à l'API : {str(e)}")
        else:
            st.warning("⚠️ Veuillez télécharger un fichier audio à traiter.")

    # Mise à jour des informations d'utilisation
    with st.expander("ℹ️ Comment utiliser cette fonctionnalité"):
        st.write("""
        1. Téléchargez un fichier audio (formats supportés : WAV, MP3, OPUS).
        2. Sélectionnez la langue de l'audio d'entrée.
        3. Sélectionnez la langue des documents PDF de référence (si applicable).
        4. Choisissez la langue dans laquelle vous voulez que l'audio de sortie soit généré.
        5. Si vous avez des documents PDF de référence, vous pouvez les télécharger (facultatif).
        6. Cliquez sur le bouton 'Traiter et Convertir' pour lancer le processus.
        7. Une fois le traitement terminé, vous pourrez :
           - Écouter l'audio d'entrée original
           - Voir la transcription originale et sa traduction
           - Écouter l'audio généré dans la langue cible
           - Voir une réponse basée sur les PDF fournis, si applicable
        """)
def page_a_propos():
    st.markdown("### 📚 À Propos de l'Application")
    
    st.write("""
    Bienvenue dans notre Application de Traitement Audio & Texte !
    
    Cette application a été développée pour faciliter le traitement et la traduction de texte et d'audio, en s'appuyant sur des documents PDF comme source de contexte. Voici un aperçu de ses principales fonctionnalités :
    """)

    st.markdown("""
    #### 🔧 Fonctionnalités principales :
    
    1. **Text to Text** : 
       - Traduisez du texte d'une langue à une autre.
       - Obtenez des réponses à vos questions basées sur le contenu de documents PDF.

    2. **Text to Speech** : 
       - Convertissez du texte écrit en audio dans différentes langues.
       - Utilisez optionnellement des PDF pour enrichir le contenu audio généré.

    3. **Speech to Text** : 
       - Transcrivez des fichiers audio en texte.
       - Traduisez la transcription dans une autre langue si nécessaire.
       - Obtenez des informations supplémentaires basées sur des PDF de référence.

    #### 🌍 Langues supportées :
    - Français
    - Anglais
    - Arabe
    - Darija (Arabe marocain)

    #### 🛠️ Technologies utilisées :
    - Backend : FastAPI, Python
    - Frontend : Streamlit
    - Modèles de langage : Seamless M4T pour la traduction et le traitement audio
    - Base de connaissances : Groq pour l'analyse des PDF et la génération de réponses
    """)

    st.info("""
    ℹ️ **Note importante** : Cette application est conçue pour traiter des informations générales. 
    Veuillez ne pas utiliser de données sensibles ou confidentielles.
    """)

    st.markdown("""
    #### 📞 Support et Contact
    
    Si vous rencontrez des problèmes ou si vous avez des suggestions d'amélioration, 
    n'hésitez pas à contacter notre équipe de support à l'adresse : support@example.com

    #### 🔄 Mises à jour
    
    Nous travaillons constamment à l'amélioration de cette application. 
    Consultez régulièrement cette page pour être informé des dernières mises à jour et nouvelles fonctionnalités.

    #### 📜 Licence

    Cette application est distribuée sous licence MIT. Pour plus de détails, veuillez consulter le fichier LICENSE inclus dans le dépôt du projet.
    """)

    # Vous pouvez ajouter ici un lien vers les conditions d'utilisation ou la politique de confidentialité si nécessaire
    st.markdown("[Conditions d'utilisation](#) | [Politique de confidentialité](#)")
def main():
    load_css()

    # Navigation
    with st.sidebar:
        choice = option_menu("Menu Principal", ["Accueil", "Text to Text", "Text to Speech", "Speech to Text", "Speech to Speech", "À Propos"],
                             icons=['house', 'chat-dots', 'megaphone', 'mic', 'headset', 'info-circle'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
                                 "container": {"padding": "5!important", "background-color": "#fafafa"},
                                 "icon": {"color": "orange", "font-size": "25px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                 "nav-link-selected": {"background-color": "#02ab21"},
                             })

    # Affichage de la page correspondante
    if choice == "Accueil":
        page_accueil()
    elif choice == "Text to Text":
        page_text_to_text()
    elif choice == "Text to Speech":
        page_text_to_speech()
    elif choice == "Speech to Text":
        page_speech_to_text()
    elif choice == "Speech to Speech":
        page_speech_to_speech()
    elif choice == "À Propos":
        page_a_propos()

if __name__ == "__main__":
    main()
