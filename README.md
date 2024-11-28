## **Ip Spoofer**

IP Spoofer Tool was created with **Cybersecurity** and **Anonymity** in mind.


   - Made for **Kali Linux**.

   - You can choose the network interface you want.

   - Your IP address changes every ms time you specify.


---



### **Cloning the Project from GitHub:**

1. **Make Sure Git is Installed**:
   - If **Git** is not installed on your computer, open the terminal and use the following commands to install Git:
     ```bash
     sudo apt update
     sudo apt install git
     ```
   - If Git is not installed, these commands will install it.

2. **Clone the GitHub Repository**:
   - Obtain the **repository URL** from GitHub where the project is hosted. For example, the project URL might look like this:  
     `https://github.com/tarqof/ipspoofer.git`
   - Open the terminal and navigate to the directory where you want to store the project. Then, use the following command to **clone** the project:
     ```bash
     git clone https://github.com/tarqof/ipspoofer.git
     ```
     This command will download the project from the provided URL and create a folder in your current directory with the project files.

3. **Navigate to the Project Folder**:
   - After successfully cloning the project, navigate to the project folder using the following command:
     ```bash
     cd ipspoofer
     ```
     This command will take you into the project directory.

4. **Installing Required Modules**:
   - We will use the **reqs.txt** file to load the required modules.
     ```bash
     pip install -r reqs.txt
     ```
5. **Run the Project**:
   - Before running the project, make sure **Python** is installed on your system. If Python is not installed, use the following command to install it:
     ```bash
     sudo apt install python3
     ```
   - After navigating to the project directory (`cd ipspoofer`), you can run the `spoof.py` file with the following command:
     ```bash
     sudo python3 spoof.py
     ```

6. **Using the Program**:
   - When the program starts, it will ask you which network interface you want to change the IP address for. The options shown will be:
     ```
     1. eth0
     2. lo
     3. wlan0
     ```
   - After making your selection, the program will **change your IP address every 3 seconds**.

7. **Stopping the Program**:
   - To stop the program, press **Ctrl + C**. This will terminate the program and return you to the terminal.


### **Summary:**

1. Clone the project from GitHub:
   ```bash
   git clone https://github.com/tarqof/ipspoofer.git
   ```

2. Navigate to the project folder:
   ```bash
   cd ipspoofer
   ```

3. Run the program:
   ```bash
   sudo python3 spoof.py
   ```

By following these steps, you can easily clone the project from GitHub and start using it.

---