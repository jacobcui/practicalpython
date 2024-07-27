# Network Scanning with Scapy
from scapy.all import sr1, IP, ICMP

# Send an ICMP echo request to a target IP
# Please note that the IP address 192.168.1.1 is imaginative and for demonstration only.
response = sr1(IP(dst="8.8.8.8")/ICMP())
if response:
    print("Host is up")
