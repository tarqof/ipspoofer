import os
import time
import random
import subprocess

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


def clear_terminal():
    """
    Clears the terminal screen.
    """
    os.system('clear' if os.name != 'nt' else 'cls')

def get_ip(interface):
    """
    Gets the IP address of the specified network interface.
    """
    result = subprocess.run(['ip', 'addr', 'show', interface], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    
    # Scanning the output to find the IP address.
    for line in output.splitlines():
        if 'inet ' in line:  # 'inet' part represents the IP address.
            return line.strip().split(' ')[1].split('/')[0]
    return None

def set_dns():
    """
    Sets the DNS settings to 1.1.1.1 and 1.0.0.1.
    """
    try:
        # Open the /etc/resolv.conf file and update DNS settings.
        with open('/etc/resolv.conf', 'w') as f:
            f.write("nameserver 1.1.1.1\n")
            f.write("nameserver 1.0.0.1\n")
        print("DNS settings updated successfully.")
    except Exception as e:
        print(f"Error updating DNS settings: {e}")

def set_gateway(interface):
    """
    Sets the default gateway.
    """
    try:
        # Set the default gateway to 192.168.1.1. You can change it if needed.
        subprocess.run(['sudo', 'ip', 'route', 'add', 'default', 'via', '192.168.1.1', 'dev', interface], check=True)
        print(f"Gateway set for {interface}.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting gateway: {e}")

def change_ip(interface):
    """
    Generates a random IP address and changes it using the 'ip' command.
    """
    # Generate a random IP address.
    new_ip = '.'.join(str(random.randint(1, 254)) for _ in range(4))
    
    # If 'lo' interface is selected, we can assign the loopback address.
    if interface == 'lo':
        new_ip = '127.0.0.1'
    
    try:
        # Flush the current IP address assigned to the network interface.
        subprocess.run(['sudo', 'ip', 'addr', 'flush', 'dev', interface], check=True)
        
        # Assign the new IP address.
        subprocess.run(['sudo', 'ip', 'addr', 'add', f'{new_ip}/24', 'dev', interface], check=True)
        
        print(f"New IP address for {interface}: {new_ip}")
    except subprocess.CalledProcessError as e:
        print(f"Error while changing IP: {e}")

def list_active_interfaces():
    """
    Lists all active network interfaces.
    """
    result = subprocess.run(['ip', 'link', 'show'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    
    # Extract the interface names (lines containing 'state').
    interfaces = []
    for line in output.splitlines():
        if 'state' in line:
            interface_name = line.split(':')[1].strip().split(' ')[0]
            interfaces.append(interface_name)
    
    return interfaces

def main():
    clear_terminal()  # Clear the terminal screen at the start.
    
    # Get list of active interfaces.
    active_interfaces = list_active_interfaces()
    
    if not active_interfaces:
        print("No active network interfaces found.")
        return
    
    print("Available network interfaces:")
    for i, interface in enumerate(active_interfaces, 1):
        print(f"{i}. {interface}")
    
    # Let the user select an interface by typing its name.
    selected_interface = input("Enter the network interface: ").strip()

    # Verify if the interface exists in the list of active interfaces.
    if selected_interface not in active_interfaces:
        print(f"Invalid interface: {selected_interface}")
        return

    # Display the current IP address initially.
    current_ip = get_ip(selected_interface)
    print(f"Current IP address for {selected_interface}: {current_ip}")

    # Set DNS settings.
    set_dns()

    # Set default gateway.
    set_gateway(selected_interface)

    # Change IP every 3 seconds.
    try:
        while True:
            change_ip(selected_interface)  # Change the IP address.
            time.sleep(3)  # Wait for 3 seconds.
    except KeyboardInterrupt:
        print("Program terminated.")  # If the program is stopped.

if __name__ == "__main__":
    main()  # Start the program.