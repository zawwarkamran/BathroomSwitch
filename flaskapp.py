from flask import Flask
import requests
import kasa
import json
import asyncio
import time
from automationfuncs import switch_on, switch_off
app = Flask(__name__)

found_devices = asyncio.run(kasa.Discover.discover())
print(found_devices)

@app.route('/a')
def on():
	for k,v in found_devices.items():
		asyncio.run(switch_on(k))
	time.sleep(10)
	return 'switch_on'

@app.route('/b')
def off():
	for k,v in found_devices.items():
		asyncio.run(switch_off(k))
	return 'switch_off'
	

@app.route('/')
def main():
	return 'Running'

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")