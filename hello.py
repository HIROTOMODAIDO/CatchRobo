import serial
import time

# setting serial port
#port = '/dev/ttyUSB0'  # need to change port for connected Arduino by ubuntu
port = 'COM4' #by windows
baud_rate = 9600  # match serial port of Arduino

# open serial port
ser = serial.Serial(port, baud_rate, timeout=1)
time.sleep(2)  # wait for serial connetion stable

try:
    while True:
        # send message Arduino
        ser.write(b'Hello from Jetson\n')
        
        # read responce from Arduino
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').rstrip()
            print("Received from Arduino: " + response)
        
        # wait 1 second
        time.sleep(1)
        
except KeyboardInterrupt:
    # close serial port when program finish
    ser.close()
    print("Serial port closed")
