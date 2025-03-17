# Virtual Networks (VNets)

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Azure/Notes/Images/Virtual-Network.png?raw=true" alt="Azure Virtual Network Diagram" width="600"/>

## 📌 Overview  
A **Virtual Network (VNet)** in Azure is the foundation of cloud networking, enabling **secure communication** between Azure resources. It allows for **custom IP address allocation, subnetting, access control, and hybrid connectivity**, making it essential for **cloud applications, microservices, and enterprise networking**.  

VNets provide **isolation and segmentation**, ensuring that Azure resources can only communicate within defined network boundaries unless explicitly allowed.  

## 🔹 Key Features  
- **Network Isolation** – Each VNet is isolated from others by default.  
- **Custom IP Addressing** – Define private IP ranges using **CIDR notation**.  
- **Subnetting** – Segment network resources for better traffic management.  
- **Security & Access Control** – Use **NSGs (Network Security Groups)** to control inbound/outbound traffic.  
- **Hybrid Connectivity** – Extend on-premises networks using **VPN Gateway** or **ExpressRoute**.  
- **Scalability & Flexibility** – Support for **multi-tier architectures and Kubernetes networking**.  

## 💡 When to Use Virtual Networks?  
VNets are **crucial** when designing **secure, scalable cloud architectures**. Some key use cases include:  

✅ **Deploying Cloud Applications** – Isolate workloads for security and efficiency.  
✅ **Microservices & Containers** – Secure Kubernetes networking for **Azure Kubernetes Service (AKS)**.  
✅ **Hybrid Cloud Deployments** – Connect Azure to **on-premises networks via VPN/ExpressRoute**.  
✅ **Multi-Tier Architectures** – Separate web, app, and database layers using **subnets**.  
✅ **Secure Internal Communication** – Protect workloads using **private IP addressing** and **NSGs**.  

## 🔹 Virtual Network Addressing  
Each **VNet has a defined address space** using **CIDR (Classless Inter-Domain Routing)** notation, ensuring proper IP allocation.  

📌 **Example Address Space & Subnet Configuration:**  
- **VNet Address Space**: `10.0.0.0/16` (**65,536** available IPs)  
- **Subnet A**: `10.0.1.0/24` (**256** available IPs)  
- **Subnet B**: `10.0.2.0/24` (**256** available IPs)  

A **best practice** is to **allocate subnets based on workload type** (e.g., Web, App, Database) to improve security and traffic control.  

## 🏢 Real-World Use Case: VNet for an Enterprise Application  
A **company hosting an internal web application** in Azure needs a **secure and scalable network** to manage traffic:  

1️⃣ **Frontend Web Servers** in **Subnet A** – Public access via **Azure Load Balancer**.  
2️⃣ **Application Layer** in **Subnet B** – Internal access only, restricted via **NSGs**.  
3️⃣ **Database Layer** in **Subnet C** – Fully private, only accessible to application servers.  

By using a **VNet with multiple subnets**, the company ensures **security, performance, and controlled access** to sensitive data.  

## 🛠️ Example: Creating a VNet Using Azure CLI  
To create a **Virtual Network (VNet)** with an **address space and subnet**, use the following **Azure CLI** commands:  

```sh
# Create a resource group
az group create --name MyResourceGroup --location eastus

# Create a virtual network with an address space
az network vnet create \
  --name MyVNet \
  --resource-group MyResourceGroup \
  --location eastus \
  --address-prefix 10.0.0.0/16

# Create a subnet within the VNet
az network vnet subnet create \
  --name MySubnet \
  --resource-group MyResourceGroup \
  --vnet-name MyVNet \
  --address-prefix 10.0.1.0/24
```
