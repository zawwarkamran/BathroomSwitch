from flask import Flask
import requests
import kasa
import asyncio
from automationfuncs import switch_on, switch_off
app = Flask(__name__)

found_devices = asyncio.run(Discover.discover())

@app.route('/')
def home():
	status = requests.get("http://192.168.2.229")
	status = json.loads(status.text)
	state = status['variables']['motion']
	if motion == 1:
		asyncio.run(switch_on())
    return "Hello, World"

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")