import hid
import random
import time

# Device Vendor ID and Product ID
VID = 0x2C0D
PID = 0x000C

# Setup device
device = hid.device()

def set_color(color, brightness, delay=.9):
    prefix='00'
    suffix='0000ff22'

    device.open(VID, PID)
    data = bytes.fromhex(f"{prefix}{color}{brightness}{suffix}")

    result = device.write(data)

    # Close the device
    device.close()
    time.sleep(delay)
    return color

def rainbow_loop():
    while True:
        set_color(color='ff0000', brightness='00') # Red
        set_color(color='ff000f', brightness='00') # Orange
        set_color(color='900030', brightness='00') # Yello
        set_color(color='0000c8', brightness='00') # Green
        set_color(color='009000', brightness='00') # Blue
        set_color(color='001100', brightness='00') # Indigo
        set_color(color='ff9600', brightness='02') # Violet (purple)

rainbow_loop()
