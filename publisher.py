import paho.mqtt.client as mqtt
import random
import time

CLIENT_ID = f'kyh-mqtt-{random.randint(0, 1000)}'
USERNAME = 'kyh_jon'
PASSWORD = 'emqx123'
BROKER = 'q1a11171.eu-central-1.emqx.cloud'
PORT = 15552


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to MQTT Broker')
    else:
        print(f'Failed to connect to Broker. Error code {rc}')


def connect_mqtt():
    client = mqtt.Client(CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def init():
    username = input('Username: ')


def main():

    client = connect_mqtt()
    client.loop_start()

    while True:
        message = input('> ')
        client.publish(f'MESSAGE', str(message))


    client.loop_stop()


if __name__ == '__main__':
    main()
