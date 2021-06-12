from nanoleafapi import discovery, Nanoleaf 
import sched, time
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

async def switch():
	while True:
		time.sleep(0.01)
		response = requests.get("http://192.168.2.229")
		p = kasa.SmartDimmer("192.168.2.233")
		await p.update()
		motion_data = json.loads(response.text)
		state = motion_data['variables']['motion']
		# print(state)
		if state == 1:
			await p.turn_on()
			# print("turning bathroom light on")
			time.sleep(1805)
		else:
			# print('turning off')
			await p.turn_off()

if __name__ == '__main__':
	try:
		asyncio.run(switch())
	except Exception as e:
		print(e)
