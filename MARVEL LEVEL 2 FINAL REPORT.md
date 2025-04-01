
### <u>TASK 1: CI/CD (Continuous Integration & Continuous Delivery) - Intro to Jenkins</u>

What did I learn?
- In this task I basically learned about what CI/CD is and learnt how it is useful in practical industry level development
- CI/CD is nothing but a working model which helps in increasing the speed of development and reduces bugs and fault in code
- I learn about different models that have been in the history of industry such as the **Waterfall model** which was the oldest model of development used in the 90's, then came the **Agile model** which was used in the early 2000's, but finally in the late 2000's a new model was adopted called as **DevOps model** here the Developers and Operations team work together and complete a feedback loop which helps in faster development and more reliable code
- So to speak about this in detail, CI/CD and DevOps are closely related, CI is continuous integration and CD is continuous development. CI is basically continuosly uploading to a repo and CD is basically deploying the code
- DevOps is basically using CI/CD and breaking down the project into smaller projects and working on them
- ![[Screenshot 2025-03-24 182846.png]]
- Now to setup the DevOps model we have a helper, this helper is called as **Jenkins**
- So Jenkins is nothing but an automating software that helps in CI/CD we have to basically script a code in **GROOVY** language and then we are done, Jenkins automatically detects new code we write , pulls it from the repo, tests it and then finally deploys it, its that easy
- ![[Pasted image 20250324192837.png]]
- ![[Screenshot 2025-03-24 205805.png]]
- ![[Screenshot 2025-03-24 205911.png]]
- ![[Screenshot 2025-03-24 213002.png]]
- ![[Pasted image 20250331141359.png]]
___
### <u>TASK 2: Terraform</u>

What did I learn?
- So the first thing I learn in this task was about what EC2 was, how does it work and what it exactly is
- Also i learned about AMI (amazon machine images), these are basic images of OS such as ubuntu, macOs , linux etc which we can use to create EC2 instances
- I learned more about AWS and I learnt how it works
- I also learned how to make an EC2 instance using the AWS website
- Terraform is basically **IaaC** (Infrastructure as Code)
- So, its basically used to make infrastructure such as EC2 instances and manage them and also configure them using basic declarative code
- I learned basic commands such as : 
```Shell 
 terraform init 
 terraform plan 
 terraform apply 
 terraform destroy
```
- **`terraform init`** – Initializes Terraform in your working directory.
-  **`terraform plan`** – Previews the changes Terraform will make.
-  **`terraform apply`** – Executes the changes and provisions the infrastructure.
-  **`terraform destroy`** - Destroys the instances
- So I made EC2 instances and also made a basic Apache webserver using Terraform
- ![[Screenshot 2025-03-28 164255.png]]
- ![[Screenshot 2025-03-28 170321.png]]
- ![[Screenshot 2025-03-28 170459.png]]
- ![[Screenshot 2025-03-28 170637.png]]
- ![[Screenshot 2025-03-28 172146.png]]
- ![[Screenshot 2025-03-28 172800.png]]
- ![[Screenshot 2025-03-28 164905.png]]
- ![[Screenshot 2025-03-29 004851.png]]
- ![[Screenshot 2025-03-29 011810.png]]
___
### <u>TASK 3: Wireshark</u>

What did I learn?
- I learned that Wireshark is an open-source network protocol analyzer widely used to troubleshoot network issues, analyze network packets, and perform security auditing and also learnt its use cases.
	- **Packet capture**: Wireshark can capture traffic using your network interface.
	- **Protocol analysis**: Wireshark supports the decoding and analyzing of over 3000 network protocols so you can understand their structure and content.
	- **Packet filtering**: Wireshark includes powerful display and capture filters that filter network traffic.
	- **Network packet reconstruction**: Wireshark can reconstruct network packets to display application-level protocols so you can see web pages, images, or other application data.
	- **Network traffic statistics and visualizations**: Wireshark provides statistical data and visualizations of network traffic.
