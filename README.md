# Darija Audio Processing Application
![Uploading image.png…]()

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

## Technologies Utilisées

### Backend

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) : Langage de programmation principal.
- ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) : Framework Python pour la création d'API RESTful.
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) : Framework Python pour la création d'applications web interactives.
- ![PyPDF2](https://img.shields.io/badge/PyPDF2-FFD43B?style=for-the-badge&logo=python&logoColor=blue) : Bibliothèque pour l'extraction de texte à partir de fichiers PDF.
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) : Bibliothèque pour le traitement numérique.
- ![SoundFile](https://img.shields.io/badge/SoundFile-008080?style=for-the-badge&logo=soundfile&logoColor=white) : Bibliothèque pour la lecture et l'écriture de fichiers audio.
- ![Librosa](https://img.shields.io/badge/Librosa-1F77B4?style=for-the-badge&logo=librosa&logoColor=white) : Bibliothèque pour le traitement du signal audio.
- ![Transformers](https://img.shields.io/badge/Transformers-FF9900?style=for-the-badge&logo=transformers&logoColor=white) : Bibliothèque pour les modèles de traitement du langage naturel (NLP), utilisée pour la traduction et la conversion texte-parole.
- ![LangChain](https://img.shields.io/badge/LangChain-00BFFF?style=for-the-badge&logo=langchain&logoColor=white) : Bibliothèque pour construire des applications d'intelligence artificielle conversationnelle.
- ![Requests](https://img.shields.io/badge/Requests-FF5733?style=for-the-badge&logo=requests&logoColor=white) : Bibliothèque pour effectuer des requêtes HTTP.
- ![Base64](https://img.shields.io/badge/Base64-9B59B6?style=for-the-badge&logo=base64&logoColor=white) : Module pour encoder et décoder les données en Base64.
- ![IO](https://img.shields.io/badge/IO-34495E?style=for-the-badge&logo=io&logoColor=white) : Module pour manipuler les flux d'entrée/sortie.
- ![OS](https://img.shields.io/badge/OS-2ECC71?style=for-the-badge&logo=os&logoColor=white) : Module pour interagir avec le système d'exploitation.
- ![Tempfile](https://img.shields.io/badge/Tempfile-7D3C5C?style=for-the-badge&logo=tempfile&logoColor=white) : Module pour créer et utiliser des fichiers temporaires.
- ![Logging](https://img.shields.io/badge/Logging-DC7633?style=for-the-badge&logo=logging&logoColor=white) : Module pour la journalisation des événements.

### Modèles de Langage Pré-entraînés

- ![Seamless M4T-v2](https://img.shields.io/badge/Seamless%20M4T-v2-9C27B0?style=for-the-badge&logo=facebook&logoColor=white) : Modèle de traduction et de conversion texte-parole développé par Facebook.

### Outils et Technologies

- ![FFMPEG](https://img.shields.io/badge/FFMPEG-007808?style=for-the-badge&logo=ffmpeg&logoColor=white) : Outil de traitement multimédia utilisé pour la conversion des fichiers audio.
- ![Groq](https://img.shields.io/badge/Groq-FF5722?style=for-the-badge&logo=groq&logoColor=white) : API permettant d'interagir avec un système de questions-réponses basé sur des documents.

### Infrastructure

- ![Uvicorn](https://img.shields.io/badge/Uvicorn-6C63FF?style=for-the-badge&logo=uvicorn&logoColor=white) : Serveur ASGI (Asynchronous Server Gateway Interface) pour FastAPI.



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
    FFMPEG_PATH = r"FFMPEG_PATH"
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
