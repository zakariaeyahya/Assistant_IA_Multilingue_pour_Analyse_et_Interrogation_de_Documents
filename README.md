<div class="document-container">
  <div class="document">
    <div class="document-header">
      <h1>Darija Audio Processing Application</h1>
      <img src="https://github.com/user-attachments/assets/46c39672-9cfa-435f-9eac-f257f5337f29" alt="image">
    </div>
    <div class="document-content">
      <h2>Description</h2>
      <p>Cette application de traitement audio et textuel, focalisée sur la langue marocaine darija, permet à l'utilisateur d'effectuer diverses actions telles que la conversion de texte en audio, la transcription d'audio en texte, la traduction de texte et d'audio, et la conversion d'audio en audio avec traduction. C'est un chatbot conçu pour répondre aux questions des utilisateurs en utilisant les informations contenues dans les fichiers PDF fournis.</p>
      <h2>Table des matières</h2>
      <ul>
        <li><a href="#fonctionnalités">Fonctionnalités</a></li>
        <li><a href="#technologies-utilisées">Technologies utilisées</a>
          <ul>
            <li><a href="#backend">Backend</a></li>
            <li><a href="#frontend">Frontend</a></li>
            <li><a href="#autres">Autres</a></li>
          </ul>
        </li>
        <li><a href="#configuration-et-démarrage">Configuration et Démarrage</a></li>
        <li><a href="#contribution">Contribution</a></li>
        <li><a href="#licence">Licence</a></li>
      </ul>
      <h2 id="fonctionnalités">Fonctionnalités</h2>
      <ul>
        <li><strong>Conversion de Texte en Audio :</strong>
          <p>L'utilisateur peut entrer une question en darija, sélectionner les langues source et cible, ainsi que les fichiers PDF à utiliser comme contexte. L'application génère une réponse audio traduite dans la langue cible.</p>
        </li>
        <li><strong>Transcription d'Audio en Texte :</strong>
          <p>L'utilisateur peut télécharger un fichier audio en darija, sélectionner les langues de l'audio et du texte de sortie, ainsi que les fichiers PDF à utiliser comme contexte. L'application génère une transcription textuelle traduite dans la langue cible.</p>
        </li>
        <li><strong>Conversion d'Audio en Audio avec Traduction :</strong>
          <p>L'utilisateur peut télécharger un fichier audio en darija, sélectionner les langues de l'audio et du texte de sortie, ainsi que les fichiers PDF à utiliser comme contexte. L'application génère une réponse audio traduite dans la langue cible.</p>
        </li>
        <li><strong>Traduction de Texte :</strong>
          <p>L'utilisateur peut entrer une question en darija, sélectionner les langues source et cible, ainsi que les fichiers PDF à utiliser comme contexte. L'application génère une traduction textuelle de la question et de la réponse.</p>
        </li>
      </ul>
      <p>Ce chatbot utilise les informations contenues dans les fichiers PDF fournis pour répondre aux questions des utilisateurs, en s'appuyant sur des technologies de traitement du langage naturel, de traduction et de synthèse vocale.</p>
      <h2 id="technologies-utilisées">Technologies Utilisées</h2>
      <h3 id="backend">Backend</h3>
      <ul>
        <li><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"> : Langage de programmation principal.</li>
        <li><img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"> : Framework Python pour la création d'API RESTful.</li>
        <li><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"> : Framework Python pour la création d'applications web interactives.</li>
        <li><img src="https://img.shields.io/badge/PyPDF2-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="PyPDF2"> : Bibliothèque pour l'extraction de texte à partir de fichiers PDF.</li>
        <li><img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"> : Bibliothèque pour le traitement numérique.</li>
        <li><img src="https://img.shields.io/badge/SoundFile-008080?style=for-the-badge&logo=soundfile&logoColor=white" alt="SoundFile"> : Bibliothèque pour la lecture et l'écriture de fichiers audio.</li>
        <li><img src="https://img.shields.io/badge/Librosa-1F77B4?style=for-the-badge&logo=librosa&logoColor=white" alt="Librosa"> : Bibliothèque pour le traitement du signal audio.</li>
        <li><img src="https://img.shields.io/badge/Transformers-FF9900?style=for-the-badge&logo=transformers&logoColor=white" alt="Transformers"> : Bibliothèque pour les modèles de traitement du langage naturel (NLP), utilisée pour la traduction et la conversion texte-parole.</li>
        <li><img src="https://img.shields.io/badge/LangChain-00BFFF?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"> : Bibliothèque pour construire des applications d'intelligence artificielle conversationnelle.</li>
        <li><img src="https://img.shields.io/badge/Requests-FF5733?style=for-the-badge&logo=requests&logoColor=white" alt="Requests"> : Bibliothèque pour effectuer des requêtes HTTP.</li>
        <li><img src="https://img.shields.io/badge/Base64-9B59B6?style=for-the-badge&logo=base64&logoColor=white" alt="Base64"> : Module pour encoder et décoder les données en Base64.</li>
        <li><img src="https://img.shields.io/badge/IO-34495E?style=for-the-badge&logo=io&logoColor=white" alt="IO"> : Module pour manipuler les flux d'entrée/sortie.</li>
        <li><img src="https://img.shields.io/badge/OS-2ECC71?style=for-the-badge&logo=os&logoColor=white" alt="OS"> : Module pour interagir avec le système d'exploitation.</li>
        <li><img src="https://img.shields.io/badge/Tempfile-7D3C5C?style=for-the-badge&logo=tempfile&logoColor=white" alt="Tempfile"> : Module pour créer et utiliser des fichiers temporaires.</li>
        <li><img src="https://img.shields.io/badge/Logging-DC7633?style=for-the-badge&logo=logging&logoColor=white" alt="Logging"> : Module pour la journalisation des événements.</li>
      </ul>
      <h3 id="modèles-de-langage-pré-entraînés">Modèles de Langage Pré-entraînés</h3>
      <ul>
        <li><img src="https://img.shields.io/badge/Seamless%20M4T-v2-9C27B0?style=for-the-badge&logo=facebook&logoColor=white" alt="Seamless M4T-v2"> : Modèle de traduction et de conversion texte-parole développé par Facebook.</li>
      </ul>
      <h3 id="outils-et-technologies">Outils et Technologies</h3>
      <ul>
        <li><img src="https://img.shields.io/badge/FFMPEG-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" alt="FFMPEG"> : Outil de traitement multimédia utilisé pour la conversion des fichiers audio.</li>
        <li><img src="https://img.shields.io/badge/Groq-FF5722?style=for-the-badge&logo=groq&logoColor=white" alt="Groq"> : API permettant d'interagir avec un système de questions-réponses basé sur des documents.</li>
      </ul>
      <h3 id="infrastructure">Infrastructure</h3>
      <ul>
        <li><img src="https://img.shields.io/badge/Uvicorn-6C63FF?style=for-the-badge&logo=uvicorn&logoColor=white" alt="Uvicorn"> : Serveur ASGI (Asynchronous Server Gateway Interface) pour FastAPI.</li>
      </ul>
    </div>
  </div>
</div>


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
