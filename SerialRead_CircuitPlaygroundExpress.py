import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    line = ser.readline()
    print (line.decode('ascii', errors='replace'), end='')
    time.sleep(1)
