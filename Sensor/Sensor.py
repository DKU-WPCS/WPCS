import serial

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)

while ser:
    print(ser)