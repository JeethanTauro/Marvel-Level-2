### **What is AWS Lambda?**

So, AWS Lambda is a **serverless computing service** provided by Amazon Web Services (AWS) that lets you run code **without provisioning or managing servers**. It automatically **scales** and only charges you for the execution time of your code.
This means that the developer only focuses on code and doesn't need to worry about managing servers and database
AWS uses DynamoDB to store data

---

### **Features of AWS lambda**

1. **Event-Driven Execution**
	    - AWS Lambda **executes code** when triggered by an **event** from AWS services (e.g., an HTTP request, a database update, or a file upload to an S3 bucket).
2. **No Server Management**
    - AWS **manages the infrastructure**, so you don’t need to worry about provisioning or scaling servers.
3. **Auto-Scaling**
    - It automatically scales **up** or **down** based on the incoming number of events.
4. **Pay-per-Use Pricing**
    - You are billed **only for execution time** (milliseconds) and the number of requests.

---

### **AWS Lambda vs. Traditional Servers**

| Feature          | **AWS Lambda (Serverless)** | **Traditional Servers (EC2, On-Premises)** |
| ---------------- | --------------------------- | ------------------------------------------ |
| **Provisioning** | No servers to manage        | Requires manual server setup               |
| **Scaling**      | Automatic scaling           | Requires load balancers and manual scaling |
| **Pricing**      | Pay only for execution time | Pay for entire server uptime               |
| **Complexity**   | Easier to maintain          | More infrastructure management needed      |

---

So in this task I have made a simple HelloWorld program which when triggers print key-value pairs as shown

![[Screenshot 2025-03-31 134034.png]]

![[Screenshot 2025-03-31 134137.png]]

![[Screenshot 2025-03-31 134236.png]]

![[Screenshot 2025-03-31 134755.png]]

![[Screenshot 2025-03-31 134825.png]]