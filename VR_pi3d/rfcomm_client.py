from bluetooth import *
import sys

def input_and_send():
    print("type something")
    while True:
        data = input()
        if len(data) == 0:
            break

        sock.send(data)
        sock.send("\n")


def rx_and_echo():
    sock.send("\nsend anything\n")
    while True:
        data = sock.recv(buf_size)
        if data:
            print(data)
            sock.send(data)

addr = "9C:9C:1F:C5:DF:D2"
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

service_match = find_service(address = addr)

buf_size = 1024

if len(service_match) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)
    
for s in range(len(service_match)):
    print("\nservice_matches: [" + str[s] + ']:')
    print(service_match[s])

first_match = service_match[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

port = 1

print("connecting to \"%s\" on %s, port %s" % (name, host, port))

sock = BluetoothSocket(RFCOMM)
sock.connect((host, port))

print("connected")

input_and_send()
#rx_and_echo()s

sock.close()
print("bye")