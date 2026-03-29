import scapy.all as scapy
import time as time
import argparse as argparse


def ping(ip, totalpacket):

    TTL = 64
    sent = 0
    recieve = 0
    lost = 0
    rttslist = []

    for seq in range(1, totalpacket + 1):

        packet = scapy.IP(dst=ip, ttl=TTL) / scapy.ICMP() / "hello"
        time.sleep(1)
        start = time.time()
        response = scapy.sr1(packet, timeout=2, verbose=0)
        end = time.time()

        sent += 1

        if response:
            ms = int((end - start) * 1000)
            ttl = response.ttl
            print(f"Reply from {ip}: seq={seq}, TTL={ttl}, time={ms}ms")
            rttslist.append(ms)
            recieve += 1

        else:
            print("Request timed out")
            lost += 1

    if rttslist:

        avg = sum(rttslist) / len(rttslist)
        min_rtt = min(rttslist)
        max_rtt = max(rttslist)
    else:
        avg = min_rtt = max_rtt = 0

    print("---Ping statistics---")
    print(f"Packet: Sent={sent}, Recieve={recieve}, Lost={lost}")
    print(f"RTT: Min={min_rtt}ms, Max={max_rtt}ms, Avg={avg}ms")


parser = argparse.ArgumentParser(description="IP address and total packets")
parser.add_argument("ip", help="Add IP Address to ping")
parser.add_argument("totalpacket", help="Number of packets to send")


args = parser.parse_args()

ip = args.ip
totalpacket = int(args.totalpacket)

ping(ip, totalpacket)
