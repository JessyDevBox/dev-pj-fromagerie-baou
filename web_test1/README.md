Prérequis

Python 3.x installé sur votre système
Un éditeur de code (VS Code recommandé)
Configuration initiale


# Créer un nouveau dossier pour le projet
mkdir fromagerie-baou
cd fromagerie-baou

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate
# Sur macOS/Linux :
source venv/bin/activate


Installation des dépendances


# Installer les dépendances
pip install -r requirements.txt
Configuration de la base de données


# Initialiser la base de données
flask db init

# Créer la première migration
flask db migrate -m "Initial migration"

# Appliquer la migration
flask db upgrade
Lancer l'application


# Démarrer le serveur de développement
python run.py