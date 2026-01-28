# vendor.py

OUI_DATABASE = {
    "00:1A:2B": "Cisco Systems",
    "44:38:39": "TP-Link",
    "FC:FB:FB": "Apple",
    "3C:5A:B4": "Google",
}


def lookup_vendor(mac):
    prefix = mac.upper()[0:8]
    return OUI_DATABASE.get(prefix, "Unknown Vendor")
