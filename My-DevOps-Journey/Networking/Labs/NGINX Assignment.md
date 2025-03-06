# Task: Deploy NGINX on EC2 with Cloudflare DNS ☁️

## Objectives 🎯

- **Domain Registration:** Purchase a domain via Cloudflare and configure DNS.
- **EC2 Instance Setup:** Launch an AWS EC2 instance with Ubuntu and NGINX.
- **DNS Configuration:** Add an A record in Cloudflare pointing to the EC2 instance.
- **HTTPS (SSL/TLS):** Secure the website using Let's Encrypt (Certbot).
- **Verification:** Ensure `nginx.hanadisa.com` loads correctly over HTTPS.
---

## Documentation Overview 🔍

This repository details the following steps:

1. **Domain Acquisition:** ™️
   - Log in to Cloudflare and purchase your domain.

2. **EC2 Instance Setup:** 💻
   - Create an EC2 instance with Ubuntu.
   - Connect via SSH.
   - Install and start NGINX on port 80.

3. **DNS Setup with Cloudflare:** ☁️
   - Add an A record in Cloudflare for your domain.
   - Verify DNS propagation by accessing your domain (e.g., `nginx.hanadisa.com`).

4. **Enabling HTTPS (SSL/TLS):** 🔒
   - Use Let's Encrypt (Certbot) to generate an SSL certificate.
   - Configure NGINX to serve traffic securely over `https://nginx.hanadisa.com`.

5. **Testing NGINX Deployment:** ✅
   - Verify that `https://nginx.hanadisa.com` loads successfully in a browser.
   - Confirm that the NGINX welcome page is displayed.
   - Ensure SSL/TLS is working and the site is secured.

Each step is documented with **screenshots** and **command outputs** to provide a clear and structured guide.

# Step 1: Domain Acquisition ™️

In this step, I logged into Cloudflare and purchased my domain. This process involved:

- Accessing the Cloudflare Dashboard.
- Searching for the desired domain (e.g., `hanadisa.com`).
- Completing the purchase using Cloudflare’s registrar service.

Below are the screenshots documenting the process:

1. **Domain Search & Selection:**  
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/DomainRegistry.png?raw=true" width="600" />

2. **Purchase Confirmation:**  
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/DomainPurchase.png?raw=true" width="600" />

# Step 2: EC2 Instance Setup 💻

In this step, I created an EC2 instance with Ubuntu and set it up with NGINX on port 80. The process involved:

- Logging into the AWS Management Console.
- Launching a new EC2 instance with Ubuntu.
- Configuring the Security Group to allow SSH (port 22) and HTTP (port 80) traffic.
- Connecting to the instance via SSH.
- Installing and starting NGINX.

Below are the screenshots documenting the process:

1. **EC2 Instance Launch:**  
   <img src="https://github.com/user-attachments/assets/02f4055f-d77c-4975-91c4-53e627703914" alt="EC2 Instance Launch Screenshot" width="600" />

2. **Instance Details:**  
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/EC2-Details.gif?raw=true" alt="EC2 Instance 
      Details GIF" width="600" />

3. **SSH Connection Terminal:**  
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/SSH-Connection.png?raw=true" width="600" />

4. **NGINX Installation & Start:**  
   <img src="https://github.com/user-attachments/assets/7858a47a-8317-46ed-ab2f-5ddf7120ebf4" width="600" />

# Step 3: Cloudflare DNS Setup ☁️

In this step, I configured the DNS settings in Cloudflare to point to my EC2 instance. The process involved:

- Logging into Cloudflare and navigating to the DNS settings for `hanadisa.com`.
- Adding an A record for a subdomain (e.g., `nginx.hanadisa.com`) that points to the public IP address of my EC2 instance.
- Verifying that the DNS changes have propagated and that I can access the NGINX welcome page using the subdomain.

Below are the screenshots documenting the process:

1. **Accessing DNS Settings:**  
   <img src="https://github.com/user-attachments/assets/bab1dd15-7f4e-4246-aa12-ff51001d3b20" width="600" />

2. **Adding the A Record:**  
   <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/A-Record.png?raw=true" alt="Add A Record Screenshot" width="600" />

3. **DNS Propagation Verification:**  
   <img src="https://github.com/user-attachments/assets/acb9d439-b38f-4d0e-ac1c-066866ab4377" width="600" />

# Step 4: Enabling HTTPS (SSL/TLS) 🔒

After setting up NGINX and configuring Cloudflare, I secured `nginx.hanadisa.com` with **Let's Encrypt (Certbot)** to enable HTTPS.

### **Verification Using Browser**
I opened my browser and visited:  https://nginx.hanadisa.com/

📸 **SSL Verification Screenshot:**  

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/HTTPS-Enabling.png?raw=true" width="600" />

This confirms that:
- The site is **secured with HTTPS** 🔒.
- The **SSL certificate is active and trusted**.
- **All HTTP traffic is automatically redirected to HTTPS**.
- **Cloudflare DNS & NGINX are properly handling HTTPS traffic**.

✅ The SSL setup is complete, and the site is now secure!

# Step 5: Testing NGINX Deployment ✅

After setting up NGINX and configuring Cloudflare, I verified that `nginx.hanadisa.com` is accessible in the browser.

### **Verification Using Browser**
I opened my browser and visited: https://nginx.hanadisa.com/

📸 **NGINX Welcome Page Screenshot:**  

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Networking/Labs/Images/Deployment-Test.png?raw=true" width="600" />

This confirms that:
- My EC2 instance is serving web requests successfully.
- NGINX is installed and running.
- My domain (`nginx.hanadisa.com`) is correctly pointing to my EC2 instance.
- SSL/TLS is enabled and working.

✅ The setup is complete, and the website is live!

---

# Conclusion

I successfully completed the assignment by:

- **Domain Acquisition:** Purchased `hanadisa.com` through Cloudflare.
- **EC2 Instance Setup:** Launched an AWS EC2 instance running Ubuntu with NGINX installed on port 80.
- **DNS Configuration:** Configured Cloudflare DNS to point a subdomain (e.g., `nginx.hanadisa.com`) to my EC2 instance.
- **Verification:** Confirmed that accessing the subdomain displays the NGINX welcome page.

This documentation, complete with step-by-step instructions and screenshots, provides a clear guide to replicating the setup. 
