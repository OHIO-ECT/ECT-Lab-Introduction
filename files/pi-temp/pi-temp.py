#!/usr/bin/python3 -u
import board
import busio
import argparse
from adafruit_ms8607 import MS8607


parser = argparse.ArgumentParser()
parser.add_argument('-g', dest='OID');
args = parser.parse_args()
print(args.OID);

i2c = busio.I2C(board.SCL, board.SDA)
sensor = MS8607(i2c)

if args.OID == ".1.3.6.1.4.1.32396.3.3100.10.1":  
	print("STRING")
	print("%.2f" % sensor.temperature)
elif args.OID == ".1.3.6.1.4.1.32396.3.3100.10.2":  
	print("STRING")
	print("%.2f" % sensor.pressure)
elif args.OID == ".1.3.6.1.4.1.32396.3.3100.10.3":  
	print("STRING")
	print("%.2f" % sensor.relative_humidity)
else:
	print("STRING")
	print("11100000")
