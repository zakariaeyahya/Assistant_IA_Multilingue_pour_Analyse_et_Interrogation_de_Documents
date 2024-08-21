# Darija Audio Processing Application

## Description

Cette application de traitement audio et textuel, focalisée sur la langue marocaine darija, permet à l'utilisateur d'effectuer diverses actions telles que la conversion de texte en audio, la transcription d'audio en texte, la traduction de texte et d'audio, et la conversion d'audio en audio avec traduction. C'est un chatbot conçu pour répondre aux questions des utilisateurs en utilisant les informations contenues dans les fichiers PDF fournis.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Autres](#autres)
- [Configuration et Démarrage](#configuration-et-démarrage)
- [Contribution](#contribution)
- [Licence](#licence)

## Fonctionnalités

- **Conversion de Texte en Audio :**

  L'utilisateur peut entrer une question en darija, sélectionner les langues source et cible, ainsi que les fichiers PDF à utiliser comme contexte. L'application génère une réponse audio traduite dans la langue cible.

- **Transcription d'Audio en Texte :**

  L'utilisateur peut télécharger un fichier audio en darija, sélectionner les langues de l'audio et du texte de sortie, ainsi que les fichiers PDF à utiliser comme contexte. L'application génère une transcription textuelle traduite dans la langue cible.

- **Conversion d'Audio en Audio avec Traduction :**

  L'utilisateur peut télécharger un fichier audio en darija, sélectionner les langues de l'audio et du texte de sortie, ainsi que les fichiers PDF à utiliser comme contexte. L'application génère une réponse audio traduite dans la langue cible.

- **Traduction de Texte :**

  L'utilisateur peut entrer une question en darija, sélectionner les langues source et cible, ainsi que les fichiers PDF à utiliser comme contexte. L'application génère une traduction textuelle de la question et de la réponse.

Ce chatbot utilise les informations contenues dans les fichiers PDF fournis pour répondre aux questions des utilisateurs, en s'appuyant sur des technologies de traitement du langage naturel, de traduction et de synthèse vocale.

## Technologies utilisées

### Backend

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) : Langage de programmation principal.
- ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) : Framework Python pour la création d'API RESTful.
- ![Transformers](https://img.shields.io/badge/Transformers-FF9900?style=for-the-badge&logo=transformers&logoColor=white) : Bibliothèque pour l'utilisation de modèles de traitement du langage naturel (NLP).
- ![PyPDF2](https://img.shields.io/badge/PyPDF2-FFD43B?style=for-the-badge&logo=python&logoColor=blue) : Bibliothèque pour l'extraction de texte à partir de fichiers PDF.
- ![SoundFile](https://img.shields.io/badge/SoundFile-008080?style=for-the-badge&logo=soundfile&logoColor=white) : Bibliothèque pour la lecture et l'écriture de fichiers audio.
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) : Bibliothèque pour le traitement numérique.
- ![Librosa](https://img.shields.io/badge/Librosa-1F77B4?style=for-the-badge&logo=librosa&logoColor=white) : Bibliothèque pour le traitement du signal audio.


### Frontend

- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) : Framework Python pour la création d'applications web interactives.

### Autres

- ![FFMPEG](https://img.shields.io/badge/FFMPEG-007808?style=for-the-badge&logo=ffmpeg&logoColor=white) : Outil de traitement multimédia utilisé pour la conversion des fichiers audio.


## Configuration et Démarrage

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/votre-utilisateur/audio-processing-app.git

2.Créez et activez un environnement virtuel Python :
cd audio-processing-app
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`

3. Installez les dépendances requises  :

    pip install -r requirements.txt


4. Définissez le chemin d'accès à l'exécutable FFMPEG dans le fichier api/api_endpoints.py  :

    ```python
    FFMPEG_PATH = r"C:\Users\HP\anaconda3\pkgs\ffmpeg-4.3.1-ha925a31_0\Library\bin\ffmpeg.exe"
    ```

5. Démarrez l'application FastAPI :

    ```bash
    cd api
    python api_endpoints.py
    ```

6. Démarrez l'application Streamlit :

    ```bash
    cd streamlit
    streamlit run audio_processing_app.py
    ```

    L'application sera accessible à l'adresse [http://localhost:8501](http://localhost:8501).

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des issues ou à soumettre des pull requests si vous avez des suggestions d'amélioration ou si vous avez identifié des bugs.

## Licence

Ce projet est sous licence MIT.
