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
