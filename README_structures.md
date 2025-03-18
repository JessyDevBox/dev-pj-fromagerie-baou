# dev-pj-fromagerie-baou
Projet Formagerie Baou

dev-pj-fromagerie-baou/
├── dev-front/           # Application Nuxt.js
│   ├── assets/          # Ressources statiques (images, styles)
│   ├── components/      # Composants Vue réutilisables
│   ├── layouts/         # Layouts de l'application
│   ├── locales/         # Fichiers de traduction (i18n)
│   ├── pages/           # Pages du site
│   ├── plugins/         # Plugins Nuxt
│   ├── public/          # Fichiers publics
│   ├── store/           # Store Vuex (état global)
│   ├── nuxt.config.js   # Configuration Nuxt
│   └── package.json     # Dépendances frontend
│
└── dev-back/            # Application FastAPI
    ├── app/             # Code source principal
    │   ├── api/         # Points d'API
    │   ├── core/        # Configuration principale
    │   ├── crud/        # Opérations CRUD
    │   ├── db/          # Configuration de la base de données
    │   ├── models/      # Modèles SQLAlchemy
    │   ├── schemas/     # Schémas Pydantic
    │   └── utils/       # Utilitaires
    ├── alembic/         # Migrations de base de données
    ├── main.py          # Point d'entrée de l'application
    └── requirements.txt # Dépendances backend
