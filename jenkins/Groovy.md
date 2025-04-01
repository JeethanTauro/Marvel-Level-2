
### **Groovy: Overview and Use in Jenkins**

#### **What is Groovy?**

Groovy is a powerful, dynamically typed programming language that runs on the Java Virtual Machine (JVM). It is often used for scripting, automation, and building applications. Groovy is syntactically similar to Java but offers additional features like closures, metaprogramming, and scripting capabilities.

Key characteristics of Groovy:

- **Compatible with Java**: Can use Java libraries and frameworks.
- **Concise and Expressive**: Reduces boilerplate code.
- **Dynamic and Static Typing**: Supports both paradigms.
- **Scripting Capabilities**: Ideal for automation and configuration.
- **Domain-Specific Language (DSL) Support**: Useful in build tools like Gradle and Jenkins pipelines.

---

#### **Groovy in Jenkins**

Jenkins, an automation server primarily used for CI/CD (Continuous Integration/Continuous Deployment), relies heavily on Groovy for scripting and pipeline automation. It allows users to define build workflows in a structured way.

**Ways Groovy is used in Jenkins:**

1. **Jenkins Pipelines** (Declarative & Scripted Pipelines)
2. **Jenkins Console & Script Console**
3. **Jenkins Shared Libraries**
4. **Jenkinsfile** (Pipeline-as-Code)
5. **Managing Jenkins Configuration & Jobs**

---

### **1. Using Groovy in Jenkins Pipelines**

Jenkins supports two types of pipelines:

1. **Declarative Pipeline** – Uses a structured Groovy DSL.
2. **Scripted Pipeline** – Uses full Groovy syntax with more flexibility.

#### **Declarative Pipeline Example (Simpler)**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}
```

#### **Scripted Pipeline Example (More Control)**

```groovy
node {
    stage('Build') {
        echo 'Building the project...'
    }
    stage('Test') {
        echo 'Executing tests...'
    }
    stage('Deploy') {
        echo 'Deploying to production...'
    }
}
```

---

### **2. Jenkins Script Console**

Jenkins provides a **Script Console** where administrators can execute Groovy scripts for automation and system management.

- Navigate to **Jenkins Dashboard → Manage Jenkins → Script Console**
- Run a script like:

```groovy
println "Hello from Jenkins!"
```

Example: Listing all Jenkins jobs

```groovy
Jenkins.instance.getAllItems().each { println it.name }
```

---

### **3. Using Groovy in Shared Libraries**

Jenkins allows **Shared Libraries** written in Groovy to be used across multiple pipelines.

- Define a shared library in Jenkins
- Use it in `Jenkinsfile`:

```groovy
@Library('my-shared-library') _
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                myCustomStep()
            }
        }
    }
}
```

---

### **4. Jenkins Job DSL Plugin (Groovy-Based)**

The **Jenkins Job DSL Plugin** allows defining jobs programmatically using Groovy.

Example: Defining a job with Groovy DSL:

```groovy
job('MyNewJob') {
    description('This is a generated job')
    scm {
        git('https://github.com/user/repo.git')
    }
    triggers {
        cron('H/5 * * * *')
    }
    steps {
        shell('echo Hello, World!')
    }
}
```

---

### **Conclusion**

Groovy is deeply integrated into Jenkins for scripting, automation, and pipeline creation. It is used in **Jenkins Pipelines, Script Console, Shared Libraries, and Job DSL** to streamline CI/CD workflows. Learning Groovy helps in customizing and extending Jenkins functionalities efficiently.

![[Pasted image 20250324205810.png]]

___
![[Pasted image 20250324213744.png]]
![[Pasted image 20250324213750.png]]
