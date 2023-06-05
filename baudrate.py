import time
import serial
import string

def is_readable(s):
    return all(c in string.printable for c in s)

def detect_baudrate(port):
    baudrates = [115200, 57600, 38400, 19200, 9600]
    for br in baudrates:
        try:
            ser = serial.Serial(port, br, timeout=1)
            time.sleep(2)  
            print(f"[!] Starting baudrate detection on {port} at {br}, turn on your serial device now.\n")
            for i in range(10):
                if ser.inWaiting():
                    data = ser.readline().decode('utf-8', 'ignore')
                    if data and is_readable(data):
                        print("[-] Detected baudrate: ", br)
                        return br
                    elif data:
                        print(f"[X] Received non-readable data at {br}.")
                        break
                else:
                    print(f"[X] No data received at {br}.")
                    break
            ser.close()
        except serial.SerialException as e:
            print(f"[X] Error occurred: {e}")
    print("[X] Baudrate detection failed.")
    return None

port = "/dev/ttyUSB0"
baudrate = detect_baudrate(port)
if baudrate:
    print(f"[-] Proceed with baudrate {baudrate}")
else:
    print("[X] Cannot detect baudrate. Check your device or try again.")
