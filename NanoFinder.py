from nanoleafapi import discovery, Nanoleaf 
import time
import requests
import json
import kasa
import asyncio

nl = Nanoleaf("192.168.2.218")

async def kasafunc():
	p = kasa.SmartDimmer("192.168.2.233")
	await p.update()
	print(p.alias)

	await p.turn_on()

	time.sleep(10)

	await p.turn_off()






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
	asyncio.run(kasafunc())
	# try:
	# 	switch()
	# except Exception as e:
	# 	print(e)
