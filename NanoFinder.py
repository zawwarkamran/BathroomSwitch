from nanoleafapi import discovery, Nanoleaf 
import time
import requests

response = requests.get("http://192.168.2.229")
print(response.content)
nl = Nanoleaf("192.168.2.218")

nl.power_off()
time.sleep(5)
nl.power_on()