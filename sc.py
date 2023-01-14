#!/usr/bin/python  
from scapy.all import *

def showPacket(packet):
    a = packet.show()
    print(a)


def sniffing(filter):
    sniff(filter=filter, prn=showPacket, count=0)


if __name__ == '__main__':
    filter = 'tcp port 80'
    sniffing(filter)  