# exporter.py
import csv


def export_to_csv(devices, filename="network_devices.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "MAC Address", "Hostname", "Vendor"])

        for d in devices:
            writer.writerow([
                d["ip"],
                d["mac"],
                d["hostname"],
                d["vendor"]
            ])
