import time
import requests
import json
import kasa
import asyncio

async def switch_on(switch_ip):
	dimmer = kasa.SmartDimmer(switch_ip)
	await dimmer.update()
	await dimmer.turn_on()

async def switch_off(switch_ip):
	dimmer = kasa.SmartDimmer(switch_ip)
	await dimmer.update()
	await dimmer.turn_off()