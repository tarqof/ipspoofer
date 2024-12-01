from scapy.all import *
import os
import time
import random

def display_ascii_art():
    # Green text color using ANSI escape code
    green_color = "\033[92m"
    reset_color = "\033[0m"
    ascii_art = r"""
 ___  ________        ________  ________  ________  ________  ________ _______   ________     
|\  \|\   __  \      |\   ____\|\   __  \|\   __  \|\   __  \|\  _____\\  ___ \ |\   __  \    
\ \  \ \  \|\  \     \ \  \___|\ \  \|\  \ \  \|\  \ \  \|\  \ \  \__/\ \   __/|\ \  \|\  \   
 \ \  \ \   ____\     \ \_____  \ \   ____\ \  \\\  \ \  \\\  \ \   __\\ \  \_|/_\ \   _  _\  
  \ \  \ \  \___|      \|____|\  \ \  \___|\ \  \\\  \ \  \\\  \ \  \_| \ \  \_|\ \ \  \\  \| 
   \ \__\ \__\           ____\_\  \ \__\    \ \_______\ \_______\ \__\   \ \_______\ \__\\ _\ 
    \|__|\|__|          |\_________\|__|     \|_______|\|_______|\|__|    \|_______|\|__|\|__|  
                        \|_________|                                                          
                                                                                              
                                                                                              

Maded by Tarqof: https://github.com/tarqof
    """
    print(f"{green_color}{ascii_art}{reset_color}")

def spoof_ip(interface, interval_ms):
    """
    Spoofs the IP address on the specified network interface at defined intervals.

    Args:
        interface (str): The network interface (e.g., eth0, wlan0, wlan1).
        interval_ms (int): The interval in milliseconds to change the IP address.
    """
    try:
        while True:
            # Generate a random IP address
            random_ip = f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"
            
            # Set the new IP address for the interface using 'ip' command instead of 'ifconfig'
            os.system(f"ip addr flush dev {interface}")
            os.system(f"ip addr add {random_ip}/24 dev {interface}")
            
            # Bring the interface up (in case it was down)
            os.system(f"ip link set {interface} up")
            
            # Set the default gateway and DNS (example: CloudFlare's public DNS)
            os.system(f"ip route add default via 192.168.1.1 dev {interface}")
            os.system("echo 'nameserver 1.1.1.1' > /etc/resolv.conf")
            os.system("echo 'nameserver 1.0.0.1' >> /etc/resolv.conf")
            
            print(f"New IP Address: {random_ip} (Interface: {interface})")
            
            # Wait for the specified interval
            time.sleep(interval_ms / 1000.0)
    except KeyboardInterrupt:
        print("\nIP spoofing process stopped.")
        os.system(f"ip link set {interface} down")
        os.system(f"ip link set {interface} up")

if __name__ == "__main__":
    display_ascii_art()
    interface = input("Please enter a network interface (e.g., eth0, wlan0): ")
    interval_ms = int(input("Enter the interval for changing the IP address (in milliseconds): "))
    
    spoof_ip(interface, interval_ms)