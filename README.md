
# Openclassroms Projet 4

Réalisation de logiciel de gestion de tounois d'échecs, dans le terminal.

## Pour commencer

### Pré-requis

- Python 3
- pip

### Installation

Executez la commande ``gcl https://github.com/gdanj/OC_projet_04.git`` pour télécharger le repo git.

Ensuite ouvrer repertoire créé ``cd OC_projet_04``

Créez un environnement virtuel python ``python3 -m venv env``

Activez l'environnement virtuel ``source env/bin/activate``

Intallez les dépendance du programme ``pip install -r requirements.txt``

Votre répertoire ressemblera à ceci :
``ls``

``chess  README.md  requirements.txt  start.py``

## Démarrage

Pour exécuter le programme entrez la commande ``python3 start.py``

## Rapport

Pour créer un rapport flake8 HTML entrez la commande ``python3 -m flake8 --max-line-length 119 --format=html --htmldir=flake-report chess start.py``
