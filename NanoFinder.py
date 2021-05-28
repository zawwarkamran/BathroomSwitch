from nanoleafapi import discovery, Nanoleaf 
import time
import requests

nl = Nanoleaf("192.168.2.218")


while True:
	response = requests.get("http://192.168.2.229")
	print(response.content['motion'])
	state = response.content['motion']
	if state == 1:
		nl.power_off()
		print("turning off")
		time.sleep(5)
	else:
		nl.power_on()

