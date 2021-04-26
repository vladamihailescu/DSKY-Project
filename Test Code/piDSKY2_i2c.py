###################################################################################################
# Stuff related to control of the lamp board via PIGPIO and I2C on the Pi's GPIO  (Vlad Mihailescu)
import smbus
# Initialize the PIGPIO API.
DEVICE_BUS = 1
DEVICE_ADDR = 0x11
bus = smbus.SMBus(DEVICE_BUS)

def StringToBytes(val):
    retVal = []
    for c in val:
        retVal.append(ord(c))
    return retVal

# Writes to a register of the LED driver chip via the I2C bus.  The
def writeI2cByte(value):
    byteVal = StringToBytes(value)
    bus.write_i2c_block_data(DEVICE_ADDR,0x00,byteVal)
    return -1

while True:
	try:
		writeI2cByte("325476B89ACE")
	except OSError:
		print("error...")
		pass