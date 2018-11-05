import mysql.connector
import serial
import time

mydb = mysql.connector.connect(
    host="192.168.0.16",
    user="root",
    passwd="root",
    database="temperature"
)
ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    line = ser.readline()
    print(line.decode('ascii', errors='replace'), end='')

    mycursor = mydb.cursor()

    sql = "INSERT INTO temperatureData (temperature_data) VALUES (" + \
        line.decode('ascii', errors='replace')+")"
    mycursor.execute(sql)

    mydb.commit()
    time.sleep(1)
