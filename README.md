## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver` ou `gunicorn oc_lettings_site.wsgi`
- Aller sur [http://127.0.0.1:8000](http://127.0.0.1:8000) dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Déploiement

Le pipeline choisi pour déployer ce projet est le suivant : 

1. dev-local
2. git-hub
3. circleCI
4. Docker Hub & Heroku
5. Sentry.

Lorsque l'on soumet un commit sur GitHub, circleCI va automatiquement déclencher un processus qui consiste à aller chercher le commit en question, à le conteneuriser pour l'envoyer sur Docker Hub et sur Heroku ou il est rendu accessible à qui le souhaite.

#### Configuration nécessaire

Outre le compte github avec lequel vous pouvez récupèrer ce projet, il vous faudra également des comptes pour les sites suivants :

- [CircleCi](https://circleci.com/signup/)
- [Docker Hub](https://hub.docker.com/signup?next=%2Forgs%3Fref%3Dlogin)
- [Heroku](https://signup.heroku.com/)
- [Sentry](https://sentry.io/signup/)

Par ailleurs, bien que non requis par le pipeline actuel, il est recommandé d'installer Docker-CLI et Heroku-CLI pour pouvoir procèder à certains tests de conteneurisation ou de déploiement.

- [Instructions pour installer Docker CLI](https://docs.docker.com/engine/install/)
- [Instructions pour installer Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)


#### Étapes de configuration du pipeline CI/CD

##### 1. Heroku
Une fois votre compte validé, utilisez le menu `New` / `Create new app` pour créer une nouvelle application de votre choix (s'il contient `oc-lettings`, c'est mieux).

Toutes les autres informations utiles à Heroku lui seront envoyées en même temps que le container par CircleCI.

Les variables suivantes seront utiles pour la configuration de CircleCI :
- **HEROKU_APP_NAME**	*(Le nom de l'application que vous venez de créer)*
- **HEROKU_TOKEN**	*(Utilisez `heroku authorizations:create` de Heroku-CLI)*

##### 2. Docker Hub
Une fois votre compte validé, utilisez le bouton `Create Repository` pour créer un nouveau dépot pour les conteneurs (s'il contient `oc-lettings`, c'est mieux).

Les variables suivantes seront utiles pour la configuration de CircleCI :
- **DOCKER_LOGIN**	*(Votre identifiant Docker-Hub)*
- **DOCKER_PASSWORD**	*(Votre mot de passe Docker-Hub)*
- **PROJECT_REPONAME**	*(Le nom du repo que vous venez de créer)*

##### 3. Sentry
Une fois votre compte validé, utilisez le bouton `Create Project` en haut à droite pour créer votre projet.

La variable suivante sera utile pour la configuration de CircleCI :
- **SENTRY_DSN**	*(Vous pouvez la trouver dans `Settings` / `Projects` / {VOTRE_PROJECT} / `Client Keys (DSN)` / `DSN`)*

##### 4. CircleCI
C'est ici que le plus gros du travail de configuration doit se faire. En effet, une fois connecté à votre compte, allez dans le menu `Projets` puis connectez le repo-github avec lequel vous travaillez à l'aide du bouton `Set Up Project`. Le projet possédant déjà un fichier de configuration dans .circleci/config.yml il va vous être proposé de l'utiliser. Confirmez son utilisation.

Une fois sur la page de gestion de votre projet sur CircleCI, utilisez le bouton `Project Settings` à droite, puis `Environment Variables` à gauche. Placez y les variables suivantes :

- **HEROKU_APP_NAME**

> Le nom de l'application Heroku

- **HEROKU_TOKEN**	

> Utilisez `heroku authorizations:create` de Heroku-CLI

- **DOCKER_LOGIN**	

> Votre identifiant Docker-Hub

- **DOCKER_PASSWORD**

> Votre mot de passe Docker-Hub

- **PROJECT_REPONAME**	

> Le nom du repo sur Docker-Hub

- **SENTRY_DSN**	

> Vous pouvez la trouver sur le site Sentry dans `Settings` / `Projects` / {VOTRE_PROJECT} / `Client Keys (DSN)` / `DSN`

- **DJANGO_SECRET_KEY**

> Vous pouvez la générez avec un suite comme [djecrety](https://djecrety.ir/) ou la générer avec le code ci-dessous

```bash
>>> from django.core.management import utils
>>> print(utils.get_random_secret_key())
```

#### Utiliser le container Docker-Hub en local

Pour utiliser le container envoyé sur Docker-Hub en local il vous faut d'abord mettre en place quelques variables d'énvironnement :

```bash
>>> export SENTRY_DSN={La même chose que pour CircleCI}
>>> export DEBUG=1
```

Puis utiliser la commande suivante pour récupèrer le conteneur et le lancer:

```bash
>>> docker run --pull always -d -e "PORT=8000" -e SENTRY_DSN -e DEBUG -p 80:8000 DOCKER_LOGIN/PROJECT_REPONAME
```

> Vous pouvez essayer avec le repo `valkea/oc-lettings` mais il vous faudra tout de même les variables d'environnement, sinon le conteneur ne se lancera pas...
> `docker run --pull always -d -e "PORT=8000" -e SENTRY_DSN -e DEBUG -p 80:8000 valkea/oc-lettings:latest`

Pour vérifier qu'il fonctionne bien vous pouvez visitez l'url suivante : [http://127.0.0.1](http://127.0.0.1)

Enfin, une fois terminé, recupèrer l'ID du container avec :

```bash
>>> docker ps -a
```

et fermez le avec la commande suivante :

```bash
>>> docker stop {containerID}
>>> docker system prune # pour nettoyer, mais non obligatoire
```

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
