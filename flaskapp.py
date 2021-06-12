from flask import Flask
import requests
import kasa
import json
import asyncio
from automationfuncs import switch_on, switch_off
app = Flask(__name__)

found_devices = asyncio.run(kasa.Discover.discover())
print(found_devices)

@app.route('/a')
def home():
	for k,v in found_devices.items():
		asyncio.run(switch_on(k))
	return 'switch'
	

@app.route('/')
def main():
	return 'Running'

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")