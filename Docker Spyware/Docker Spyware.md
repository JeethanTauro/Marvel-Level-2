

I set up an **automated file transfer system** where any image uploaded to `FIRST_EC2` (`~/watched_folder`) is automatically transferred to `SECOND_EC2` (`~/images`).
So basically here the spyware watches for any changes in the `watched_folder` if any image is uploaded the the image gets transferred to another server 

---

## **Step 1: Launched Two EC2 Instances**

- **FIRST_EC2** (Source machine where images are uploaded).
- **SECOND_EC2** (Destination machine where images are transferred).
- I used AWS website to launch 2 ubuntu EC2 instances and named them first and second

---
ssh into first and second server:
```Shell
ssh -i C:\Users\TH\Desktop\jeethan-key.pem ubuntu@54.167.119.11
ssh -i C:\Users\TH\Desktop\jeethan-key.pem ubuntu@34.224.174.148

then to check if monitor.sh is working : ps aux
if not then : nohup bash /home/ubuntu/monitor.sh > /home/ubuntu/monitor.log 2>&1 &
```
## **Step 2: Set Up SSH Key-Based Authentication**

To allow `FIRST_EC2` to securely transfer files to `SECOND_EC2`, we used an **SSH private key**.
1. **Transferred the private key (`jeethan-key.pem`) from local machine to `FIRST_EC2`**:
    ```bash
    scp -i "C:\Users\TH\Desktop\jeethan-key.pem" "C:\Users\TH\Desktop\jeethan-key.pem" ubuntu@<FIRST_EC2_IP>:~/
    ```
2. **Set correct permissions on `FIRST_EC2`**: (400 means only owner can read)
    ```bash
    chmod 400 ~/jeethan-key.pem
    ```
3. **Tested SSH access from `FIRST_EC2` to `SECOND_EC2`**:
    ```bash
    ssh -i ~/jeethan-key.pem ubuntu@<SECOND_EC2_IP>
    ```
    - So here i connected my first server to second server using SSH
---

## **Step 3: Created Necessary Directories**

### **On `FIRST_EC2` (Source)**

- Created a folder where images will be uploaded:
    ```bash
    mkdir -p ~/watched_folder
    ```
### **On `SECOND_EC2` (Destination)**
- Created a folder where images will be received:
    ```bash
    mkdir -p ~/images
    ```
    - -p ensures that the directory is created the way it is given even if the path doesn't exist
    - ~ basically means home directory
---

## **Step 4: Created the `monitor.sh` Script**
- This script **monitors the `watched_folder`** for new images and **automatically transfers** them to `SECOND_EC2` using `scp`.
### **Final `monitor.sh` Script**

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

---

## **Step 5: Gave Execution Permission to the Script**

On `FIRST_EC2`, ran:
```bash
chmod +x ~/monitor.sh
```

---

## **Step 6: Started the Script in the Background**

To ensure the script runs even if we log out, we used `nohup`:

```bash
nohup bash ~/monitor.sh > ~/monitor.log 2>&1 &
```

- `nohup` ensures the script runs in the background even after logging out.
- Output is stored in `monitor.log`.
---

## **Step 7: Verified Automatic File Transfer**

1. **Uploaded a test image on `FIRST_EC2`**:
    ```bash
    touch ~/watched_folder/test.jpg
    ```
2. **Checked if the file was successfully transferred to `SECOND_EC2`**:
    ```bash
    ssh -i C:\Users\TH\Desktop\jeethan-key.pem ubuntu@34.224.174.148 "ls -l ~/images"
    ```

---


---

## **Next Steps**

- If you want this script to **start automatically on system reboot**, add the following line to `crontab` (`crontab -e` on `FIRST_EC2`):
    
    ```
    @reboot nohup bash /home/ubuntu/monitor.sh > /home/ubuntu/monitor.log 2>&1 &
    ```
    
- This ensures the script runs whenever `FIRST_EC2` reboots.
    

---

![[Screenshot 2025-03-30 193701.png]]

