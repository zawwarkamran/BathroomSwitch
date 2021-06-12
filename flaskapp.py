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
	status = requests.get("http://192.168.2.229")
	status = json.loads(status.text)
	state = status['variables']['motion']
	print(state)
	if state == 1:
		for k,v in found_devices.items():
			asyncio.run(switch_on(switch_ip=k))
	else:
		for k,v in found_devices.items():
			asyncio.run(switch_off(switch_ip=k))
	return 'hi'

@app.route('/')
def main():
	return 'Running'

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")