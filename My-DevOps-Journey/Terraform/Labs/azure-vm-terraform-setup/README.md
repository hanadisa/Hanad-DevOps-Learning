# Azure VM Terraform Setup 💻

This lab demonstrates how to use **Terraform** to provision a basic **Linux Virtual Machine** on **Microsoft Azure**.  
It includes a minimal configuration to get you started with Infrastructure as Code (IaC) on Azure.

---

## 🚀 What This Setup Includes

- ✅ Resource Group  
- ✅ Virtual Network and Subnet  
- ✅ Network Interface (NIC)  
- ✅ Linux Virtual Machine (Ubuntu 18.04 LTS)  
- ✅ Admin password authentication (for testing)  
- ✅ Terraform state tracking files

---

## 📁 Project Structure

```bash
azure-vm-terraform-setup/
├── .terraform/                    # Local plugin cache (auto-generated)
├── .terraform.lock.hcl           # Provider dependency lock file
├── provider.tf                   # Provider configuration (AzureRM)
├── vm.tf                         # Main infrastructure config (VNet, NIC, VM, etc.)
├── terraform.tfstate             # Terraform-managed state file
├── terraform.tfstate.backup      # Backup state file
└── README.md                     # Project documentation
```

---

## Prerequisites

- An Azure account with permissions to create resources
- [Terraform installed](https://developer.hashicorp.com/terraform/downloads)
- Azure CLI authenticated (`az login`)
- SSH installed (for key generation and VM access)

---

## 🛠️ How to Deploy

1. **Initialize Terraform**  
   ```bash
   terraform init
   ```
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Terraform/Labs/Images/tf-init.png?raw=true" width="500">

2. **Preview the infrastructure plan**  
   ```bash
   terraform plan
   ```
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Terraform/Labs/Images/tf-plan.png?raw=true" width="500">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Terraform/Labs/Images/tf-plan2.png?raw=true" width="500">

3. **Apply the configuration**  
   ```bash
   terraform apply
   ```
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Terraform/Labs/Images/tf-apply.png?raw=true" width="500">
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Terraform/Labs/Images/confirmation.png?raw=true" width="500">

4. **To destroy everything when done**  
   ```bash
   terraform destroy
   ```
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Terraform/Labs/Images/tf-destroy.png?raw=true" width="500">

---

## 📝 Notes

- The VM uses admin username + password for simplicity — in production, use SSH key pairs.
- The setup uses Ubuntu Server 18.04 LTS and the Standard_B1s VM size (cost-effective).
- You can refactor this into a module or extend with other Azure services.

---

## 📸 VM Creation Confirmation

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Terraform/Labs/Images/vm-creation.png?raw=true" width="500">

---

## 💡 Key Takeways

- Understand how Terraform provisions infrastructure in Azure
- Practice defining infrastructure as code
- Build foundational DevOps cloud experience

---

## 📌 Tags

`#Terraform` `#Azure` `#DevOps` `#InfrastructureAsCode` `#CloudComputing`
