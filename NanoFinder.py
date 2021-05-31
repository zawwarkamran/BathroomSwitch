from nanoleafapi import discovery, Nanoleaf 
import time
import requests
import json
import kasa

nl = Nanoleaf("192.168.2.218")
kasa1 = kasa.SmartDimmer("192.168.2.233")
await kasa1.update()
print(kasa1.alias)
def switch():
	while True:
		time.sleep(0.01)
		response = requests.get("http://192.168.2.229")
		motion_data = json.loads(response.text)
		state = motion_data['variables']['motion']
		print(state)
		if state == 1:
			nl.power_on()
			print("turning off")
			time.sleep(5)
		else:
			nl.power_off()

if __name__ == '__main__':
	print(kasa1.alias)
	kasa1.turn_on()
	time.sleep(5)
	kasa1.turn_off()
	# try:
	# 	switch()
	# except Exception as e:
	# 	print(e)