![[Screenshot 2025-03-30 180630.png]]

![[Screenshot 2025-03-30 181432.png]]

![[Screenshot 2025-03-30 181444.png]]

![[Screenshot 2025-03-30 181450.png]]

![[Screenshot 2025-03-30 182748.png]]

![[Screenshot 2025-03-30 183020.png]]

![[Screenshot 2025-03-30 183215.png]]

![[Screenshot 2025-03-30 184349.png]]

![[Screenshot 2025-03-30 193656.png]]![[Pasted image 20250330222356.png]]
![[Pasted image 20250330222414.png]]
___
You can create the **Dockerfile** on your first EC2 instance (`EC2_FIRST`) by following these steps:

---

### **Step 1: Create a Directory for the Project**

On your first EC2 instance, run:

```bash
mkdir ~/file-watcher && cd ~/file-watcher
```

---

### **Step 2: Create the Dockerfile**

Run:

```bash
nano Dockerfile
```

Then, **copy and paste** the following content into the `Dockerfile`:

```dockerfile
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

Save and exit (`CTRL+X`, then `Y`, then `ENTER`).

---

### **Step 3: Create the Monitoring Script**

Now, create the `monitor.sh` file:

```bash
nano monitor.sh
```

Paste the following script inside:

```bash
#!/bin/bash

WATCH_DIR="/watched_folder"
REMOTE_USER="ubuntu"
REMOTE_HOST="34.224.174.148"
REMOTE_PATH="/home/ubuntu/images"
SSH_KEY="/root/.ssh/jeethan-key.pem"

# Start watching the directory
inotifywait -m -e create "$WATCH_DIR" --format '%f' | while read FILE
do
    echo "New file detected: $FILE"
    scp -i "$SSH_KEY" "$WATCH_DIR/$FILE" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"
    if [ $? -eq 0 ]; then
        echo "File $FILE successfully transferred to $REMOTE_HOST"
    else
        echo "Error transferring file $FILE"
    fi
done
```

Save and exit (`CTRL+X`, then `Y`, then `ENTER`).

---

### **Step 4: Copy the SSH Private Key**

If your private key (`jeethan-key.pem`) is on your **local computer**, upload it to the EC2 instance using SCP:

```bash
scp -i ~/.ssh/your-key.pem ~/path/to/jeethan-key.pem ubuntu@<EC2_FIRST_IP>:~/file-watcher/
```

Move it inside the project folder:

```bash
mv ~/file-watcher/jeethan-key.pem ~/file-watcher/
```

Ensure correct permissions:

```bash
chmod 400 ~/file-watcher/jeethan-key.pem
```

---

### **Step 5: Build the Docker Image**

Run the following command in the `file-watcher` directory:

```bash
docker build -t file-watcher .
```

---

### **Step 6: Run the Docker Container**

Start the container with:

```bash
docker run -d --name file-watcher \
  -v ~/watched_folder:/watched_folder \
  file-watcher
```

- The `-d` flag runs the container in the background.
    
- The `-v` flag **mounts** the `watched_folder` directory from your host system into the container.
    

---

### **Step 7: Test the File Transfer**

Now, create a test image in your **watched folder**:

```bash
touch ~/watched_folder/test.jpg
```

This should **automatically transfer** `test.jpg` to `/home/ubuntu/images` on the second EC2 instance.

---

### **Step 8: Check Logs (if needed)**

To check if the script is working, you can inspect the logs:

```bash
docker logs file-watcher
```

---

### **Step 9: Enable Auto-Start on Reboot**

Ensure the container restarts automatically after a system reboot:

```bash
docker update --restart unless-stopped file-watcher
```

---

### **What Happens Now?**

- Your `file-watcher` container runs in the background.
    
- It **detects** any new files in `watched_folder`.
    
- The new files are **automatically transferred** to `EC2_SECOND` using `scp`.
    

---

This setup ensures that **even if you restart your EC2 instance**, the monitoring script will **continue running** inside the Docker container.

Would you like to add any enhancements, such as logging to a file or sending notifications?