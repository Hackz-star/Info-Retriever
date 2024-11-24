

# Linux Network Info Retriever  

## Overview  
This Python script retrieves and displays private IP address information of a Linux system using multiple methods: **socket**, **netifaces**, **ifconfig**, and **hostname**. It provides detailed network information such as IP address, netmask, broadcast address, and associated network interfaces.  

Whether you're a network administrator or cybersecurity professional, this script is a quick and versatile tool to analyze your system's network configuration.  

---

## Features  
- **Socket Method**: Retrieves the system's IP address using Python's `socket` module.  
- **Netifaces Method**: Collects detailed information (interface, IP, netmask, and broadcast address) using the `netifaces` library.  
- **Ifconfig Command**: Extracts IP addresses by parsing the output of the `ifconfig` command.  
- **Hostname Method**: Fetches the IP address of the system's hostname using `socket.gethostbyname`.  
- **Color-Coded Output**: Enhances readability using the `colorama` library.  
- **Linux-Only Design**: Built specifically for Linux systems, leveraging platform-specific tools and commands.  

---

## Prerequisites  
1. Ensure your system runs **Linux**.  
2. Install the required Python libraries:  
   ```bash
   pip install netifaces colorama
   ```  

---

## How to Use  

### Clone the Repository  
```bash
git clone https://github.com/yourusername/linux-network-info-retriever.git
cd linux-network-info-retriever
```  

### Run the Script  
Make the script executable (optional):  
```bash
chmod +x network_info_retriever.py
```  

Run the script directly:  
```bash
./network_info_retriever.py
```  
Or, run it with Python:  
```bash
python3 network_info_retriever.py
```  

---

## Output Information  
The script will display:  
- **Socket Method IP**: IP address detected via `socket`.  
- **Netifaces Details**: Network interfaces with IP, netmask, and broadcast address.  
- **Ifconfig Method IPs**: IPs parsed from the `ifconfig` command.  
- **Hostname Method IP**: IP address resolved from the system's hostname.  

### Example Output:  
```
=== Private IP Address Information ===

Socket Method IP: 192.168.1.10

Netifaces Method Details:
Interface: eth0
IP Address: 192.168.1.10
Netmask: 255.255.255.0
Broadcast: 192.168.1.255

Ifconfig Method IPs:
192.168.1.10

Hostname Method IP: 192.168.1.10
================================
```

---

## Notes  
- This script is **Linux-specific** and will not work on other operating systems.  
- Some methods (like `ifconfig`) require tools to be installed and accessible in your environment.  

---

## Contributing  
Contributions are welcome! If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.  

---

## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

--- 

Let me know if you want to refine anything further!
