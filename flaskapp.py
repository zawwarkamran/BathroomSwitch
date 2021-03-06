from flask import Flask
import kasa
import json
import asyncio
import time, sched
from automationfuncs import switch_on, switch_off
from waitress import serve
import grequests
app = Flask(__name__)
counter = 0
s = sched.scheduler(time.time, time.sleep)

found_devices = asyncio.run(kasa.Discover.discover())

@app.route('/a')
def on():
	global counter
	counter += 1
	global s
	for k,v in found_devices.items():
		asyncio.run(switch_on(k))
	if s.empty():
		for k,v in found_devices.items():
			s.enter(10, 1, action = await switch_off, kwargs={'switch_ip': k} )
			s.run()
	print(s.queue)
	print('a:{}'.format(counter))
	return 'on'

@app.route('/b')
def timer():
	time.sleep(6)
	global counter
	counter -= 1
	print('b:{}'.format(counter))
	if counter == 0:
		for k,v in found_devices.items():
			asyncio.run(switch_off(k))
	return 'timer'
	
@app.route('/')
def main():
	if counter == 0:
		return 'light_off'
	else:
		return 'light_on'

if __name__ == '__main__':
	serve(app, host="0.0.0.0", port=5000)
	# app.run(host='0.0.0.0', port=5000,debug=True)