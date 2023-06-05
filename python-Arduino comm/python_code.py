import serial
import time

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    word = input("Enter a Phrase/Word to be Morsified: ")
    value = write_read(word)
    print(value)

