


### **What is Nmap?**

Nmap (**Network Mapper**) is a powerful **network scanning tool** used for discovering hosts, scanning ports, detecting services, identifying operating systems, and finding security vulnerabilities.
It works by sending network packets to a target and analyzing the responses to gather information about the system.

---

### **Nmap Commands and Their Use Cases**

|**Command**|**Description**|**Use Case**|
|---|---|---|
|`nmap <target>`|Basic scan to detect live hosts and open ports.|Quick check for available hosts and open services.|
|`nmap -sS <target>`|**Stealthy TCP SYN scan**. Sends SYN packets without completing handshake.|Used for **fast, undetected scanning** on networks with firewalls or IDS.|
|`nmap -sT <target>`|**TCP Connect scan**. Completes the full handshake.|Used when running Nmap as a normal (non-root) user.|
|`nmap -sU <target>`|**UDP Scan** to detect open UDP ports.|Identifies services like **DNS, DHCP, SNMP, VoIP** which run on UDP.|
|`nmap -p 80 <target>`|Scan a **specific port** (e.g., 80 for HTTP).|Used to check if a specific service (e.g., a web server) is running.|
|`nmap -p 1-1000 <target>`|Scan a **range of ports** (1 to 1000).|Checks for common open ports.|
|`nmap -p- <target>`|Scan **all 65535 ports** on a target.|Comprehensive scan to detect all running services.|
|`nmap -O <target>`|**OS detection**. Identifies the operating system of the target.|Helps determine if the target is running Windows, Linux, or macOS.|
|`nmap -sV <target>`|**Service version detection**. Identifies the exact software running on open ports.|Useful for finding **outdated or vulnerable services**.|
|`nmap -A <target>`|**Aggressive scan** (combines OS detection, service version detection, script scanning, and traceroute).|Provides **detailed** information about the target.|
|`nmap --script=vuln <target>`|Runs **vulnerability detection scripts**.|Identifies known security weaknesses in software.|
|`nmap -Pn <target>`|Disables host discovery (ping scan) and assumes the target is online.|Useful when **ping requests are blocked** by firewalls.|
|`nmap -f <target>`|**Fragment packets** to evade firewalls.|Helps bypass network security filters.|
|`nmap -D RND:10 <target>`|**Decoy scanning**. Spoofs 10 random IP addresses to mask the real scanner.|Used to **avoid detection** and make tracking difficult.|
|`nmap -T4 <target>`|Adjust scan speed (`-T0` is slow, `-T5` is fastest).|**Faster scans** for large networks (`-T4` is a good balance).|
|`nmap -sC <target>`|Run **default scripts** for common vulnerabilities and misconfigurations.|Quick **security check** for known issues.|
|`nmap -sM <target>`|**Firewalk scan** to test firewall rules.|Helps map out **which ports are allowed or blocked** by a firewall.|
|`nmap -sX <target>`|**XMAS scan** (sets FIN, PSH, and URG flags) to detect closed ports.|Used for **stealth scanning** since some firewalls do not detect these packets.|
|`nmap -sP <network>`|**Ping scan** to detect all live hosts in a network.|Finds **all connected devices** in a subnet (e.g., `192.168.1.0/24`).|
|`nmap --traceroute <target>`|Traces the path of packets to the target.|Helps in **network troubleshooting** by showing the route packets take.|
|`nmap -oN output.txt <target>`|Saves scan results to a file in normal text format.|Used to **log scan results** for later analysis.|
|`nmap -oX output.xml <target>`|Saves scan results in XML format.|Helps in **automating scans** and exporting data for other tools.|
![[Screenshot 2025-03-30 171012.png]]

![[Screenshot 2025-03-30 171032.png]]

![[Screenshot 2025-03-30 171643.png]]

![[Screenshot 2025-03-30 171845.png]]