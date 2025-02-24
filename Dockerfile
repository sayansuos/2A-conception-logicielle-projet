# On part d'un environnement Ubuntu 22.04
FROM python:3.10

# On copie les fichiers de notre projet dans l'environnement
COPY . .

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0
    
# On installe les dépendances à partir du fichier requirements.txt
RUN pip install -r requirements.txt 

# On définit la commande à exécuter pour lancer notre application
ENTRYPOINT ["python", "main.py"]