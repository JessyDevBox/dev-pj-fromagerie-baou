from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import des modèles pour les rendre disponibles depuis le package models
from .cheese_milk import CheeseMilk
from .cheese import Cheese
from .discussion import Discussion
from .message import Message
from .milk import Milk
from .paste_type import PasteType
from .platter import Platter
from .platter_cheese import PlatterCheese
from .user import User


# Liste des modèles pour faciliter l'importation
__all__ = [
    "db",
    "CheeseMilk",
    "Cheese",
    "Discussion",
    "Message",
    "Milk",
    "PasteType",
    "Platter",
    "PlatterCheese",
    "User",
]
