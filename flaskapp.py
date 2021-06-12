from flask import Flask
import kasa
import json
import asyncio
import time
from automationfuncs import switch_on, switch_off
from waitress import serve
app = Flask(__name__)
counter = 0

found_devices = asyncio.run(kasa.Discover.discover())

@app.route('/a')
def on():
	counter +=  1
	for k,v in found_devices.items():
		asyncio.run(switch_on(k))
	timer()
	return 'switch'

@app.route('/b')
def timer():
	time.sleep(10)
	counter -= 1
	if counter == 0:
		for k,v in found_devices.items():
			asyncio.run(switch_off(k))
	return 'timer'
	

@app.route('/')
def main():
	return 'Running'

if __name__ == '__main__':
	serve(app, host="0.0.0.0", port=5000)