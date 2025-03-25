from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import des modèles pour les rendre disponibles depuis le package models
from .user import User
from .cheese import Cheese
from .platter import Platter
from .platter_cheese import PlatterCheese
from .message import Message
from .discussion import Discussion
from .discussion_message import DiscussionMessage

# Liste des modèles pour faciliter l'importation
__all__ = [
    'db',
    'User',
    'Cheese',
    'Platter',
    'PlatterCheese',
    'Message',
    'Discussion',
    'DiscussionMessage'
]