- I leaned about TLS and SSL, TLS is Transport Layer Security which is a cryptographic security provided to protocols in the transport layer for example `HTTPS`, so https is secure due to TLS, SSL is Secure Socket Layer, it is just an outdated version of TLS
- I learnt basic working of Wireshark and to use its tools: 
	1. **Adding Filters**
	    -  Lets you focus on specific packets by filtering out unnecessary traffic.
	    -  If you only want to see HTTP traffic, you can use the filter `http` instead of browsing through thousands of packets.
	2. **Using Statistics (Conversations, Protocol Hierarchy, IO Graphs, etc.)**
	    - Helps analyze traffic patterns by summarizing different aspects of network communication.
	    - You can check which protocols (like TCP, UDP, HTTP) are used the most, see which devices are talking to each other, and visualize traffic trends over time.
	    -  **Different Statistics in Wireshark** 
	        - Wireshark provides several **statistical tools** that help analyze network traffic patterns. These tools summarize data, making it easier to **spot issues, understand traffic flow, and optimize network performance**.
		         1. `Packet Lengths` :  Shows the distribution of packet sizes in your network capture. Helps identify abnormal packet sizes. For example, too many **very small packets** might indicate **inefficient communication**, while **unusually large packets** could be a sign of **data exfiltration or an attack**.
		         
		         2. `Protocol Hierarchy` : Breaks down traffic by protocol (e.g., HTTP, TCP, UDP, DNS).Shows **what percentage of traffic each protocol** is using. if you see too much **HTTP traffic**, it may indicate **heavy web browsing**, while a high percentage of **DNS requests** could signal **malware or misconfigurations**.
		         
		         3. `Conversations` : Lists **all communication** between two devices (IP or MAC addresses).Shows the number of packets exchanged, total bytes sent, and duration of communication. Can be used to detect **suspicious or long-lasting connections**, which may indicate **data leaks or malware**.
		         
		         4. ` Endpoints` : Lists **all devices (endpoints) communicating on the network**. Shows each device’s IP address, MAC address, packets sent, and total data exchanged. Helps **identify unknown devices** on a network.
		         
		         5.  `IO (Input/Output) Graphs` : **Graphs network traffic over time** to visualize trends. Useful for spotting **traffic spikes** that may indicate **DDoS attacks, data downloads, or streaming activity**.
		         
			    6. `Flow Graphs` : Displays **a step-by-step flow of communication** between two hosts. Helps debug **slow responses, failed connections, or retransmissions**.
		    
	3. **Following Streams**
	    - Reconstructs an entire conversation (TCP, UDP, HTTP, etc.) between two devices.
	    - If you want to see a full exchange between a computer and a server, you can "follow" the conversation instead of viewing individual packets separately.
	4. **Color Coding**
	    - **What it does:** Highlights packets with different colors to make different types of traffic stand out.
	    - **Use case:** Red may indicate TCP errors, green might show normal traffic, and black could signal serious issues like lost packets.

---
![[Screenshot 2025-03-30 104431.png]]
![[Pasted image 20250330160540.png]]

![[Screenshot 2025-03-30 104456.png]]
![[Screenshot 2025-03-30 123748.png]]
![[Screenshot 2025-03-30 125005.png]]
![[Screenshot 2025-03-30 130550.png]]
![[Screenshot 2025-03-30 131650.png]]

___

### <u>TASK 4: Docker</u>

What did I learn?
- So i learnt that Docker is used to **package, distribute, and run applications in isolated environments called containers**. It ensures that an application runs the same way on different machines, avoiding issues like "it works on my machine but not on yours."
- It packs all the necessary dependencies in a box and helps it to parcel to different clients so they can unbox and use it.
- So to help understand docker this is the example and analogy i thought of: 
	- Imagine you are developing a **Java-based banking application** on your laptop. It requires **Java, MySQL, and some libraries**. Instead of manually installing everything on every machine where you want to run the application, you can create a **Docker container** that includes the application and all its dependencies.
	- Now, you can run this container anywhere on another developer’s computer, a test server, or in the cloud without worrying about missing dependencies or configuration issues.
- I also learned the difference between VM's and Containers : 
	1. **VMs have a full operating system** (OS) inside them, including a separate kernel, making them heavy and slow to start.
	2. **Containers share the host OS kernel**, so they are lightweight and start almost instantly.
	3. **VMs need more system resources**, while **containers use less memory and CPU**.

-  Commands I learnt for using docker
	- `docker ps` → List running containers.
	- `docker ps -a` → List all containers (including stopped ones).
	- `docker run <image>` → Run a container from an image.
	- `docker start <container_id>` → Start a stopped container.
	- `docker stop <container_id>` → Stop a running container.
	- `docker restart <container_id>` → Restart a container.
	- `docker kill <container_id>` → Forcefully stop a running container.
	- `docker rm <container_id>` → Remove a stopped container.
	- `docker logs <container_id>` → View the logs of a container.
	- `docker images` → List all available images.
	- `docker pull <image>` → Download an image from Docker Hub.
	- `docker push <image>` → Push an image to Docker Hub.
	- `docker build -t <image_name> .` → Build an image from a Dockerfile.
	- `docker tag <image> <new_image_name>` → Tag an image with a new name.
	- `docker rmi <image>` → Remove an image.
	- `docker history <image>` → Show the history of an image.
	- `docker inspect <image>` → Get detailed information about an image.
