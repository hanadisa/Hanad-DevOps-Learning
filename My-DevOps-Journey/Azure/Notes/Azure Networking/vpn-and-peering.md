# VPN & VNet Peering in Azure

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Azure/Notes/Images/vnet-peering.png?raw=true" alt="Azure VPN and VNet Peering Diagram" width="700"/>

## 📌 Overview  
In **Azure Networking**, **VPN Gateway and VNet Peering** are key solutions for **secure connectivity** between on-premises environments, Azure Virtual Networks (VNets), and even different cloud providers.  

- **VPN Gateway** enables **secure site-to-site or point-to-site VPN connections** between Azure and on-premises networks.  
- **VNet Peering** connects multiple Azure VNets, allowing resources to communicate **privately with low latency and high bandwidth**.  

## 🔹 Key Features  
- **Secure Hybrid Connectivity** – Connect on-premises networks securely to Azure.  
- **Private Communication Between VNets** – Share resources **without using public IPs**.  
- **Low-Latency, High-Bandwidth Peering** – Enables **fast** inter-VNet communication.  
- **Global Peering** – Connect VNets across **different Azure regions**.  
- **Cost-Effective Networking** – Avoid traffic costs by routing within Azure.  

---

## 🔹 Azure VPN Gateway

### 📌 Overview  
**VPN Gateway** is a **cloud-based gateway** that establishes **encrypted tunnels** for secure communication between **on-premises networks and Azure VNets**.

### 🔹 Types of Azure VPNs  
1️⃣ **Site-to-Site (S2S) VPN** – Connects **on-premises networks** to Azure using **IPsec/IKE VPN tunnels**.  
2️⃣ **Point-to-Site (P2S) VPN** – Allows **individual devices** (e.g., laptops) to securely connect to Azure VNets.  
3️⃣ **ExpressRoute** – Provides a **private, high-speed** connection between **on-premises data centers and Azure** (bypasses the public internet).  

### 📌 When to Use VPN Gateway?  
✔ Connecting **on-premises data centers** securely to Azure.  
✔ Enabling **remote workers** to access Azure **via Point-to-Site VPN**.  
✔ Creating **a backup connection** for ExpressRoute.  
✔ Connecting **branch offices** securely to Azure services.  

---

## 🔹 VNet Peering

### 📌 Overview  
**VNet Peering** allows **private communication** between multiple **Azure Virtual Networks (VNets)** without using public internet routing.  

### 🔹 Key Capabilities  
- ✅ **Low-Latency Communication** – Near **real-time** network performance.  
- ✅ **Cross-Region Peering** – Connect VNets **across different Azure regions**.  
- ✅ **Full IP Address Transparency** – Resources communicate **without NAT or public IPs**.  
- ✅ **Shared Services Model** – Centralize common resources (e.g., firewalls, DNS, monitoring) across multiple VNets.  

### 📌 When to Use VNet Peering?  
✔ Connecting **two or more VNets** in the same or different regions.  
✔ **Enabling communication** between microservices or multi-tier applications.  
✔ **Sharing centralized resources** like firewalls and security appliances.  
✔ Avoiding **performance bottlenecks** in hub-and-spoke networking architectures.  

---

## 🛠️ Configuring VPN & VNet Peering Using Azure CLI  

### **1️⃣ Create a Virtual Network Gateway for VPN**
```sh
# Create a public IP for the VPN Gateway
az network public-ip create \
  --name MyVpnGatewayIP \
  --resource-group MyResourceGroup \
  --allocation-method Dynamic
```

### 2️⃣ Create a Virtual Network Gateway for VPN
```sh
az network vnet-gateway create \
  --name MyVpnGateway \
  --resource-group MyResourceGroup \
  --location eastus \
  --public-ip-address MyVpnGatewayIP \
  --vnet MyVNet \
  --gateway-type Vpn \
  --vpn-type RouteBased \
  --sku VpnGw2 \
  --asn 65515
```

### 3️⃣ Create a VNet peering connection from VNet1 to VNet2
```sh
az network vnet peering create \
  --name MyVNetPeering \
  --resource-group MyResourceGroup \
  --vnet-name MyVNet1 \
  --remote-vnet MyVNet2 \
  --allow-vnet-access
```
