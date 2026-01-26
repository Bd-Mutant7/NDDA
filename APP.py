import scapy.all as scapy
from scapy.layers.inet import IP, ARP, ICMP
from scapy.layers.l2 import Ether
import os
import platform
from datetime import datetime

# Define a function for ARP scanning
def arp_scan(ip_range):
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list

# Define a function for ICMP ping sweep
def icmp_ping_sweep(ip_range):
    ip = IP(dst=ip_range, ttl=20)/ICMP()
    response_list = scapy.srp(ip, timeout=1, verbose=False)[0]
    return response_list

# Define a function to get device information
def get_device_info(ip):
    try:
        # Use scapy to get MAC address
        mac = scapy.srp1(IP(dst=ip)/ARP(), timeout=1, verbose=False).hwsrc
        # Use scapy to get hostname
        hostname = scapy.srp1(IP(dst=ip)/ARP(pdst=ip, op=ARP.who_has), timeout=1, verbose=False).psrc
        return {
            "ip": ip,
            "mac": mac,
            "hostname": hostname
        }
    except:
        return None

# Define a function to scan the network
def scan_network(ip_range):
    devices = []
    # Perform ARP scanning
    answered_list = arp_scan(ip_range)
    for element in answered_list:
        device_info = get_device_info(element[1].psrc)
        if device_info:
            devices.append(device_info)
    # Perform ICMP ping sweep
    response_list = icmp_ping_sweep(ip_range)
    for element in response_list:
        device_info = get_device_info(element[0].dst)
        if device_info and device_info not in devices:
            devices.append(device_info)
    return devices

# Example usage
if __name__ == "__main__":
    ip_range = "192.168.1.0/24"
    devices = scan_network(ip_range)
    for device in devices:
        print(device)
