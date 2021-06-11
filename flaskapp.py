from flask import Flask
import requests
import kasa
import asyncio
# from automationfuncs import switch_on, switch_off
app = Flask(__name__)

found_devices = asyncio.run(kasa.Discover.discover())
print(found_devices)


@app.route('/')
def home():
	status = requests.get("http://192.168.2.229")
	status = json.loads(status.text)
	state = status['variables']['motion']
	print(state)
	if motion == 1:
		for k,v in found_devices.items():
			asyncio.run(switch_on(k))
	else:
		for k,v in found_devices.items():
			asyncio.run(switch_off())

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")