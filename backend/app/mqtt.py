import os
import paho.mqtt.publish as publish
from dotenv import load_dotenv

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "10.0.0.213")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")


def publish_bulb_state(bulb_id: int, state: bool):
    topic = f"hariom/iot/bulbs/{bulb_id}/set"
    payload = "ON" if state else "OFF"

    publish.single(
        topic,
        payload,
        hostname=MQTT_HOST,
        port=MQTT_PORT,
        auth={
            "username": MQTT_USERNAME,
            "password": MQTT_PASSWORD
        }
    )