# Subnetting and Routes

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Azure/Notes/Images/routing-subnets.jpg?raw=true" alt="Azure Subnetting and Routing Diagram" width="600"/>

## 📌 Overview  
In **Azure Virtual Networks (VNets)**, **subnetting and routing** allow for efficient **network segmentation, traffic management, and security enforcement**.  

- **Subnets** divide a **VNet into smaller network segments**, helping organize workloads and enforce network policies.  
- **Routing** determines **how traffic flows** within a VNet and to external networks using **system-defined and custom routes**.  

Proper subnetting and routing help **optimize security, control network traffic, and improve scalability** for cloud workloads.  

## 🔹 Key Features  
- **Subnet Isolation** – Secure workloads by assigning them to different subnets.  
- **Traffic Management** – Control **internal and external communication** within Azure.  
- **Custom Routing** – Define specific routes for **on-premises and hybrid connectivity**.  
- **Default System Routes** – Azure automatically manages core routing without manual setup.  
- **Subnet-Level NSGs** – Apply different **security rules** to separate application layers.  

## 💡 When to Use Subnetting and Routing?  
Subnetting and custom routing are **essential** for:  

✅ **Multi-Tier Applications** – Separating frontend, backend, and database layers.  
✅ **Security Hardening** – Restricting communication between **sensitive workloads**.  
✅ **Hybrid Connectivity** – Controlling traffic between **Azure and on-premises environments**.  
✅ **Microservices Architectures** – Organizing services across different **subnets** for efficiency.  
✅ **Network Traffic Optimization** – Directing **traffic through VPNs, ExpressRoute, or firewalls**.  

## 🔹 Understanding Subnets in Azure  
A **subnet** is a logical division within a **VNet**, assigned its own **CIDR block** for IP allocation.  

📌 **Example of Subnet Allocation in a VNet:**  
- **VNet Address Space**: `10.0.0.0/16` (**65,536 IPs available**)  
- **Subnet A (Frontend)**: `10.0.1.0/24` (**256 IPs**)  
- **Subnet B (Backend)**: `10.0.2.0/24` (**256 IPs**)  
- **Subnet C (Database)**: `10.0.3.0/24` (**256 IPs**)  

🚀 **Best Practices for Subnetting**:  
- Assign **specific application layers** (Web, App, Database) to separate subnets.  
- Use **NSGs at the subnet level** to enforce **security policies**.  
- Avoid **overlapping IP ranges** if connecting to on-premises networks.  

## 🔹 Routing in Azure  
Routing determines how network **traffic flows between subnets, VNets, and external networks**.  

Azure **automatically creates system-defined routes**, but you can also configure **custom routes** using **Route Tables**.  

🔹 **Types of Routing in Azure**:  
1️⃣ **System-Defined Routes** – Automatically created for **internal Azure traffic**.  
2️⃣ **User-Defined Routes (UDRs)** – Custom routes to **override system routes**.  
3️⃣ **BGP Routes** – Used in **VPN Gateway & ExpressRoute** for dynamic routing.  

📌 **Example of System vs. Custom Routes:**  
- **System Route:** Allows all traffic within a **VNet** (`10.0.0.0/16 → Virtual Network`).  
- **Custom Route:** Directs **internet-bound** traffic through a **firewall or VPN**.  

🚀 **Best Practices for Routing**:  
- Use **custom route tables** to enforce traffic flow policies.  
- Direct traffic **through an Azure Firewall or VPN Gateway** for secure external communication.  
- **Avoid asymmetric routing** by ensuring **both inbound & outbound paths are defined**.  

## 🛠️ Example: Creating a Subnet and Custom Route Using Azure CLI  
To create a **subnet** and a **custom route** in Azure, use the following **CLI commands**:

```sh
# Create a subnet inside an existing VNet
az network vnet subnet create \
  --name BackendSubnet \
  --resource-group MyResourceGroup \
  --vnet-name MyVNet \
  --address-prefix 10.0.2.0/24

# Create a route table
az network route-table create \
  --name MyRouteTable \
  --resource-group MyResourceGroup \
  --location eastus

# Add a custom route (forcing traffic through a firewall)
az network route-table route create \
  --name InternetRoute \
  --resource-group MyResourceGroup \
  --route-table-name MyRouteTable \
  --address-prefix 0.0.0.0/0 \
  --next-hop-type VirtualAppliance \
  --next-hop-ip-address 10.0.0.4

# Associate the route table with a subnet
az network vnet subnet update \
  --name BackendSubnet \
  --resource-group MyResourceGroup \
  --vnet-name MyVNet \
  --route-table MyRouteTable
```
