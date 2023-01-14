from scapy.all import*
from PyQt5.QtCore import *
from scapy.layers.inet import IP, TCP

def showPacket(packet):
    # IP
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    proto = packet[IP].proto
    ttl = packet[IP].ttl
    length = packet[IP].len

    if proto == 6:
        sport = packet[TCP].sport
        dport = packet[TCP].dport
        seq = packet[TCP].dport
        ack = packet[TCP].ack
        flag = packet[TCP].flags
        payload = packet[TCP].payload


        print("src: %s -> dst: %s" % (src_ip, dst_ip))
        print("TTL: %s Length: %s" % (ttl, length))
        print("sport: %s dport: %s" % (sport, dport))
        print("seq: %s ack: %s flag: %s" % (seq, ack, flag))
        print("payload : %s" %(payload))
        print("\n")
    # if packet.getlayer("Raw"):
    #     # TODO : Raw data만 저장 안됨
    #     print(packet.show())
    #     rawV = packet.getlayer("TCP").payload.original
    #     print(type(rawV))
    #     rawV = str(rawV, "utf-8")
    # # a = packet.show()
    # # print(a)

#TODO :Snipping동작은 스레드로 돌리도록 수정 -> 중간에 중지시 꺼짐
def sniffing(filter, cnt):
    print(cnt)
    t = AsyncSniffer(filter=filter, prn=showPacket, count=cnt)
    if cnt == 0:
        t.start()
    else:
        t.stop()
    #sniff(filter=filter, prn=showPacket, count=cnt)

class SnippingWorker(QThread):
    def __init__(self):
        super().__init__()
        self.filter = ''

    def run(self):
        self.filter = 'tcp port 80'
        sniffing(self.filter, 0)

    def pause(self):
        self.filter = 'tcp port 80'
        sniffing(self.filter, 1)