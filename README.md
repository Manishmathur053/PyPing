# PyPing
This is a Custom ICMP Ping Tool built using Python and Scapy for network diagnostics.

#What it does
This Project let you Ping an IP and check if its reachable or not by sending packets and recieving them. You can custom add the amount of packets to send and the TTL. 

It uses socket to check if the IP is valid, 

#Reason for building this
This project was built to gain hands-on understanding of networking concepts[ICMP, Packets, etc] while learning Python. Instead of relying on the system ping command, this tool manually constructs and sends ICMP packets to measure network performance.

#Features
Sends ICMP Echo Requests to target host
Measures Round Trip Time (RTT)
Displays Min, Max, and Average RTT
Tracks packet loss (sent, received, lost)
Supports both IP addresses and domain names
Command-line interface using argparse
Customizable packet count and TTL

#Concepts
ICMP protocol basics
TTL (Time-To-Live) behavior
DNS resolution using socket
RTT measurement and timing using perf_counter()
CLI tool design in Python
Packet crafting and network interaction


#How to run

pip install scapy

sudo python ping.py google.com -p 5 -t 64
