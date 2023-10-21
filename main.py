# create a python routine to read devices.json which was created by tinytuya scan and create a list of devices found in that json file
# then loop through the list and turn on each device

import tinytuya
import json

# Read devices file
with open('devices.json') as json_file:
    devices = json.load(json_file)

# Loop through devices
for i, device in enumerate(devices):
    if device['ip'] != '':
        print('ID:', i, 'Device:', device['name'])
        d = tinytuya.Device(device['id'], device['ip'], device['key'])
        d.set_version(3.3)
        print('Dictionary %r' % d.status())
    else:
        print(f"Device {device['name']} does not have an IP address.")
