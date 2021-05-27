from nanoleafapi import discovery, Nanoleaf 
import time


nl = Nanoleaf("192.168.2.218")

nl.power_off()
time.sleep(5)
nl.power_on()