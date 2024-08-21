# Audio Processing Application

## Description

Cette application de traitement audio et textuel permet à l'utilisateur d'effectuer diverses actions telles que :
- Conversion de texte en audio
- Transcription d'audio en texte
- Traduction de texte et d'audio
- Conversion d'audio en audio avec traduction

## Fonctionnalités

- **Conversion de Texte en Audio**
- **Transcription d'Audio en Texte**
- **Conversion d'Audio en Audio avec Traduction**
- **Traduction de Texte**

## Technologies utilisées

### Backend
- **FastAPI** : Framework Python pour la création d'API RESTful.
- **Transformers** : Bibliothèque pour l'utilisation de modèles de traitement du langage naturel (NLP).
- **PyPDF2** : Bibliothèque pour l'extraction de texte à partir de fichiers PDF.
- **SoundFile** : Bibliothèque pour la lecture et l'écriture de fichiers audio.
- **NumPy** : Bibliothèque pour le traitement numérique.
- **Librosa** : Bibliothèque pour le traitement du signal audio.

### Frontend
- **Streamlit** : Framework Python pour la création d'applications web interactives.

### Autres
- **FFMPEG** : Outil de traitement multimédia utilisé pour la conversion des fichiers audio.
- **Docker** : Outil de containerisation pour faciliter le déploiement de l'application.

## Configuration et Démarrage

1. Clonez le dépôt GitHub :

    ```bash
    git clone https://github.com/votre-utilisateur/audio-processing-app.git
    ```

2. Créez et activez un environnement virtuel Python :

    ```bash
    cd audio-processing-app
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances requises :

    ```bash
    pip install -r requirements.txt
    ```

4. Définissez le chemin d'accès à l'exécutable FFMPEG dans le fichier `api/api_endpoints.py` :

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

## Déploiement avec Docker

1. Construisez l'image Docker :

    ```bash
    docker build -t audio-processing-app .
    ```

2. Exécutez le conteneur Docker :

    ```bash
    docker run -p 8000:8000 -p 8501:8501 audio-processing-app
    ```

    L'application sera accessible aux adresses :
    - **API FastAPI** : [http://localhost:8000](http://localhost:8000)
    - **Interface Streamlit** : [http://localhost:8501](http://localhost:8501)

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des issues ou à soumettre des pull requests si vous avez des suggestions d'amélioration ou si vous avez identifié des bugs.

## Licence

Ce projet est sous licence MIT.
