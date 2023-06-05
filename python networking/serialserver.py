import serial
from serial.tools import list_ports
import time
import socket
import sys

def find_arduino():
    known_ports = list_ports.comports() # should give a list of port names
    port_name = ""

    for each_port in known_ports:
        # print("FOUND pid " + str(each_port.pid) + " vid "+ str(each_port.vid))
        # if((each_port.pid == 24597) and (each_port.vid==1027)):
        if each_port.vid== 2341:
            port_name = each_port.name
            break

    if(port_name == ""):
        print("Could not find serial port; ensure Arduino is plugged in")
        exit(1)
    print("found Arduino device at " + port_name)
    return port_name

def main():
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "" # can leave this blank on the server side
    port = int(sys.argv[1])
    s.bind((host, port))

    # accept "call" from client
    s.listen(1)
    conn, addr = s.accept()
    # connect the serial port
    arduino = serial.Serial(port='COM6', baudrate=57600, timeout=0.3)

    # flush the buffer
    arduino.reset_input_buffer()
    arduino.reset_output_buffer()

    while(True):
        # read the byte from the serial port
        x = arduino.read()
        #v = int.from_bytes(x, byteorder='little')

        # print(x)
        conn.send(x)

        time.sleep(0.25)

    arduino.close()

if __name__ == "__main__":
    main()
