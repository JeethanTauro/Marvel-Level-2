### **What is Hashing?**

Hashing is the process of converting an input (or "message") into a fixed-size string of characters, which is usually a hexadecimal number, using a mathematical algorithm called a hash function. The output, known as the hash value or digest, is unique for a given input. Even a small change in the input will produce a vastly different hash value.

---

### **Why is Hashing Used?**

Hashing is widely used for several purposes:

1. **Data Checking**: To verify that data has not been altered (e.g., in file integrity checks or message authentication).
4. **Hash Tables**: For efficient data retrieval in programming.
5. **Blockchain**: To maintain the integrity of blocks in a blockchain.

---

### **Difference Between Authentication and Authorization**

| **Authentication**                                         | **Authorization**                                                            |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------- |
| The process of verifying the identity of a user or system. | The process of granting or denying access to resources based on permissions. |
| Confirms **who you are**.                                  | Determines **what you are allowed to do**.                                   |


### **Detailed Explanation of Hashing Algorithms**

Hashing algorithms are categorized into two major types:

1. **Cryptographic Hashing** – Designed for security (passwords, digital signatures, blockchain).
    
2. **Non-Cryptographic Hashing** – Designed for speed (hash tables, checksums, error detection).
    

Each algorithm follows a unique process to transform data into a hash. Below is an in-depth breakdown of different hashing techniques and how they work.

---

## **1. Cryptographic Hashing Algorithms**

These algorithms ensure security by making it computationally infeasible to reverse-engineer the original input from the hash.

### MD5 (Message Digest Algorithm 5)
1. The input is divided into **512-bit blocks**.
2. Each block undergoes **four rounds of processing**, each with 16 operations.
3. Uses bitwise operations (AND, OR, XOR, shifts) to scramble data.
4. The final result is a **128-bit hash**.
5. Previously used for **password hashing** and **file checksums**.
6. Now obsolete due to **collision vulnerabilities** (two different inputs can produce the same hash).
	**Example:**  
		MD5 of `"hello"` → `5d41402abc4b2a76b9719d911017c592`

**Security Issue:**  
Attackers can generate the same hash for two different inputs (collision attack), making MD5 unsafe for cryptographic purposes.

---

### SHA-1 (Secure Hash Algorithm 1) 
1. The input is **padded** to fit into 512-bit blocks.        
2. Uses **five 32-bit words (H0 to H4)** initialized with fixed values.
3. **80 rounds** of processing involve bitwise operations, shifts, and modular additions.  
4. Produces a **160-bit hash**.
5. Previously used for **SSL certificates** and **digital signatures**.
6. No longer secure due to **collision attacks**.
	**Example:**  
		SHA-1 of `"hello"` → `f572d396fae9206628714fb2ce00f72e94f2258f`

---

### SHA-256 
1. Input is padded and divided into **512-bit blocks**.
2. Uses **eight 32-bit words (H0 to H7)** initialized with predefined values.
3. **64 rounds** of complex transformations, including bitwise operations, shifts, and modular arithmetic.
4. Produces a **256-bit hash** (hex representation is 64 characters long).
5. Used in **blockchain (Bitcoin, Ethereum)**.
6. Secure for **file integrity verification** and **digital signatures**.
	**Example:**  
		SHA-256 of `"hello"` →  
		`2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824`
---

### Bcrypt
1. Adds a **random salt** to prevent precomputed attacks.
2. Uses the **Blowfish cipher** internally.
3. Performs multiple rounds (cost factor) to slow down brute-force attacks.
4. Secure for **storing passwords**.
5. Adjustable computation cost makes brute-force attacks impractical.
	**Example Output:**  
		Bcrypt hash of `"password123"` →  
		`$2a$12$eL.ZO14L1ik5MQ7Jq8RHq.V3t83WjG3U7po6mc6FylXfpRC3HbF7i`
### Argon2 
1. Uses **random salt** and **multiple memory-intensive iterations**.
2. Performs **parallel computation** to make brute-force attacks infeasible.
3. Modern and **recommended for password hashing**.
4. Used in **cryptographic applications** where security is crucial.

---

## **2. Non-Cryptographic Hashing Algorithms**

These algorithms prioritize speed and efficiency rather than security.
### MurmurHash
1. Uses **bitwise shifts and multiplications** to distribute data evenly.
2. No cryptographic security but is very fast.
3. Used in **databases and hash tables** for fast lookups.
### FNV-1a (Fowler-Noll-Vo)

 1. Starts with a **large prime number** as an initial hash.
 2. ORs each byte with the hash and multiplies it by a prime number.
 3. ed in **cache lookups and fast non-secure hashing**.
### CRC32 (Cyclic Redundancy Check)

1. Treats data as a **binary polynomial** and divides it by a fixed divisor.
2. Remainder is the CRC checksum.
3. Used in **network packets and file verification** to detect transmission errors.
---

## **Comparison of Hashing Algorithms**

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
