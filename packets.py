from scapy.all import IP, send

SRC = "192.168.0.1"
DST = "192.168.0.1"

packet = IP(ttl=64, src=SRC, dst=DST)

print(packet)
send(packet)