- I learnt about docker compose : 
	- Docker Compose is a tool that allows you to define and manage multi-container Docker applications using a YAML configuration file (`docker-compose.yml`). Instead of running multiple `docker run` commands manually, you can define all services, networks, and volumes in one file and start them with a single command.
		- `docker-compose up` → Start services defined in `docker-compose.yml`.
		- `docker-compose down` → Stop and remove services.
		- `docker-compose ps` → List running services.
		- `docker-compose logs` → View logs of services.
		- `docker-compose restart` → Restart all services.
- I learnt the difference between images and containers: 
	- Images are nothing but a blueprint or templates for a container, the images are read only and can be configured only once, they are reusable, they are stored in docker hub, they contain all the dependencies and a base OS
			- The **application code**
			- All **dependencies** (libraries, runtimes, configurations)
			- A **base operating system** (like Ubuntu, Alpine, etc.)
			- Any **customized settings**
	- Docker containers are nothing but the running instances of a docker image, it is the actual execution of the application in an isolated environment
			- **Based on Images** → Containers are created from images.
			- **Read-Write Layer** → Containers can modify their filesystem while running.
			- **Isolated but Share the Host Kernel** → Unlike Virtual Machines, containers share the host OS kernel but have their own filesystem, processes, and network.
			- **Temporary (Ephemeral) or Persistent** → Containers can be deleted after use or configured to keep data.
___
- I learnt what a Dockerfile is and the use cases : 
	- A **Dockerfile** is a text file that contains a set of instructions for building a **Docker image**. It acts as a **blueprint** for creating lightweight, portable, and consistent environments.
	- So if we have an application, if we want to convert that application into an image we just have to include a docker file into it.
	- Once our image is created we can upload it to dicker hub and then developers can pull our images form there. To pull images we can use the `docker pull` command
	- We can push our image to docker hub using `docker push` command

- ![[Pasted image 20250330145922.png]]
- ![[Pasted image 20250330152455.png]]
- ![[Pasted image 20250330152548.png]]
- ![[Pasted image 20250330153024.png]]
- ![[Pasted image 20250330153137.png]]
- Instead of manually setting up software dependencies, a **Dockerfile automates this process**.
- ![[Pasted image 20250330151341.png]]
- ![[Pasted image 20250330151409.png]]
- ![[Pasted image 20250330151429.png]]
- ![[Pasted image 20250330151511.png]]
___

### <u>TASK 5: Docker File Spyware</u>

What did I learn?
- So here I learnt what a spyware is and what it generally does
     - **Spyware** is a type of **malicious software (malware)** that is designed to **secretly monitor, collect, and transmit data** from an infected device **without the user's knowledge or consent**. It often operates in the background, recording sensitive information such as:
		- **Keystrokes** (keyloggers)
		- **Browsing history**
		- **Login credentials** (usernames, passwords)
		- **Personal data** (emails, financial details)
		- **Microphone & camera activity**
	- Types of spyware: 
		1. **Keyloggers** – Record everything typed on a keyboard.
		2. **Adware** – Tracks browsing habits to display targeted ads.
		3. **Trojan-based Spyware** – Disguised as legitimate software but secretly collects data.
		4. **Tracking Cookies** – Small files that track web activity across sites.
		5. **System Monitors** – Capture screenshots, record chats, and monitor internet usage.
