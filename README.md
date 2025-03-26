# dev-pj-fromagerie-baou
```
/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── data/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── garden.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── gardens.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py
│   └── templates/
│       ├── base.html
│       ├── welcome.html
│       └── garden.html
│       └── auth/
│           ├── login.html
│           └── register.html
├── requirements.txt
└── run.py
```

``` Windows install specific Python version like 3.11.2
- Installation folder: C:\Users\jessy\AppData\Local\Programs\Python\Python311\
$ C:\Users\jessy\AppData\Local\Programs\Python\Python311\python.exe -m venv .venv

- For os current Python version
$ python -m venv venv

```

```
$ source venv/bin/activate  # Sur Unix
# ou
$ venv\Scripts\activate  # Sur Windows
```

```
$ pip install -r requirements.txt
```

```
$ flask db init
$ flask db migrate -m "Initial migration"
$ flask db upgrade
```

``` See list of configured routes
$ flask routes
```

```
$ python run.py
```
