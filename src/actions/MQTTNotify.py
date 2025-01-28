import paho.mqtt.client as mqtt

from src.IButton import IButton



class MQTTNotify(IButton):

    BROKER = "192.168.188.208"
    TOPIC = "homeassistant/button/gpio5"
    client = mqtt.Client()
    client.connect(BROKER)

    def on_press(self):
        self.client.publish(self.TOPIC, "pressed")

    def on_release(self) -> None:
        self.client.publish(self.TOPIC, "released")
