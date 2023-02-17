#Team members: Caroline Dworken and Tessa Wills
#Github repo: https://github.com/cdworken/lab-04

"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


if __name__ == '__main__':
    #gets computer's IP address
    ip_address = 0 
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)

    while True:
        #replace user with your USC username in all subscriptions
        client.publish("cdworken/ipinfo", f"{ip_address}")
        print("Publishing ip address")
        time.sleep(4)

        #get date and time 
        #get date
        now = datetime.now()
        today_date = now.strftime("%m/%d/%Y")
        
        #get time 
        today_time = now.strftime("%H:%M:%S")
        
        
        #publish date and time in their own topics
        #publish date
        client.publish("cdworken/date", f"{today_date}")
        print("Publishing date")
        time.sleep(4)
        
        #publish time
        client.publish("cdworken/time", f"{today_time}")
        print("Publishing time")
        time.sleep(4)
        
        
        
        
