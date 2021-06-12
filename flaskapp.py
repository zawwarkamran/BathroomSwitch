from flask import Flask
import kasa
import json
import asyncio
import time
from automationfuncs import switch_on, switch_off
from waitress import serve
import grequests
app = Flask(__name__)
counter = 0

found_devices = asyncio.run(kasa.Discover.discover())
print(found_devices)

@app.route('/a')
def on():
	global counter
	counter += 1
	for k,v in found_devices.items():
		asyncio.run(switch_on(k))
	print('a:{}'.format(counter))
	a = grequests.get('http://192.168.2.228:5000/b')
	grequests.map(a)
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