# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from scanner import arp_scan
from vendor import lookup_vendor
from exporter import export_to_csv


IP_RANGE = "192.168.1.0/24"


class NetworkScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Device Scanner")
        self.devices = []

        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(
            self.root,
            columns=("IP", "MAC", "Host", "Vendor"),
            show="headings"
        )

        for col in ("IP", "MAC", "Host", "Vendor"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Scan Network", command=self.scan).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Export CSV", command=self.export).pack(side=tk.LEFT, padx=5)

    def scan(self):
        self.tree.delete(*self.tree.get_children())
        self.devices.clear()

        results = arp_scan(IP_RANGE)
        for d in results:
            d["vendor"] = lookup_vendor(d["mac"])
            self.devices.append(d)
            self.tree.insert("", tk.END, values=(
                d["ip"], d["mac"], d["hostname"], d["vendor"]
            ))

    def export(self):
        if not self.devices:
            messagebox.showwarning("Warning", "No devices to export")
            return

        export_to_csv(self.devices)
        messagebox.showinfo("Success", "Exported to network_devices.csv")


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkScannerGUI(root)
    root.mainloop()
