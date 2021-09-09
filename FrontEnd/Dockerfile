FROM python:3.8

# le dossier /code sera le dossier courant du container
WORKDIR /src

# Copy du fichier dans le container 
COPY requirements.txt .

# installation des biblioth�ques sp�cifi� dans le fichier 
RUN pip install -r requirements.txt

# Copie du contenu du dossier 'src' dans le container
COPY src/ .
EXPOSE 5000
# commande a executer au lancement du container 
CMD [ "python", "./main.py" ] 