- In this task I learnt a lot about SSH, here i learn how to SSH into EC2 instances and then run docker on those EC2 instances. I also learnt how to manually transfer files using `SSH scp`
- I learnt how to run a SH script to automate the task of transferring newly added images from one server to another server
- So the steps I followed for this task is as follows:
     1. Launched 2 EC2 instances, `first_server` and `second_server` using the AWS website
     2. SSH into to `first_server` and installed docker and created a dockerfile that runs the monitor script and automates the process 
     ``` Shell
     # Use a lightweight Linux base image
FROM ubuntu:latest

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    inotify-tools \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV WATCH_DIR=/watched_folder
ENV REMOTE_USER=ubuntu
ENV REMOTE_HOST=34.224.174.148
ENV REMOTE_PATH=/home/ubuntu/images

# Create necessary directories
RUN mkdir -p $WATCH_DIR

# Copy the monitor script into the container
COPY monitor.sh /monitor.sh
RUN chmod +x /monitor.sh

# Copy the SSH private key (for SCP)
COPY jeethan-key.pem /root/.ssh/jeethan-key.pem
RUN chmod 400 /root/.ssh/jeethan-key.pem

# Start monitoring when the container runs
CMD ["/bin/bash", "/monitor.sh"]
     ```

	 3. Created a folder using the dockerfile where images will be uploaded in the first server:
    ```bash
    mkdir -p ~/watched_folder
    ```
  2. 4. Created a folder where images will be received in the second server: 
    ```bash
    mkdir -p ~/images
    ```
  3. 5. Created the `monitor.sh` Script**
		- This script **monitors the `watched_folder`** for new images and **automatically transfers** them to `SECOND_EC2` using `scp`.
		```bash
#!/bin/bash

	WATCH_DIR="/home/ubuntu/watched_folder"
	REMOTE_USER="ubuntu"
	REMOTE_HOST="<SECOND_EC2_IP>"
	REMOTE_PATH="/home/ubuntu/images"
	KEY_PATH="/home/ubuntu/jeethan-key.pem"
	
	# Ensure the watched directory exists
	mkdir -p "$WATCH_DIR"
	
	echo "Monitoring $WATCH_DIR for new files..."
	
	# Start monitoring directory for new files
	inotifywait -m -e create "$WATCH_DIR" --format "%f" |
	while read FILE; do
	    echo "New file detected: $FILE"
	    scp -i "$KEY_PATH" "$WATCH_DIR/$FILE" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"
	    if [ $? -eq 0 ]; then
	        echo "File successfully transferred: $FILE"
	    else
	        echo "Error transferring file: $FILE"
	    fi
	done
```
    - And done we just have to upload the images in the first_server and it will be trasferred
    - ![[Pasted image 20250330222356.png]]
    - ![[Pasted image 20250330222414.png]]
___
### <u>TASK 6: Hashing</u>

What did I learn?
- So I learnt what hashing is, Hashing is the process of converting an input (or "message") into a fixed-size string of characters, using a mathematical algorithm called a hash function. The output, known as the hash value or digest, is unique for a given input. Even a small change in the input will produce a vastly different hash value.
- I learnt different hashing algorithms : 
		Hashing algorithms are categorized into two major types:
			1. **Cryptographic Hashing** – Designed for security (passwords, digital signatures, blockchain).
			2. **Non-Cryptographic Hashing** – Designed for speed (hash tables, checksums, error detection).

| Algorithm      | Hash Length | Secure? | Use Case                                     |
| -------------- | ----------- | ------- | -------------------------------------------- |
| **MD5**        | 128-bit     | No      | Legacy file checksums (not for security)     |
| **SHA-1**      | 160-bit     | No      | Old SSL/TLS, digital signatures (deprecated) |
| **SHA-256**    | 256-bit     | Yes     | Blockchain, file verification                |
| **Bcrypt**     | Variable    | Yes     | Secure password hashing (includes salting)   |
| **Argon2**     | Variable    | Yes     | Modern password hashing, highly secure       |
| **MurmurHash** | Variable    | No      | Hash tables, fast database lookups           |
| **FNV-1a**     | Variable    | No      | Caching, simple hash functions               |
| **CRC32**      | 32-bit      | No      | Error detection in networking                |
![[Pasted image 20250330164948.png]]
![[Pasted image 20250330165034.png]]
___
### <u>TASK 7: NMap</u>

What did I learn?

- Nmap (**Network Mapper**) is a powerful **network scanning tool** used for discovering hosts, scanning ports, detecting services, identifying operating systems, and finding security vulnerabilities.
- It works by sending network packets to a target and analyzing the responses to gather information about the system.

---
- ### **Basic Nmap Commands and Their Use Cases**

