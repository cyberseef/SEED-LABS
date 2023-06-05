#!/usr/bin/env python3
from scapy.all import *
E = Ether()
A = ARP()
A.op = 1 # 1 for ARP request; 2 for ARP reply
pkt = E/A
sendp(pkt)
