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
            
            # Set the new IP address for the interface
            os.system(f"ifconfig {interface} {random_ip} netmask 255.255.255.0")
            
            print(f"New IP Address: {random_ip} (Interface: {interface})")
            
            # Wait for the specified interval
            time.sleep(interval_ms / 1000.0)
    except KeyboardInterrupt:
        print("\nIP spoofing process stopped.")
        os.system(f"ifconfig {interface} down")
        os.system(f"ifconfig {interface} up")

if __name__ == "__main__":
    display_ascii_art()
    interface = input("Please enter a network interface (e.g., eth0, wlan0): ")
    interval_ms = int(input("Enter the interval for changing the IP address (in milliseconds): "))
    
    spoof_ip(interface, interval_ms)