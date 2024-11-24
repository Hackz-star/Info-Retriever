Linux Network Info Retriever
Overview
This Python script retrieves and displays private IP address information of a Linux system using multiple methods: socket, netifaces, ifconfig, and hostname. It provides detailed network information such as IP address, netmask, broadcast address, and associated network interfaces.

Whether you're a network administrator or cybersecurity professional, this script is a quick and versatile tool to analyze your system's network configuration.

Features
Socket Method: Retrieves the system's IP address using Python's socket module.
Netifaces Method: Collects detailed information (interface, IP, netmask, and broadcast address) using the netifaces library.
Ifconfig Command: Extracts IP addresses by parsing the output of the ifconfig command.
Hostname Method: Fetches the IP address of the system's hostname using socket.gethostbyname.
Color-Coded Output: Enhances readability using the colorama library.
Linux-Only Design: Built specifically for Linux systems, leveraging platform-specific tools and commands.