| **Command**                    | **Description**                                                                                          | **Use Case**                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `nmap <target>`                | Basic scan to detect live hosts and open ports.                                                          | Quick check for available hosts and open services.                              |
| `nmap -sS <target>`            | **Stealthy TCP SYN scan**. Sends SYN packets without completing handshake.                               | Used for **fast, undetected scanning** on networks with firewalls or IDS.       |
| `nmap -sT <target>`            | **TCP Connect scan**. Completes the full handshake.                                                      | Used when running Nmap as a normal (non-root) user.                             |
| `nmap -sU <target>`            | **UDP Scan** to detect open UDP ports.                                                                   | Identifies services like **DNS, DHCP, SNMP, VoIP** which run on UDP.            |
| `nmap -p 80 <target>`          | Scan a **specific port** (e.g., 80 for HTTP).                                                            | Used to check if a specific service (e.g., a web server) is running.            |
| `nmap -p 1-1000 <target>`      | Scan a **range of ports** (1 to 1000).                                                                   | Checks for common open ports.                                                   |
| `nmap -p- <target>`            | Scan **all 65535 ports** on a target.                                                                    | Comprehensive scan to detect all running services.                              |
| `nmap -O <target>`             | **OS detection**. Identifies the operating system of the target.                                         | Helps determine if the target is running Windows, Linux, or macOS.              |
| `nmap -sV <target>`            | **Service version detection**. Identifies the exact software running on open ports.                      | Useful for finding **outdated or vulnerable services**.                         |
| `nmap -A <target>`             | **Aggressive scan** (combines OS detection, service version detection, script scanning, and traceroute). | Provides **detailed** information about the target.                             |
| `nmap --script=vuln <target>`  | Runs **vulnerability detection scripts**.                                                                | Identifies known security weaknesses in software.                               |
| `nmap -Pn <target>`            | Disables host discovery (ping scan) and assumes the target is online.                                    | Useful when **ping requests are blocked** by firewalls.                         |
| `nmap -f <target>`             | **Fragment packets** to evade firewalls.                                                                 | Helps bypass network security filters.                                          |
| `nmap -D RND:10 <target>`      | **Decoy scanning**. Spoofs 10 random IP addresses to mask the real scanner.                              | Used to **avoid detection** and make tracking difficult.                        |
| `nmap -T4 <target>`            | Adjust scan speed (`-T0` is slow, `-T5` is fastest).                                                     | **Faster scans** for large networks (`-T4` is a good balance).                  |
| `nmap -sC <target>`            | Run **default scripts** for common vulnerabilities and misconfigurations.                                | Quick **security check** for known issues.                                      |
| `nmap -sM <target>`            | **Firewalk scan** to test firewall rules.                                                                | Helps map out **which ports are allowed or blocked** by a firewall.             |
| `nmap -sX <target>`            | **XMAS scan** (sets FIN, PSH, and URG flags) to detect closed ports.                                     | Used for **stealth scanning** since some firewalls do not detect these packets. |
| `nmap -sP <network>`           | **Ping scan** to detect all live hosts in a network.                                                     | Finds **all connected devices** in a subnet (e.g., `192.168.1.0/24`).           |
| `nmap --traceroute <target>`   | Traces the path of packets to the target.                                                                | Helps in **network troubleshooting** by showing the route packets take.         |
| `nmap -oN output.txt <target>` | Saves scan results to a file in normal text format.                                                      | Used to **log scan results** for later analysis.                                |
| `nmap -oX output.xml <target>` | Saves scan results in XML format.                                                                        | Helps in **automating scans** and exporting data for other tools.               |
- ![[Screenshot 2025-03-30 171012.png]]

- ![[Screenshot 2025-03-30 171032.png]]

- ![[Screenshot 2025-03-30 171643.png]]

- ![[Screenshot 2025-03-30 171845.png]]
___
### <u>TASK 8: AWS Lambda</u>

What did I learn ?
- So I learnt more about AWS in this task, I learnt about what FaaS is and why is it used
- So, AWS Lambda is a **serverless computing service** provided by Amazon Web Services (AWS) that lets you run code **without provisioning or managing servers**. It automatically **scales** and only charges you for the execution time of your code.
- This means that the developer only focuses on code and doesn't need to worry about managing servers and database
- AWS uses DynamoDB to store data
-  **Features of AWS lambda**
	1. **Event-Driven Execution**
		- AWS Lambda **executes code** when triggered by an **event** from AWS services (e.g., an HTTP request, a database update, or a file upload to an S3 bucket).
	2. **No Server Management**
	    - AWS **manages the infrastructure**, so you don’t need to worry about provisioning or scaling servers.
	3. **Auto-Scaling**
	    - It automatically scales **up** or **down** based on the incoming number of events.
	4. **Pay-per-Use Pricing**
	    - You are billed **only for execution time** (milliseconds) and the number of requests.

