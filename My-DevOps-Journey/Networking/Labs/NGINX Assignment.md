# Task: Deploy NGINX on EC2 with Cloudflare DNS ☁️

## Objectives 🎯

- **Domain Registration:** Purchase your domain via Cloudflare (or AWS Route53, preferably Cloudflare) for example, `luqman.co.uk`.
- **EC2 Instance Setup:** Launch an EC2 instance running Ubuntu with NGINX installed on port 80.
- **DNS Configuration:** Add an A record in Cloudflare pointing to your EC2 instance so you can access your site at, for instance, `nginx.luqman.co.uk`.
- **Verification:** Ensure that accessing the domain displays the NGINX welcome page.

---

## Documentation Overview 🔍

This repository details the following steps:

1. **Domain Acquisition:**  
   - Log in to Cloudflare and purchase your domain.

2. **EC2 Instance Setup:**  
   - Create an EC2 instance with Ubuntu.
   - Connect via SSH.
   - Install and start NGINX on port 80.

3. **DNS Setup with Cloudflare:**  
   - Add an A record in Cloudflare for your domain.
   - Verify DNS propagation by accessing your domain (e.g., `nginx.luqman.co.uk`).

Each step is documented with screenshots and command outputs to guide you through the process.

# Step 1: Domain Acquisition

In this step, I logged into Cloudflare and purchased my domain. This process involved:

- Accessing the Cloudflare Dashboard.
- Searching for the desired domain (e.g., `hanadisa.com`).
- Completing the purchase using Cloudflare’s registrar service.

Below are the screenshots documenting the process:

1. **Domain Search & Selection:**  
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/DomainRegistry.png?raw=true" width="600" />

2. **Purchase Confirmation:**  
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/DomainPurchase.png?raw=true" width="600" />

# Step 2: EC2 Instance Setup

In this step, I created an EC2 instance with Ubuntu and set it up with NGINX on port 80. The process involved:

- Logging into the AWS Management Console.
- Launching a new EC2 instance with Ubuntu.
- Configuring the Security Group to allow SSH (port 22) and HTTP (port 80) traffic.
- Connecting to the instance via SSH.
- Installing and starting NGINX.

Below are the screenshots documenting the process:

1. **EC2 Instance Launch:**  
   <img src="./screenshots/ec2-launch.png" alt="EC2 Instance Launch Screenshot" width="600" />

2. **Instance Details:**  
   <img src="./screenshots/ec2-details.png" alt="EC2 Instance Details Screenshot" width="600" />

   # Step 3: Cloudflare DNS Setup

In this step, I configured the DNS settings in Cloudflare to point to my EC2 instance. The process involved:

- Logging into Cloudflare and navigating to the DNS settings for `hanadisa.com`.
- Adding an A record for a subdomain (e.g., `nginx.hanadisa.com`) that points to the public IP address of my EC2 instance.
- Verifying that the DNS changes have propagated and that I can access the NGINX welcome page using the subdomain.

Below are the screenshots documenting the process:

1. **Accessing DNS Settings:**  
   <img src="./screenshots/dns-settings.png" alt="DNS Settings Screenshot" width="600" />

2. **Adding the A Record:**  
   <img src="./screenshots/add-a-record.png" alt="Add A Record Screenshot" width="600" />

3. **DNS Propagation Verification:**  
   <img src="./screenshots/dns-verification.png" alt="DNS Verification Screenshot" width="600" />

*Note: Replace the image paths with the actual paths to your screenshots.*

---

# Conclusion

I successfully completed the assignment by:

- **Domain Acquisition:** Purchased `hanadisa.com` through Cloudflare.
- **EC2 Instance Setup:** Launched an AWS EC2 instance running Ubuntu with NGINX installed on port 80.
- **DNS Configuration:** Configured Cloudflare DNS to point a subdomain (e.g., `nginx.hanadisa.com`) to my EC2 instance.
- **Verification:** Confirmed that accessing the subdomain displays the NGINX welcome page.

This documentation, complete with step-by-step instructions and screenshots, provides a clear guide to replicating the setup. 

*Visit [nginx.hanadisa.com](https://nginx.hanadisa.com) to see the final result!*


3. **SSH Connection Terminal:**  
   <img src="./screenshots/ssh-connection.png" alt="SSH Connection Screenshot" width="600" />

4. **NGINX Installation & Start:**  
   <img src="./screenshots/nginx-install.png" alt="NGINX Installation Screenshot" width="600" />
