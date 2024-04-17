#!/usr/bin/python3
import board
import busio
from adafruit_ms8607 import MS8607

i2c = busio.I2C(board.SCL, board.SDA)
sensor = MS8607(i2c)
print(".1.3.6.1.4.1.32396.3.3100.11.1")
print("STRING")
print("%.2f" % sensor.temperature)
