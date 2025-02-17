import hid
import time

# Device Vendor ID and Product ID
VID = 0x2C0D
PID = 0x000C

# Setup device
device = hid.device()

prefix='00'
suffix='0000ff22'

statelist = [
    "00ff0000", # blue, bright
    "00ff0002", # blue, dim
    "ff960000", # purple, bright
    "ff960002", # purple, dim
    "ff000001", # off
    "ff003c00", # yellow, bright
    "ff003c02", # yellow, dim
    "ff000001", # off
    "0000c800", # green, bright
    "0000c802", # green, dim
    "ff000001", # off
    "ff000000", # red, bright
    "ff000002", # red, dim
    "ff000001", # off
    "ff000f00", # orange, bright
    "ff000f02", # orange, dim
    "ff000001", # off
]


for state in statelist:
    device.open(VID, PID)
    data = bytes.fromhex(f"{prefix}{state}{suffix}")

    print(data)
    device.write(data)
    time.sleep(0.5)

    # Close the device
    device.close()
