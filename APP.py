import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether
import socket
from datetime import datetime


def arp_scan(ip_range):
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered = scapy.srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in answered:
        hostname = resolve_hostname(received.psrc)
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "hostname": hostname
        })

    return devices


def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"


def scan_network(ip_range):
    print(f"[+] Scanning network {ip_range} at {datetime.now()}")
    return arp_scan(ip_range)


if __name__ == "__main__":
    TARGET_RANGE = "192.168.1.0/24"
    results = scan_network(TARGET_RANGE)

    print("\nDiscovered Devices:")
    print("-" * 50)
    for device in results:
        print(f"IP: {device['ip']}")
        print(f"MAC: {device['mac']}")
        print(f"Host: {device['hostname']}")
        print("-" * 50)
