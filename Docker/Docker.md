
Docker is used to **package, distribute, and run applications in isolated environments called containers**. It ensures that an application runs the same way on different machines, avoiding issues like "it works on my machine but not on yours."
It packs all the necessary dependencies in a box and helps it to parcel to different clients so they can unbox and use it

### **From my understanding about Docker

Imagine you are developing a **Java-based banking application** on your laptop. It requires **Java, MySQL, and some libraries**. Instead of manually installing everything on every machine where you want to run the application, you can create a **Docker container** that includes the application and all its dependencies.
Now, you can run this container **anywhere**—on another developer’s computer, a test server, or in the cloud—without worrying about missing dependencies or configuration issues.

### **Differences Between Containers and VMs:**
Now even VM's behave almost the same way, it is used to run other OS's in the computer in isolation.
1. **VMs have a full operating system** (OS) inside them, including a separate kernel, making them heavy and slow to start.
2. **Containers share the host OS kernel**, so they are lightweight and start almost instantly.
3. **VMs need more system resources**, while **containers use less memory and CPU**.

## Commands I learnt for using docker
---
### **1. Docker Container Management**

- `docker ps` → List running containers.
- `docker ps -a` → List all containers (including stopped ones).
- `docker run <image>` → Run a container from an image.
- `docker run -d <image>` → Run a container in detached mode (background).
- `docker run -it <image> /bin/bash` → Run a container interactively with a shell.
- `docker start <container_id>` → Start a stopped container.
- `docker stop <container_id>` → Stop a running container.
- `docker restart <container_id>` → Restart a container.
- `docker kill <container_id>` → Forcefully stop a running container.
- `docker rm <container_id>` → Remove a stopped container.
- `docker logs <container_id>` → View the logs of a container.
- `docker exec -it <container_id> /bin/bash` → Access a running container's shell.
- `docker inspect <container_id>` → Get detailed information about a container.

---

### **2. Docker Image Management**

- `docker images` → List all available images.
- `docker pull <image>` → Download an image from Docker Hub.
- `docker push <image>` → Push an image to Docker Hub.
- `docker build -t <image_name> .` → Build an image from a Dockerfile.
- `docker tag <image> <new_image_name>` → Tag an image with a new name.
- `docker rmi <image>` → Remove an image.
- `docker history <image>` → Show the history of an image.
- `docker inspect <image>` → Get detailed information about an image.

---
### **4. Docker Volume Management**
- `docker volume create <volume_name>` → Create a new volume.
- `docker volume ls` → List all volumes.
- `docker volume inspect <volume_name>` → Get details of a volume.
- `docker volume rm <volume_name>` → Remove a volume.
---
### **6. Docker Compose (for Multi-Container Applications)**

Docker Compose is a tool that allows you to define and manage multi-container Docker applications using a YAML configuration file (`docker-compose.yml`). Instead of running multiple `docker run` commands manually, you can define all services, networks, and volumes in one file and start them with a single command.

- `docker-compose up` → Start services defined in `docker-compose.yml`.
- `docker-compose down` → Stop and remove services.
- `docker-compose ps` → List running services.
- `docker-compose logs` → View logs of services.
- `docker-compose restart` → Restart all services.
---

### **7. Docker System Management**

- `docker system df` → Show disk usage by Docker objects.
- `docker system prune` → Remove unused containers, networks, and images.

___
## What is the difference between Images and Containers

- Images are nothing but a blueprint or templates for a container, the images are read only and can be configured only once, they are reusable, they are stored in docker hub, they contain all the dependencies and a base OS
- Docker containers are nothing but the running instances of a docker image, it is the actual execution of the application in an isolated environment
#### **1. What is a Docker Image?**
A **Docker image** is a **blueprint** or **template** used to create containers. It contains:

- The **application code**
- All **dependencies** (libraries, runtimes, configurations)
- A **base operating system** (like Ubuntu, Alpine, etc.)
- Any **customized settings**


#### **2. What is a Docker Container?**

A **Docker container** is a **running instance** of a Docker image. It is the **actual execution** of the application inside an isolated environment.

- **Based on Images** → Containers are created from images.
- **Read-Write Layer** → Containers can modify their filesystem while running.
- **Isolated but Share the Host Kernel** → Unlike Virtual Machines, containers share the host OS kernel but have their own filesystem, processes, and network.
- **Temporary (Ephemeral) or Persistent** → Containers can be deleted after use or configured to keep data.
___

## In development
- we make our custom image in which we have the tools and dependencies installed and we can tell other team members to use this images, we can publish this image in docker hub and people can use these images in their container

### **What is a Dockerfile?**

A **Dockerfile** is a text file that contains a set of instructions for building a **Docker image**. It acts as a **blueprint** for creating lightweight, portable, and consistent environments.
So if we have an application, if we want to convert that application into an image we just have to include a docker file into it.
Once our image is created we can upload it to dicker hub and then developers can pull our images form there. To pull images we can use the `docker pull` command
We can push our image to docker hub using `docker push` command

![[Pasted image 20250330145922.png]]
![[Pasted image 20250330152455.png]]
![[Pasted image 20250330152548.png]]
![[Pasted image 20250330153024.png]]
![[Pasted image 20250330153137.png]]

Instead of manually setting up software dependencies, a **Dockerfile automates this process**.

---

### **How Does a Dockerfile Work?**

1. **You write a Dockerfile** with instructions on how to set up an environment.
2. **Docker builds an image** from the Dockerfile.
3. **You run a container** from the image.

![[Pasted image 20250330151341.png]]
![[Pasted image 20250330151409.png]]
![[Pasted image 20250330151429.png]]
![[Pasted image 20250330151511.png]]


___
### **What is Docker Compose?**

**Docker Compose** is a tool that allows you to **define and run multi-container Docker applications** using a simple **YAML file (`docker-compose.yml`)**. Instead of manually running multiple `docker run` commands, you can define everything in **one file** and start everything with a single command.
#### **Scenario: Running a Website with a Database**

Imagine you are developing a simple **To-Do List web app** that consists of:

1. **A Python Flask web server** to handle user requests.
2. **A MySQL database** to store the to-do items.

Instead of manually starting two separate containers (one for Flask and one for MySQL) and linking them together, **Docker Compose** makes this process easier by defining everything in a `docker-compose.yml` file.

---

### **Why Use Docker Compose?**

- Without Docker Compose:
    - You’d need to run multiple `docker run` commands.
    - Manually link containers and manage networks.
    - Set up environment variables manually.
- With Docker Compose:
    - Define everything in one YAML file.
    - Start everything with **one command**: `docker-compose up`.

---

