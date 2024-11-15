import subprocess
import time
import random

def get_current_ip_address(interface_name):
    """
    Returns the current IP address of the specified network interface.
    """
    ip_address = subprocess.check_output(["ip", "addr", "show", "dev", interface_name]).decode()
    return ip_address.split("\n")[2].split(" ")[5]

def generate_new_ip_address():
    """
    Generates a new IP address.
    """
    new_ip_address = "192.168." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    return new_ip_address

def assign_ip_address(interface_name, new_ip_address):
    """
    Assigns the new IP address to the specified network interface.
    """
    subprocess.run(["ip", "addr", "flush", "dev", interface_name])  # Clears the existing IP configuration
    subprocess.run(["ip", "addr", "add", new_ip_address + "/24", "dev", interface_name])  # Assigns the new IP address

def validate_new_ip_address(interface_name, new_ip_address):
    """
    Validates if the new IP address has been successfully assigned.
    """
    ip_address = subprocess.check_output(["ip", "addr", "show", "dev", interface_name]).decode()
    if new_ip_address in ip_address:
        print("New IP address is:", ip_address.split("\n")[2])  # Prints the new IP address
    else:
        print("Failed to assign new IP address.")

# Main program
interface_name = input("Enter the network interface name (e.g. eth0, wlan0): ")
while True:
    current_ip_address = get_current_ip_address(interface_name)  # Get current IP address
    new_ip_address = generate_new_ip_address()  # Generate a new IP address
    assign_ip_address(interface_name, new_ip_address)  # Assign the new IP address
    validate_new_ip_address(interface_name, new_ip_address)  # Validate the new IP address
    time.sleep(600)  # Wait for 10 minutes