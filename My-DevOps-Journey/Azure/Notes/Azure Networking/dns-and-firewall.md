# DNS & Firewalls in Azure

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Azure/Notes/Images/azurednsfirewall.png?raw=true" width="700"/>

## 📌 Overview  
**DNS (Domain Name System) and Firewalls** play a crucial role in **network security and traffic management** in Azure.  

- **Azure DNS** ensures reliable name resolution for applications by **mapping domain names to IP addresses**.  
- **Azure Firewall** provides **network-level security** by enforcing **rules for inbound and outbound traffic**, protecting cloud resources from unauthorized access.  

## 🔹 Key Features  
- **DNS Resolution** – Converts human-readable domain names into IP addresses.  
- **Custom Domain Management** – Host and manage custom domains in Azure DNS.  
- **Firewall Traffic Filtering** – Control traffic based on IP addresses, ports, and protocols.  
- **Threat Intelligence** – Detect and block traffic from malicious IPs.  
- **Integration with NSGs** – Strengthen network security with layered protection.  

---

## 🔹 Azure DNS (Domain Name System)

### 📌 Overview  
Azure DNS is a **fully managed DNS service** that provides **fast and reliable domain name resolution** within Azure.  

### 🔹 Key Capabilities  
- ✅ **Host custom domains** without managing DNS infrastructure.  
- ✅ **Integrate with Azure services** (e.g., App Services, VMs).  
- ✅ **Use Private DNS Zones** for **internal name resolution** in Azure.  
- ✅ **Fast, global resolution** with **low-latency performance**.  

### 🔹 Types of DNS in Azure  
1️⃣ **Public DNS Zones** – Resolve domains for **internet-facing applications**.  
2️⃣ **Private DNS Zones** – Resolve domains **within an Azure Virtual Network (VNet)**.  

### 📌 When to Use Azure DNS?  
✔ Hosting a **custom domain** for an Azure Web App.  
✔ Setting up **internal DNS resolution** for private resources.  
✔ Enabling **service discovery** for microservices inside a VNet.  

---

## 🔹 Azure Firewall (Network Security)

### 📌 Overview  
Azure Firewall is a **cloud-based, fully managed network security service** that **protects Azure resources** by filtering traffic based on rules.  

### 🔹 Key Capabilities  
- ✅ **Stateful Packet Inspection** – Tracks connections for enhanced security.  
- ✅ **Application & Network Filtering** – Control access based on ports and protocols.  
- ✅ **Threat Intelligence** – Blocks traffic from known malicious IPs.  
- ✅ **High Availability** – Scales automatically to meet demand.  
- ✅ **Integration with NSGs & Route Tables** – Provides **layered security**.  

### 📌 When to Use Azure Firewall?  
✔ **Protecting Azure VMs & services** from external attacks.  
✔ **Filtering outbound traffic** to **allow only whitelisted destinations**.  
✔ **Enforcing security policies** at the **network level**.  
✔ **Combining with NSGs** for **fine-grained control over traffic flows**.  

---

## 🛠️ Configuring Azure DNS & Firewall Using Azure CLI  

### 1️⃣ Create an Azure DNS Zone
```sh
# Create a DNS zone for a custom domain
az network dns zone create \
  --name example.com \
  --resource-group MyResourceGroup
```

### 2️⃣ Create an Azure Firewall
```sh
az network firewall create \
  --name MyAzureFirewall \
  --resource-group MyResourceGroup \
  --location eastus \
  --sku Standard
```

### 3️⃣ Create a firewall rule to allow web traffic
```sh
az network firewall rule-collection-group rule add \
  --resource-group MyResourceGroup \
  --firewall-name MyAzureFirewall \
  --collection-name AllowWebTraffic \
  --rule-name AllowHTTP \
  --action Allow \
  --priority 100 \
  --source-addresses '*' \
  --destination-addresses '*' \
  --destination-ports 80 443 \
  --protocols TCP
```

