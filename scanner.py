# scanner.py
import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether
import socket


def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"


def arp_scan(ip_range):
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered = scapy.srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for _, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "hostname": resolve_hostname(received.psrc)
        })

    return devices
