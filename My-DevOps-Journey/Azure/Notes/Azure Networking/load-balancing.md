# Load Balancing in Azure

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Azure/Notes/Images/load-balancer.png?raw=true" alt="Azure Load Balancing Diagram" width="700"/>

## 📌 Overview  
Load balancing is **essential** in cloud computing for ensuring **high availability, scalability, and fault tolerance**. In **Azure**, load balancing services distribute **incoming network traffic** across multiple resources, preventing single points of failure and optimizing performance.  

Azure provides **different types of load balancers** based on workload requirements, from **network layer (Layer 4) traffic distribution to application layer (Layer 7) intelligent routing**.

## 🔹 Key Features  
- **High Availability** – Ensures services remain operational even if individual resources fail.  
- **Scalability** – Distributes traffic across multiple instances to handle varying workloads.  
- **Traffic Distribution** – Balances requests based on predefined algorithms.  
- **Health Probing** – Continuously monitors resource availability and removes unhealthy instances.  
- **Global and Regional Balancing** – Manage traffic distribution across multiple Azure regions.  

---

## 🔹 Types of Load Balancers in Azure  

### **1️⃣ Azure Load Balancer (Layer 4 - TCP/UDP)**
A **network-level load balancer** that distributes traffic **across virtual machines (VMs) in a virtual network**. It operates at **Layer 4 (Transport Layer - TCP/UDP)** and supports:  
✅ **Inbound and outbound traffic balancing**.  
✅ **Automatic failover** when an instance becomes unhealthy.  
✅ **Support for virtual machine scale sets (VMSS)**.  

📌 **When to Use Azure Load Balancer?**  
✔ Distributing traffic to backend **VMs within a single region**.  
✔ Load balancing **internal or external-facing** applications.  
✔ Ensuring **high availability** for virtual machine scale sets.  

---

### **2️⃣ Azure Application Gateway (Layer 7 - HTTP/HTTPS)**
A **web traffic load balancer** that operates at **Layer 7 (Application Layer)**. It provides **intelligent routing** for **HTTP/HTTPS-based workloads** and integrates **Web Application Firewall (WAF) for security**.  

📌 **Key Features:**  
✅ **URL-Based Routing** – Direct requests to different backends based on URL path.  
✅ **SSL Termination** – Offloads SSL decryption to improve backend performance.  
✅ **Web Application Firewall (WAF)** – Protects web applications from common vulnerabilities.  
✅ **Autoscaling** – Scales based on traffic demand automatically.  

📌 **When to Use Azure Application Gateway?**  
✔ Hosting **multiple web applications** behind a single entry point.  
✔ Protecting applications from **web-based attacks (WAF integration)**.  
✔ Distributing traffic based on **URL paths (e.g., `/api`, `/login`, `/static`)**.  

---

### **3️⃣ Azure Traffic Manager (DNS-Based Global Load Balancing)**
A **global DNS load balancer** that directs users to the **nearest available Azure region** based on policies. It helps optimize latency and ensures high availability across **multiple Azure regions**.  

📌 **Key Features:**  
✅ **Geographical Routing** – Directs traffic based on user location.  
✅ **Performance-Based Routing** – Routes users to the lowest-latency region.  
✅ **Failover Support** – Redirects traffic when an entire region goes down.  
✅ **Multi-Cloud Support** – Can manage endpoints **outside Azure** as well.  

📌 **When to Use Azure Traffic Manager?**  
✔ Managing **global applications** that serve users from multiple regions.  
✔ Optimizing **latency** by routing users to the nearest available region.  
✔ Providing **regional failover mechanisms** in case of data center outages.  

---

### **4️⃣ Azure Front Door (Global Layer 7 Load Balancer)**
A **global web application delivery service** that provides **load balancing, acceleration, and security** for internet-facing applications.  

📌 **Key Features:**  
✅ **HTTP/HTTPS Load Balancing** – Optimizes global traffic distribution.  
✅ **Caching & Acceleration** – Uses edge caching to **reduce latency**.  
✅ **WAF Integration** – Protects against **DDoS attacks & web vulnerabilities**.  
✅ **Global Traffic Routing** – Uses AI-based traffic optimization.  

📌 **When to Use Azure Front Door?**  
✔ Speeding up **internet-facing applications** using edge caching.  
✔ Distributing traffic **across multiple Azure regions**.  
✔ Enhancing **security with DDoS protection & WAF**.  

---

## 🛠️ Example: Creating an Azure Load Balancer Using Azure CLI  
To create a **basic Azure Load Balancer** and distribute traffic across **VMs**, use the following commands:

```sh
# Create a public IP for the Load Balancer
az network public-ip create \
  --name MyPublicIP \
  --resource-group MyResourceGroup \
  --allocation-method Static

# Create the Load Balancer
az network lb create \
  --name MyLoadBalancer \
  --resource-group MyResourceGroup \
  --location eastus \
  --sku Standard \
  --public-ip-address MyPublicIP \
  --frontend-ip-name MyFrontEnd \
  --backend-pool-name MyBackEndPool

# Create a health probe to monitor VM health
az network lb probe create \
  --resource-group MyResourceGroup \
  --lb-name MyLoadBalancer \
  --name MyHealthProbe \
  --protocol Tcp \
  --port 80

# Create a load balancing rule
az network lb rule create \
  --resource-group MyResourceGroup \
  --lb-name MyLoadBalancer \
  --name HTTPRule \
  --protocol Tcp \
  --frontend-port 80 \
  --backend-port 80 \
  --frontend-ip-name MyFrontEnd \
  --backend-pool-name MyBackEndPool
```


