import time
import requests
import json
import kasa
import asyncio

async def switch_on(switch_ip):
	dimmer = kasa.SmartDimmer(switch_ip)
	await asyncio.coroutine(dimmer.update)()
	await asyncio.coroutine(dimmer.turn_on)()

async def switch_off(switch_ip):
	dimmer = kasa.SmartDimmer(switch_ip)
	await asyncio.coroutine(dimmer.update)()
	await asyncio.coroutine(dimmer.turn_off)()