# Network Security in Azure

<img src="https://raw.githubusercontent.com/hanadisa/Hanad-DevOps-Learning/refs/heads/main/My-DevOps-Journey/Azure/Notes/Images/azurenetsecurity.webp" alt="Azure Network Security Diagram" width="700"/>

## 📌 Overview  
Security is a **critical** component of cloud networking. In **Azure**, network security is enforced using **Network Security Groups (NSGs) and Application Security Groups (ASGs)** to control **traffic flow, enforce security policies, and protect workloads** from unauthorized access.  

NSGs and ASGs provide **granular control** over inbound and outbound traffic, ensuring that **only approved connections** can reach specific Azure resources.

## 🔹 Key Features  
- **Traffic Filtering** – Define **rules** to allow or deny network traffic.  
- **Subnet-Level & NIC-Level Security** – Apply security rules at different levels.  
- **Granular Access Control** – Use **ASGs** to group VMs dynamically instead of managing individual IPs.  
- **Inbound & Outbound Rules** – Control network flow at the **port, protocol, and address** level.  
- **Integration with Azure Firewall** – Strengthen security by enforcing **centralized network policies**.  

## 💡 When to Use NSGs & ASGs?  
✅ **Restricting access to sensitive resources** (e.g., databases).  
✅ **Controlling traffic flow between subnets** in multi-tier applications.  
✅ **Minimizing attack surface** by only allowing required ports and IPs.  
✅ **Segmenting workloads** without managing individual IP addresses.  
✅ **Applying security at scale** for VM-based workloads using ASGs.  

## 🔹 Understanding Network Security Groups (NSGs)  
A **Network Security Group (NSG)** acts as a **virtual firewall** that filters network traffic based on **rules**.  

📌 **NSG Rules consist of:**  
- **Priority** – Rules are evaluated in order (lower numbers have higher priority).  
- **Source & Destination** – Define where traffic is coming from and going to.  
- **Protocol** – Supports **TCP, UDP, ICMP, and Any**.  
- **Port Range** – Specify allowed/disallowed ports (e.g., `22` for SSH, `443` for HTTPS).  
- **Action** – Either **Allow** or **Deny** the traffic.  

### 🔹 Default NSG Rules  
Azure automatically applies **default NSG rules** to allow core networking services:  
- **Allow VNet Inbound/Outbound** – Enables internal VNet communication.  
- **Allow Load Balancer Traffic** – Ensures Azure Load Balancer health checks work.  
- **Deny All Inbound by Default** – Blocks external traffic unless explicitly allowed.  

🚀 **Best Practices for NSGs**:  
- Use **Deny All by Default** and explicitly allow required traffic.  
- Apply **NSGs at the subnet level** to enforce broad policies.  
- Avoid using **ANY** in security rules—always specify **specific ports and IPs**.  

---

## 🔹 Understanding Application Security Groups (ASGs)  
An **Application Security Group (ASG)** simplifies security management by allowing **VMs to be grouped dynamically** instead of using individual IP addresses.  

### 🔹 How ASGs Work  
- Instead of defining security rules **per VM**, **ASGs allow you to group resources** by application role.  
- **Rules reference ASGs instead of individual IPs**, making security **more scalable**.  

📌 **Example Use Case**:  
Instead of managing **IP addresses manually**, an ASG-based NSG rule can allow:  
- **Web Servers ASG** → Allow HTTP/HTTPS (`80, 443`)  
- **App Servers ASG** → Allow API Calls from **Web Servers ASG** (`5000`)  
- **Database ASG** → Only allow traffic from **App Servers ASG** (`1433`)  

🚀 **Best Practices for ASGs**:  
- **Use ASGs instead of individual VM IPs** to simplify rule management.  
- **Combine ASGs with NSGs** to create flexible **role-based security**.  
- **Tag resources logically** (e.g., `web-tier`, `db-tier`, `api-tier`) for easier automation.  

---

## 🛠️ Example: Creating an NSG and ASG Using Azure CLI  
To create a **Network Security Group (NSG)** and an **Application Security Group (ASG)** in **Azure CLI**, use the following commands:  

```sh
# Create a Network Security Group (NSG)
az network nsg create \
  --name MyNSG \
  --resource-group MyResourceGroup \
  --location eastus

# Create an Application Security Group (ASG)
az network asg create \
  --name WebAppASG \
  --resource-group MyResourceGroup \
  --location eastus

# Create a security rule in the NSG to allow HTTP traffic for ASG
az network nsg rule create \
  --resource-group MyResourceGroup \
  --nsg-name MyNSG \
  --name AllowHTTP \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefix '*' \
  --source-asg WebAppASG \
  --destination-port-range 80

# Associate the ASG with a VM's NIC
az network nic update \
  --name MyVMNIC \
  --resource-group MyResourceGroup \
  --add ipConfigurations[0].ApplicationSecurityGroups id="/subscriptions/{subscription-id}/resourceGroups/MyResourceGroup/providers/Microsoft.Network/applicationSecurityGroups/WebAppASG"
```


