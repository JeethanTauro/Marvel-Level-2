### What is SSH?

SSH stands for **Secure Shell**. It is a protocol used to securely connect to a remote computer or server over an unsecured network. SSH provides encrypted communication between the two systems, ensuring the confidentiality, integrity, and authenticity of the connection.
![[Pasted image 20250101184633.png]]


### Why is SSH Used?

1. **Secure Remote Access:** SSH is primarily used to remotely access and manage servers, devices, or computers. It allows administrators to execute commands, transfer files, and perform system maintenance securely.
    
2. **Encrypted Communication:** Unlike older protocols like Telnet or FTP, SSH encrypts all data transmitted between the client and the server, protecting against eavesdropping and man-in-the-middle attacks.
    
3. **Authentication and Authorization:** SSH uses cryptographic keys or passwords to verify the identity of users, ensuring only authorized individuals can access the system.

---

### How Does SSH Work?

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

---


### Public/Private Key Authentication:

1. **Key Generation:** The client generates a key pair:
    
    ```bash
    ssh-keygen -t rsa -b 4096
    ```
    
    This creates:
    
    - `id_rsa` (private key)
    - `id_rsa.pub` (public key)
2. **Key Deployment:**
    
    - The public key is copied to the server's `~/.ssh/authorized_keys` file:
        
        ```bash
        ssh-copy-id user@server_ip
        ```
        
3. **Connection:**
    
    - When connecting, the server challenges the client. The client uses its private key to respond, proving its identity without sending sensitive information over the network.
![[Pasted image 20250101185439.png]]

---
![[Pasted image 20250101185223.png]]
![[Pasted image 20250101185300.png]]

![[Pasted image 20250101185503.png]]