| Feature          | **AWS Lambda (Serverless)** | **Traditional Servers (EC2, On-Premises)** |
| ---------------- | --------------------------- | ------------------------------------------ |
| **Provisioning** | No servers to manage        | Requires manual server setup               |
| **Scaling**      | Automatic scaling           | Requires load balancers and manual scaling |
| **Pricing**      | Pay only for execution time | Pay for entire server uptime               |
| **Complexity**   | Easier to maintain          | More infrastructure management needed      |
So in this task I have made a simple HelloWorld program which when triggers print key-value pairs as shown: 

![[Screenshot 2025-03-31 134034.png]]

![[Screenshot 2025-03-31 134137.png]]

![[Screenshot 2025-03-31 134236.png]]

![[Screenshot 2025-03-31 134755.png]]

![[Screenshot 2025-03-31 134825.png]]____

___
### <u>Task 9: SSH</u>

What did I learn?
- SSH stands for **Secure Shell**. It is a protocol used to securely connect to a remote computer or server over an unsecured network. SSH provides encrypted communication between the two systems, ensuring the confidentiality, integrity, and authenticity of the connection.
- ![[Pasted image 20250101184633.png]]
- SSH is used for : 
		1. **Secure Remote Access:** SSH is primarily used to remotely access and manage servers, devices, or computers. It allows administrators to execute commands, transfer files, and perform system maintenance securely.
		2. **Encrypted Communication:** Unlike older protocols like Telnet or FTP, SSH encrypts all data transmitted between the client and the server, protecting against eavesdropping and man-in-the-middle attacks.
		3. **Authentication and Authorization:** SSH uses cryptographic keys or passwords to verify the identity of users, ensuring only authorized individuals can access the system.
- How Does SSH Work?
	1. **Client-Server Model:** SSH operates using a client-server architecture. One system acts as the client initiating the connection, while the other acts as the server, accepting and responding to the connection.
	2. **Encryption:**
	    - When a client connects to an SSH server, both systems exchange cryptographic keys to establish a secure, encrypted communication channel.
	    - The encryption ensures that all data transferred between the client and server is scrambled, making it unreadable to anyone intercepting the communication.
	3. **Authentication:**
	    - **Password Authentication:** The client provides a username and password to authenticate.
	    - **Public/Private Key Authentication:** A more secure method where the client has a private key, and the server has the corresponding public key. The client proves its identity by signing a challenge using the private key.
	4. **Session Establishment:**
	    - After authentication, a secure session is established. Commands sent by the client are executed on the server, and the results are returned to the client.
		![[Pasted image 20250101184833.png]]

		![[Pasted image 20250101185439.png]]
		![[Pasted image 20250101185503.png]]
- So in this task I connected to the first EC2 instance and then searched for `ssh.pem` file and then transferred it into the second EC2 instance 
	- ![[Pasted image 20250401211942.png]]
	- ![[Pasted image 20250401211950.png]]
	- ![[Pasted image 20250401212003.png]]
	- ![[Pasted image 20250401212008.png]]

___
### <u>TASK 10: Web Scraping and Automation - Flight Ticket Price Analysis</u>

What did I learn?
- I learnt the basics of selenium and how it works
- i learnt what web scraping is and how it can be used
- I also learnt the ethical and legal issues with web scraping
- In this task the program automatically opens chrome tab, searches the website, fills in the details, finds the flights and then writes it into a text file and a csv file which we cab use to analyse later
- **Web scraping** is the process of extracting data from websites by simulating human interaction with the web page using a program or script. This data can be anything publicly available on a website, such as text, images, videos, or even complex data like tables and charts. Scraping can be done through libraries like `BeautifulSoup`, `Selenium`, and `Scrapy` in Python, or through other programming languages and tools.
- Web scraping typically involves:
	1. **Sending an HTTP request** to the website’s server to retrieve its content.
	2. **Parsing the HTML content** of the page to extract the relevant data.
	3. **Storing or processing the extracted data** as per the user’s needs.
- Ethical Issues in Web Scraping: 
    1. **Impact on Website Performance**: If a scraper is too aggressive and sends too many requests in a short period, it can overwhelm a website’s server, potentially slowing down or crashing the website. This can harm the website's operations and disrupt services for legitimate users.
    2. **Violation of Terms of Service**: Many websites explicitly prohibit scraping in their Terms of Service (ToS). Ignoring these terms and scraping the data could lead to conflicts with the website owner or platform.
    3. **Bot Laws**: Some countries have specific laws regarding the use of bots for data scraping. These laws aim to prevent bots from misusing data or overloading servers.
- ![[Pasted image 20250401202634.png]]
- ![[Pasted image 20250401210159.png]]
___
