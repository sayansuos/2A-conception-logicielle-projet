# League of Lilian

Ce projet a été réalisé dans le cadre du cours de Conception de Logiciel de 2ème année à l'ENSAI.

## Application

Cette application est faite pour les joueurs de League of Legends qui veulent optimiser leurs choix de champions. L'idée est simple : tu précises les champions déjà choisis (alliés et ennemis), ceux qui sont bannis, et l'application te recommande le meilleur champion à jouer en fonction des synergies et des contres.

En plus de ça, tu peux sauvegarder tes builds préférés pour chaque champion et les retrouver facilement plus tard. Plus besoin de galérer à se souvenir de la meilleure combinaison d'objets, tout est stocké dans l'appli ! 🎮🔥

## Installation de l'application

1. Récupérez votre clé d'API Riot. Pour cela, allez à cette adresse : https://developer.riotgames.com, connectez vous ou créez un compte et générez une clé d'API.

2. Depuis ```./backend```: créez le fichier ```.env.local``` et copiez y le contenu de ```.env.template```.

3. Modifiez la ligne suivante : **DATA_PWD=XXXX-XXXX-XXX** en remplaçant ```XXXX-XXXX-XXX```par votre propre clé d'API Riot.

## Lancer l'application en local avec Docker

### 1. Lancer l'API backend

1. Depuis ```./kurbenetes/backend```: créez le fichier ```configmap.yaml``` et copiez y le contenu de ```configmap_template.yaml```.

2. Renseignez ```DATA_PWD:``` avec votre propre clé API Riot.

3. Depuis la racine du projet, exécutez : 

```
cd kurbenetes
cd backend
docker build -t backend-app .
docker run -d --name backend-container -p 8000:8000 backend-app
docker ps  # Vérifier que le conteneur tourne
```

L'API sera disponible à :

- ```http://localhost:8000```
- Swagger UI : ```http://localhost:8000/docs``` ou accessible en permanence depuis : https://lol.kub.sspcloud.fr/docs.

### 2. Lancer l'application frontend

Depuis la racine du projet, exécutez : 

```
cd kurbenetes
cd frontend
docker build -t frontend-app .
docker run -d -e VITE_API_URL=http://localhost:8000 --name frontend-container -p 8080:80 frontend-app
docker ps  # Vérifier que le conteneur tourne
```

L'application web sera disponible à :

- ```http://localhost:8000``` ou accessible en permanence depuis : https://lol-app.kub.sspcloud.fr.