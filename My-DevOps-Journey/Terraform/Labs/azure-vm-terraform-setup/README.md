# Azure VM Terraform Setup

This lab demonstrates how to use **Terraform** to provision a basic **Linux Virtual Machine** on **Microsoft Azure**. It includes a minimal configuration to get you started with Infrastructure as Code (IaC) on the Azure cloud platform.

---

## 🚀 What This Setup Includes

- ✅ Resource Group  
- ✅ Virtual Network and Subnet  
- ✅ Public IP Address  
- ✅ Network Security Group (NSG) with SSH access  
- ✅ Network Interface (NIC)  
- ✅ Linux Virtual Machine (Ubuntu 18.04 LTS)  
- ✅ Boot Diagnostics via a Storage Account  
- ✅ SSH Key Generation for secure access

---

## 📁 File Structure

```
azure-vm-terraform-setup/
├── provider.tf         # Provider config for AzureRM
├── vm.tf               # All resource definitions
├── .terraform/         # (Ignored) Terraform plugin directory
├── .terraform.lock.hcl # Provider dependency lock file
└── README.md           # Project overview
```

---

## 🧱 Prerequisites

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

2. **Preview the infrastructure plan**  
   ```bash
   terraform plan
   ```

3. **Apply the configuration**  
   ```bash
   terraform apply
   ```

4. **To destroy everything when done**  
   ```bash
   terraform destroy
   ```

---

## 💡 Notes

- All variables are defined directly in `vm.tf` — feel free to refactor into `variables.tf` and `terraform.tfvars` as the next step.
- This is a great starting point for testing out Azure Terraform projects or adding additional services (e.g. web servers, storage, etc.).

---

## 📸 Screenshots

_Add deployment screenshots here to showcase your lab in action._

---

## 📚 Learning Goals

- Understand how Terraform provisions infrastructure in Azure
- Practice defining infrastructure as code
- Build foundational DevOps cloud experience

---

## 📌 Tags

`#Terraform` `#Azure` `#DevOps` `#InfrastructureAsCode` `#CloudComputing`
