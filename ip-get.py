#!/usr/bin/env python3

import socket
import netifaces
import subprocess
import re
from typing import List, Optional
import platform
import sys
import colorama
from colorama import Fore, Style

class NetworkInfoRetriever:
  def __init__(self):
      colorama.init(autoreset=True)
      self.operating_system = platform.system()

  def check_system(self) -> bool:
      """Check if running on Linux"""
      if self.operating_system != "Linux":
          print(f"{Fore.RED}[ERROR] This script is designed for Linux systems only.")
          print(f"Current OS: {self.operating_system}")
          return False
      return True

  def get_ip_socket(self) -> Optional[str]:
      """Get IP using socket method"""
      try:
          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          # We don't actually connect to Google, just use it as a reference
          s.connect(("8.8.8.8", 80))
          ip = s.getsockname()[0]
          s.close()
          return ip
      except Exception as e:
          print(f"{Fore.YELLOW}[WARNING] Socket method failed: {str(e)}")
          return None

  def get_ip_netifaces(self) -> List[dict]:
      """Get IPs using netifaces method"""
      ips = []
      try:
          interfaces = netifaces.interfaces()

          for interface in interfaces:
              if interface == 'lo':  # Skip loopback
                  continue

              addrs = netifaces.ifaddresses(interface)

              if netifaces.AF_INET in addrs:
                  for addr in addrs[netifaces.AF_INET]:
                      ip_info = {
                          'interface': interface,
                          'ip': addr['addr'],
                          'netmask': addr.get('netmask', 'N/A'),
                          'broadcast': addr.get('broadcast', 'N/A')
                      }
                      ips.append(ip_info)

          return ips
      except Exception as e:
          print(f"{Fore.YELLOW}[WARNING] Netifaces method failed: {str(e)}")
          return []

  def get_ip_ifconfig(self) -> List[str]:
      """Get IPs using ifconfig command"""
      try:
          output = subprocess.check_output(['ifconfig']).decode()
          pattern = r'inet (?:addr:)?(\d+\.\d+\.\d+\.\d+)'
          ips = re.findall(pattern, output)
          return [ip for ip in ips if not ip.startswith('127.')]
      except Exception as e:
          print(f"{Fore.YELLOW}[WARNING] ifconfig method failed: {str(e)}")
          return []

  def get_ip_hostname(self) -> Optional[str]:
      """Get IP using hostname method"""
      try:
          hostname = socket.gethostname()
          return socket.gethostbyname(hostname)
      except Exception as e:
          print(f"{Fore.YELLOW}[WARNING] Hostname method failed: {str(e)}")
          return None

  def display_results(self, socket_ip: Optional[str], netifaces_ips: List[dict], 
                     ifconfig_ips: List[str], hostname_ip: Optional[str]):
      """Display all retrieved IP information"""
      print(f"\n{Fore.GREEN}=== Private IP Address Information ===\n")

      if socket_ip:
          print(f"{Fore.CYAN}Socket Method IP: {Fore.WHITE}{socket_ip}")

      if netifaces_ips:
          print(f"\n{Fore.CYAN}Netifaces Method Details:")
          for ip_info in netifaces_ips:
              print(f"{Fore.WHITE}Interface: {ip_info['interface']}")
              print(f"IP Address: {ip_info['ip']}")
              print(f"Netmask: {ip_info['netmask']}")
              print(f"Broadcast: {ip_info['broadcast']}\n")

      if ifconfig_ips:
          print(f"{Fore.CYAN}Ifconfig Method IPs:")
          for ip in ifconfig_ips:
              print(f"{Fore.WHITE}{ip}")

      if hostname_ip:
          print(f"\n{Fore.CYAN}Hostname Method IP: {Fore.WHITE}{hostname_ip}")

      print(f"\n{Fore.GREEN}================================")

def main():
  try:
      retriever = NetworkInfoRetriever()

      # Check if running on Linux
      if not retriever.check_system():
          sys.exit(1)

      # Get IPs using different methods
      socket_ip = retriever.get_ip_socket()
      netifaces_ips = retriever.get_ip_netifaces()
      ifconfig_ips = retriever.get_ip_ifconfig()
      hostname_ip = retriever.get_ip_hostname()

      # Display results
      retriever.display_results(socket_ip, netifaces_ips, ifconfig_ips, hostname_ip)

  except KeyboardInterrupt:
      print(f"\n{Fore.YELLOW}[INFO] Program terminated by user")
      sys.exit(0)
  except Exception as e:
      print(f"{Fore.RED}[ERROR] An unexpected error occurred: {str(e)}")
      sys.exit(1)

if __name__ == "__main__":
  main()