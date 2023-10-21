import tinytuya

# Connect to device
d = tinytuya.BulbDevice('eb82c96b0d5fcb7022wvc0', '192.168.1.135', 'w~-<J~=yvazNw6&7')

# Set the version of the device (important for encryption)
d.set_version(3.3)

# Print status of device
print('Dictionary %r' % d.status())

d.turn_on()

d.set_colour(153, 89, 47, True)

print('Dictionary %r' % d.status())