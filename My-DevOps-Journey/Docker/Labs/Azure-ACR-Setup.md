# 🚀 Setting Up Azure Container Registry (ACR) & Pushing Docker Images  

## 📌 Introduction  
As part of my **containerization learning journey**, I explored how to **set up Azure Container Registry (ACR)** to store and manage Docker images. This documentation walks through the exact steps I took to configure **ACR**, push container images, and pull them for deployment in a cloud-native environment.  

By leveraging **ACR**, I can securely store, manage, and deploy containerized applications while integrating with **Kubernetes (AKS)** and CI/CD pipelines.


## 🔹 Why I Chose ACR  
I wanted a **private, secure** registry to store and manage my Docker images within **Azure**. Compared to public registries like **Docker Hub**, **ACR integrates seamlessly** with **Azure Kubernetes Service (AKS)**, **Azure DevOps**, and **other cloud-native services**.  

### 🚀 **What I Achieved in This Lab**
✅ Set up **Azure Container Registry (ACR)**  
✅ Built and **tagged Docker images**  
✅ Pushed images to **ACR**  
✅ Pulled images from **ACR** for deployment  

---

## 🛠 Prerequisites  
Before starting, I ensured I had the following:  
- ✅ **An active Azure subscription** (Pay-As-You-Go)  
- ✅ **Azure CLI installed** ([Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli))  
- ✅ **Docker installed** ([Install Docker](https://docs.docker.com/get-docker/))  
