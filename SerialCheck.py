import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for port in ports:
    print(f"Device: {port.device}, Description: {port.description}")
