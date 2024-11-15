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

4. **Run the Project**:
   - Before running the project, make sure **Python** is installed on your system. If Python is not installed, use the following command to install it:
     ```bash
     sudo apt install python3
     ```
   - After navigating to the project directory (`cd ipspoofer`), you can run the `spoof.py` file with the following command:
     ```bash
     sudo python3 spoof.py
     ```

5. **Using the Program**:
   - When the program starts, it will ask you which network interface you want to change the IP address for. The options shown will be:
     ```
     1. eth0
     2. lo
     3. wlan0
     ```
   - After making your selection, the program will **change your IP address every 3 seconds**.

6. **Stopping the Program**:
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

### **GitHub'dan Projeyi Çekme:**

1. **Git'in Yüklü Olduğundan Emin Olun**:
   - Eğer bilgisayarınızda **Git** yüklü değilse, terminali açarak şu komutu kullanarak Git'i yükleyebilirsiniz:
     ```bash
     sudo apt update
     sudo apt install git
     ```
   - Git yüklü değilse, bu komut ile yükleme işlemi yapılacaktır.

2. **GitHub Reposunu Klonlayın**:
   - GitHub'da projeyi barındıran **repo** bağlantısını (URL) alın. Örneğin, proje URL'si şu şekilde olabilir:  
     `https://github.com/tarqof/ipspoofer.git`
   - Terminali açın ve projeyi kaydedeceğiniz dizine gidin. Ardından aşağıdaki komutu kullanarak projeyi **klonlayın**:
     ```bash
     git clone https://github.com/tarqof/ipspoofer.git
     ```
     Bu komut, projeyi belirtilen URL'den bilgisayarınıza indirecek ve bulunduğunuz dizinde bir klasör oluşturacaktır.

3. **Projeye Gitmek**:
   - Proje başarıyla indirildikten sonra, projenin klasörüne gitmek için şu komutu kullanabilirsiniz:
     ```bash
     cd ipspoofer
     ```
     Bu komut, projeyi içeren klasöre geçiş yapmanızı sağlar.

4. **Proje Dosyasını Çalıştırmak**:
   - Proje dosyasına gitmeden önce, bu projeyi çalıştırabilmek için **Python**'ın yüklü olması gerekiyor. Eğer yüklü değilse, şu komut ile yükleyebilirsiniz:
     ```bash
     sudo apt install python3
     ```
   - Projeye gitmek için **cd ipspoofer** komutunu kullandıktan sonra, `spoof.py` dosyasını çalıştırmak için şu komutu kullanın:
     ```bash
     sudo python3 spoof.py
     ```

5. **Programı Kullanmak**:
   - Program başladığında, hangi ağ arayüzü üzerinden IP adresini değiştirmek istediğinizi soracaktır. Ekranda şu seçenekler gösterilecektir:
     ```
     1. eth0
     2. lo
     3. wlan0
     ```
   - Seçiminizi yaptıktan sonra, program **her 3 saniyede bir IP adresinizi değiştirecek** şekilde çalışacaktır.

6. **Programı Durdurmak**:
   - Programı durdurmak için **Ctrl + C** tuşlarına basabilirsiniz. Bu, programın çalışmasını sonlandıracaktır.

### **Özetle:**

1. GitHub'dan projeyi klonlamak için:
   ```bash
   git clone https://github.com/tarqof/ipspoofer.git
   ```

2. Proje dizinine geçmek için:
   ```bash
   cd ipspoofer
   ```

3. Programı çalıştırmak için:
   ```bash
   sudo python3 spoof.py
   ```

Bu adımları izleyerek, GitHub'dan projeyi çekip kullanmaya başlayabilirsiniz.
