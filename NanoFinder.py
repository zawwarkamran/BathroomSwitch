from nanoleafapi import discovery, Nanoleaf 


print(discovery.discover_devices())

nl = Nanoleaf("192.168.2.246")

print(nl.get_power())