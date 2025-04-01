## **What is Jenkins Used For?**

Jenkins is an **automation server** used for **Continuous Integration (CI) and Continuous Deployment (CD)** in software development. It automates **building, testing, and deploying** applications, making software delivery **faster and more reliable**.

### **Common Use Cases of Jenkins:**

1. **Continuous Integration (CI)** – Automatically integrates new code changes from developers.
2. **Automated Testing** – Runs tests to detect bugs before deployment.
3. **Continuous Deployment (CD)** – Deploys tested applications to production without manual intervention.
4. **Infrastructure as Code (IaC)** – Automates server provisioning using tools like Terraform and Ansible.
5. **Monitoring and Alerts** – Sends notifications for build failures (Slack, Email, etc.).

---

## **Example: Jenkins Automating a Java Web App Deployment**

### **Scenario**:

A company is developing a **Java-based banking application**. They want to automate the process of **building, testing, and deploying** new features.

### **Jenkins Workflow for CI/CD**

1. **Developer writes and commits code** to **GitHub**.
2. **Jenkins detects the change** and pulls the latest code.
3. **Jenkins builds the application** using **Maven**.
4. **Jenkins runs automated tests** to check for bugs.
5. If tests pass, **Jenkins deploys the app** to a **Tomcat server** (staging/production).
6. **Jenkins sends notifications** to the team about the deployment status.

### **Jenkins Pipeline Code (Jenkinsfile)**

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/example/banking-app.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'scp target/banking-app.war user@server:/tomcat/webapps/'
            }
        }
    }
}
```

### **How It Works:**

✔ **Automates Code Integration** → No manual merging required.  
✔ **Ensures Code Quality** → Runs tests to prevent errors.  
✔ **Deploys Application Quickly** → No need for manual intervention.

___
## **What is Jenkins Pipeline?**

A **Jenkins Pipeline** is a set of steps that automate **building, testing, and deploying** applications. It is written as **code (Pipeline as Code)** and allows developers to define the CI/CD process in a structured way.

### **Key Features of Jenkins Pipeline:**

✅ **Automates CI/CD workflows** – Builds, tests, and deploys software automatically.  
✅ **Pipeline as Code** – Uses a script (Jenkinsfile) for easy version control.  
✅ **Parallel Execution** – Runs multiple jobs at once for efficiency.  
✅ **Error Handling** – Detects failures and supports rollback mechanisms.

---

## **Types of Jenkins Pipelines**

1. **Declarative Pipeline** – Uses a simple, structured syntax (recommended for most cases).
2. **Scripted Pipeline** – More flexible but requires Groovy scripting knowledge.

---

## **Example: Declarative Jenkins Pipeline**

This pipeline **pulls code from Git, builds it with Maven, tests it, and deploys it to a server**.

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/example/repository.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'scp target/app.war user@server:/webapps/'
            }
        }
    }
}
```

---

## **How This Works in a CI/CD Pipeline**

1. **Checkout Code** → Pulls the latest code from GitHub.
2. **Build** → Compiles the code using Maven.
3. **Test** → Runs unit tests to check for errors.
4. **Deploy** → If tests pass, the application is deployed to a server.
___
![[Pasted image 20250324192837.png]]
![[Pasted image 20250324192853.png]]
![[Pasted image 20250324192909.png]]
![[Pasted image 20250324192934.png]]
![[Pasted image 20250324193311.png]]
![[Pasted image 20250324201848.png]]
