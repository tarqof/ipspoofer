import os
import time
import random
import subprocess

def get_ip(interface):
    """
    Belirtilen ağ arayüzü için IP adresini alır. 
    (Gets the IP address of the specified network interface.)
    """
    result = subprocess.run(['ip', 'addr', 'show', interface], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    
    # IP adresini bulmak için çıktıyı tarıyoruz. (We scan the output to find the IP address.)
    for line in output.splitlines():
        if 'inet ' in line:  # 'inet' ifadesi IP adresini temsil eder. (The 'inet' part represents the IP address.)
            return line.strip().split(' ')[1].split('/')[0]
    return None

def change_ip(interface):
    """
    IP adresini değiştirmek için random bir IP adresi oluşturur ve ifconfig komutuyla değiştirir. 
    (Generates a random IP address and changes it using the 'ip' command.)
    """
    # Random bir IP adresi oluşturuyoruz (We generate a random IP address).
    new_ip = '.'.join(str(random.randint(1, 254)) for _ in range(4))
    
    # Eğer 'lo' arayüzü seçildiyse, loopback adresi atanabilir (If the 'lo' interface is selected, we can assign the loopback address).
    if interface == 'lo':
        new_ip = '127.0.0.1'
    
    try:
        # Ağ arayüzüne atanmış mevcut IP adresini temizliyoruz (We flush the existing IP address assigned to the interface).
        subprocess.run(['sudo', 'ip', 'addr', 'flush', 'dev', interface], check=True)
        
        # Yeni IP adresini atıyoruz (We assign the new IP address).
        subprocess.run(['sudo', 'ip', 'addr', 'add', f'{new_ip}/24', 'dev', interface], check=True)
        
        print(f"{interface} arayüzü için yeni IP adresi: {new_ip}")  # Yeni IP'yi ekrana yazdırıyoruz. (Print the new IP address for the interface.)
    except subprocess.CalledProcessError as e:
        print(f"IP değiştirilirken hata oluştu (Error while changing IP): {e}")  # Hata mesajı (Error message)

def main():
    print("IP adresini değiştirmek için bir ağ arayüzü seçin (Select a network interface to change the IP address):")  # Kullanıcıdan ağ arayüzü seçmesi istenir. (Prompt user to select a network interface.)
    print("1. eth0")
    print("2. lo")
    print("3. wlan0")
    
    choice = input("Seçiminizi yapın (Enter your choice) {1/2/3}: ")  # Kullanıcıdan giriş alınır (User input is taken).

    interface_mapping = {
        '1': 'eth0',  # eth0 ağ arayüzü (eth0 network interface)
        '2': 'lo',    # loopback arayüzü (loopback interface)
        '3': 'wlan0'  # wlan0 kablosuz ağ arayüzü (wlan0 wireless interface)
    }
    
    if choice not in interface_mapping:
        print("Geçersiz seçim (Invalid choice)!")  # Kullanıcı geçersiz seçim yaptıysa hata mesajı (Invalid selection message)
        return

    selected_interface = interface_mapping[choice]  # Kullanıcının seçtiği ağ arayüzünü alıyoruz (Get the selected network interface).

    # Başlangıçta mevcut IP adresini göster (Display the current IP address initially).
    current_ip = get_ip(selected_interface)
    print(f"Başlangıç IP adresi (Current IP address for) ({selected_interface}): {current_ip}")  # Mevcut IP adresini ekrana yazdırıyoruz (Print current IP address to screen).

    # IP'yi her 3 saniyede bir değiştir (Change IP every 3 seconds).
    try:
        while True:
            change_ip(selected_interface)  # IP'yi değiştiriyoruz (Change the IP address).
            time.sleep(3)  # 3 saniye bekliyoruz (Wait for 3 seconds).
    except KeyboardInterrupt:
        print("Program sonlandırıldı (Program terminated).")  # Program durdurulursa (If the program is stopped).

if __name__ == "__main__":
    main()  # Programı başlat (Start the program).