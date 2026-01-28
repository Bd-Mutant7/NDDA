 Network Device Discovery Application

## Objective
To design and implement a Python-based application that discovers devices on a local area network using ARP scanning and presents the results in a graphical interface.

## Features
- ARP-based network discovery
- Displays IP address, MAC address, hostname, and vendor
- Graphical User Interface (GUI)
- Export scan results to CSV
- Cross-platform support (Windows, Linux, macOS)

## Technologies Used
- Python
- Scapy
- Tkinter
- PyInstaller

## How It Works
The application sends ARP broadcast requests within a specified subnet. Devices that respond are identified as active hosts. MAC addresses are used to determine vendor information.

## Usage
1. Run the application as Administrator / sudo
2. Click "Scan Network"
3. View discovered devices
4. Export results to CSV if required

## Ethical Considerations
This tool is intended for educational purposes and must only be used on networks where the user has authorization.

## Author
[kariukipeter7]

