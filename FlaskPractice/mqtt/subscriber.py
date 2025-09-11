#subscriber.py                                            
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "myhome/room1/temperature"

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received on {msg.topic}: {msg.payload.decode()}")

# Create MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect & subscribe
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("Listening for sensor data...")
client.loop_forever()