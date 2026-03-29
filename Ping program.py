import scapy.all as scapy

ip = "www.google.com"

packet = scapy.IP(dst=ip) / scapy.ICMP() / "hello"


response = scapy.sr1(packet, timeout=2)

if response:
    print("Host is reachable")
    print(response.show)

else:
    print("No response")
