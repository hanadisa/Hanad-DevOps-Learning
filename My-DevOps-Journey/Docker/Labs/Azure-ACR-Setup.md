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

## 📌 **Prerequisites**
Before I began, I made sure I had the following:
- **Azure CLI** installed (`az --version` to check)
- **Docker** installed (`docker --version` to check)
- An **Azure Subscription** (Sign up [here](https://azure.microsoft.com/en-gb/free/) if you don’t have one)

---

## 🔹 **Step 1: Manually Creating Azure Container Registry (ACR)**
Instead of using the CLI, I created the ACR manually through the **Azure Portal**:

1. Navigated to **Azure Portal** ([portal.azure.com](https://portal.azure.com/)).
2. Searched for **Container Registry** and clicked **Create**.
3. Filled in the necessary details:
   - **Resource Group**: `RG1`
   - **Registry Name**: `sampleregistry101`
   - **SKU**: `Basic`
4. Clicked **Review + Create**, then **Create**.

✅ **Screenshot of Successful ACR Creation:**
![ACR Created](./screenshots/acr-created.png)

---
