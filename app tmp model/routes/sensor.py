import random
from flask import Blueprint, jsonify
from app.config import ConfigEnv

bp = Blueprint("sensor", __name__)

if ConfigEnv.is_platform_raspberrypi:
    # Librairie only use on Raspberry Pi OS
    import Adafruit_DHT

    DHT_SENSOR_11 = Adafruit_DHT.DHT11
    DHT_SENSOR_22 = Adafruit_DHT.DHT22
    DHT_PIN_4 = 4  # GPIO pin 4


@bp.route("/")
def index():
    data = {
        "platform": ConfigEnv.platform,
        "humidify": "/sensor/humidity-temperature/<int:garden_id>",
    }
    return jsonify(data)


@bp.route("/humidity-temperature/<int:garden_id>")
def humidityTemperature(garden_id):
    # JCC TODO: check for user <=> garden
    info = ""
    humidity = 0
    temperature = 0
    if ConfigEnv.is_platform_raspberrypi:
        # Librairie only use on Raspberry Pi OS
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_22, DHT_PIN_4)
        info = "Sensor on"
    else:
        info = "Sensor Test mode, generate random numbers"
        humidity = random.randint(50, 100) * 0.987
        temperature = random.randint(18, 30) * 0.987
    data = {
        "gardenId": garden_id,
        "humidity": round(humidity, 1) if humidity else None,
        "temperature": round(temperature, 1) if temperature else None,
        "info": info,
    }
    return jsonify(data)


@bp.route("/capture/<int:garden_id>")
def capture(garden_id):
    # JCC TODO: check for user <=> garden
    info = ""
    data = {
        "gardenId": garden_id,
    }
    return jsonify(data)


"""
@bp.route("/humidity/<int:ident>")
def humidity_type(ident):
    info = ""
    humidity = 0
    temperature = 0
    if not ident in [1, 2]:
        ident = 1

    if ConfigEnv.is_platform_raspberrypi:
        if ident == 1:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_11, DHT_PIN_4)
        else:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_22, DHT_PIN_4)
        info = f"Sensor on - ident: {ident}"
    else:
        info = "Test mode, generate random 30 ~60"
        humidity = random.randint(30, 60)
        temperature = random.randint(30, 60)
    data = {
        "humidity": humidity,
        "temperature": temperature,
        "info": info,
    }
    return jsonify(data)
"""
