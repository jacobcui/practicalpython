from scapy.all import *

def scan_ports(host, ports):
    ans, unans = sr(IP(dst=host)/TCP(sport=RandShort(), dport=ports, flags="S"), timeout=2)
    
    for sent, received in ans:
        if received.haslayer(TCP) and received[TCP].flags == 0x12:  # SYN-ACK
            print(f'Port {received.sport} is open')

# Example usage
scan_ports('192.168.1.1', [21, 22, 80, 443])
