# LANG - Setting multilang with Babel

### Requirements
flask-babel


### Files
** /babel.cfg
```
[python: app/**.py]
[jinja2: app/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

** /config.py
``` 
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cle-secrete-par-defaut'
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_TRANSLATION_DIRECTORIES = 'app/translations'
```


### Extract and compil tranductions
1. Extraction des chaînes à traduire
```
pybabel extract -F babel.cfg -o app/translations/messages.pot .
```

2. Création des fichiers de traduction (première fois)
```
# Pour le français
pybabel init -i app/translations/messages.pot -d app/translations -l fr

# Pour l'anglais
pybabel init -i app/translations/messages.pot -d app/translations -l en
```

3. Édition des fichiers de traduction
Modifiez les fichiers app/translations/fr/LC_MESSAGES/messages.po et app/translations/en/LC_MESSAGES/messages.po pour ajouter vos traductions.

Exemple pour app/translations/en/LC_MESSAGES/messages.po:

```
msgid "Accueil"
msgstr "Home"

msgid "Bienvenue sur notre site web"
msgstr "Welcome to our website"

msgid "Cette page est disponible en plusieurs langues."
msgstr "This page is available in multiple languages."

msgid "© 2025 Mon Application"
msgstr "© 2025 My Application"
```

4. Compilation des traductions
```
pybabel compile -d app/translations
```

5. Mise à jour des traductions (après modification du code)
```
pybabel extract -F babel.cfg -o app/translations/messages.pot .
pybabel update -i app/translations/messages.pot -d app/translations
```


### Best practicies
Séparation des préoccupations : Utilisez des fichiers de traduction distincts pour chaque langue.

Contexte : Utilisez pgettext pour fournir un contexte aux traductions ambiguës.

Copier
from flask_babel import pgettext
menu_home = pgettext('navigation menu', 'Home')
Pluralisation : Utilisez ngettext pour gérer les pluriels.

Copier
from flask_babel import ngettext
message = ngettext('%(count)d message', '%(count)d messages', count) % {'count': count}
Lazy loading : Utilisez lazy_gettext pour les chaînes dans les formulaires et les modèles.

Copier
from flask_babel import lazy_gettext as _l
class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
Détection automatique de la langue : Implémentez une logique de détection basée sur :

Préférence explicite de l'utilisateur (stockée en session)
En-têtes HTTP Accept-Language
Langue par défaut de l'application
Paramètres régionaux : Utilisez format_datetime, format_currency, etc. pour formater les dates et les nombres selon les conventions locales.

Copier
from flask_babel import format_datetime
formatted_date = format_datetime(datetime.utcnow())
Internationalisation des URLs : Envisagez d'ajouter un préfixe de langue aux URLs pour une meilleure SEO.

Copier
@app.route('/<lang>/about')
def about(lang):
    session['language'] = lang
    return render_template('about.html')
