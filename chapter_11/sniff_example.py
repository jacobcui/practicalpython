import warnings
from scapy.all import *

# Suppress CryptographyDeprecationWarning to avoid cluttering the output
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

def capture_packets(interface, filter):
    """
    Function to capture network packets on a specified interface using a given filter.

    Args:
    interface (str): The network interface to capture packets from (e.g., 'eth0').
    filter (str): The BPF (Berkeley Packet Filter) filter to apply (e.g., 'tcp').

    Returns:
    None
    """
    # Use Scapy's sniff function to capture packets
    # iface: network interface to capture from
    # filter: BPF filter to apply
    # count: number of packets to capture (10 in this case)
    packets = sniff(iface=interface, filter=filter, count=10)

    # Iterate over each captured packet
    for packet in packets:
        # Check if the packet has a TCP layer
        if packet.haslayer(TCP):
            # Print source IP, destination IP, and protocol (TCP)
            print(f'Source: {packet[IP].src}, Destination: {packet[IP].dst}, Protocol: TCP')

# Example usage
# Capture packets on interface 'eth0' with a filter for TCP traffic
capture_packets('eth0', 'tcp')