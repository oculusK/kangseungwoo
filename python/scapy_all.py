import sys
from scapy.all import *

#print(conf.ifaces)

# 패킷 캡쳐를 시작합니다.
# 인터페이스 이름을 실제로 사용하는 네트워크 인터페이스 이름으로 변경하세요.
while True:
    sniff(iface="Software Loopback Interface 1", prn= lambda x : x.show())
    #sniff(prn=lambda x:x.show())