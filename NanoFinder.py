from nanoleafapi import discovery, Nanoleaf 
import time
import requests
import json

nl = Nanoleaf("192.168.2.218")

def switch():
	while True:
		response = requests.get("http://192.168.2.229")
		motion_data = json.loads(response.text)
		state = motion_data['variables']['motion']
		if state == 1:
			nl.power_on()
			print("turning off")
			time.sleep(5)
		else:
			nl.power_off()

if __name__ == '__main__':
	while True:
		try:
			switch()
		except:
			print("Error")
