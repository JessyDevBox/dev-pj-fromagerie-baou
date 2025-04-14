# Flask Mail - dev-pj-raspizero-tropical-garden
``` 
$ pip install Flask-Mail
``` 

### Tests with gmail
Url: https://mailtrap.io/blog/flask-send-email-gmail/
* We have to rely on "app-specific passwords"
* An app passwod essentially allows us to leverage Gmail SMTP for email sending.
- Log into your Google Account
- Click on 'Security', scroll down to 'How you sign in to Google'
- Active 2-step verification - add phone 699694749
* In search bar, look for 'app password'
https://myaccount.google.com/apppasswords?continue=https://myaccount.google.com/security?gar%3DWzJd%26rapt%3DAEjHL4Mg7FJ9DbUnvyhBR41wIPfVzydrF88s6y3PFvvhXgU8MI-NHJP_2_gy93IPg3wJuusmARGcrjPw3OUHZWPF2m_662yDtmGXxAHHUdUi5ENcqd6oyaQ%26authuser%3D0%26continue%3Dhttps%253A%252F%252Fmyaccount.google.com%252Fsecurity%253Frapt%253DAEjHL4Mg7FJ9DbUnvyhBR41wIPfVzydrF88s6y3PFvvhXgU8MI-NHJP_2_gy93IPg3wJuusmARGcrjPw3OUHZWPF2m_662yDtmGXxAHHUdUi5ENcqd6oyaQ%2526gar%253DWzJd&rapt=AEjHL4MBNVGwALFd_YW86A7ZvSlXFalxxqH5FX7WOmZtNAenXMJWrOEgmZzJ2zQ7eMBX15nHCOqwa2NDUcmiFqEHp9pYicYY6ACBPorJxHOjJVRv3OED4kI

* Name of application: TinyGardenRaspi
- password generated: azkg xtrj lvbs npqk

### Configure flask application for gmail
We can also use port 465, whick was originally intended for SMTPS, if you do decide to use it, you'll have to change the "MAIL_USE_SSL" =true and "MAIL_USE_TLS" =FALSE
``` Exemple of flask_mail script
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Use your actual Gmail address
app.config['MAIL_PASSWORD'] = 'your_app_password'     # Use your generated App Password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def index():
    msg = Message(
        subject='Hello from the other side!', 
        sender='your_email@gmail.com',  # Ensure this matches MAIL_USERNAME
        recipients=['recipient@example.com']  # Replace with actual recipient's email
    )
    msg.body = "Hey, sending you this email from my Flask app, let me know if it works."
    mail.send(msg)
    return "Message sent!"

if __name__ == '__main__':
    app.run(debug=True)
```

``` xxxx
xxxx
```
