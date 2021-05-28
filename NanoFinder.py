from nanoleafapi import discovery, Nanoleaf 
import time
import requests

nl = Nanoleaf("192.168.2.218")
def switch():

	response = requests.get("http://192.168.2.229")
	print(response.content['motion'])
	state = response.content['motion']
	if state == 1:
		nl.power_off()
		print("turning off")
		time.sleep(5)
	else:
		nl.power_on()

if __name__ == '__main__':
	try:
		while True:
			switch()
	except:
		print("error")