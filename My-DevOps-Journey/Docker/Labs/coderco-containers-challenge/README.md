#  CoderCo Containers Challenge: Multi-Container Flask & Redis App

## 📌 Introduction
As part of my Docker learning journey, I completed the **CoderCo Containers Challenge**, where I built a **multi-container application** using **Flask and Redis**. This challenge helped reinforce concepts around **containerized services**, **Docker Compose**, and **inter-container networking**.

## 🎯 Objective
The goal of this challenge was to create a **Flask web application** that interacts with a **Redis database** to store and retrieve data.

## 🛠 Project Overview
This project consists of:
- **Flask Web App** (Python) - Displays a welcome message and tracks visit counts using Redis.
- **Redis Database** - A key-value store that maintains visit counts.

## 🔹 Features
✅ Flask application with two endpoints:
  - `/` → Displays a welcome message.
  - `/count` → Increments and displays a visit count stored in Redis.  
✅ **Dockerized both services** with individual `Dockerfile`s.  
✅ **Docker Compose** to manage the multi-container setup.

---

## 📂 Folder Structure
```bash
coderco-containers-challenge/
├── app.py 
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
```
---

## 🔹 **Step 1: Writing the Flask App**  
I created a simple **Flask application** with the following routes:  

- `/` → Displays a **Welcome Message**  
- `/count` → **Increments & displays a visit count** stored in Redis


✅ **Final Flask App Code (app.py):**
```python
from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def home():
    return "Welcome to the CoderCo Containers Challenge!"

@app.route("/count")
def count():
    redis_client.incr("visits")
    visits = redis_client.get("visits")
    return f"Visit count: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
📸 **Screenshot of Docker Compose + Redis Running:**

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Docker/Labs/coderco-containers-challenge/Images/start-up.png?raw=true" width="600">

📸 **Screenshot of Welcome Page:**

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Docker/Labs/coderco-containers-challenge/Images/welcome-page.png?raw=true" width="600">

<div style="text-align: center; margin: 20px 0;">

<div style="text-align: center; margin: 20px 0;">
  <h4 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration Of Count Page</h4>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Docker/Labs/coderco-containers-challenge/Images/count-page.gif?raw=true" alt="Count Page GIF" width="75%" />
  </div>
</div>

## 📌 Dockerfile  
The `Dockerfile` sets up the environment to run the Flask application.

### 🔹 Steps:
1. **Base Image**: Uses `python:3.8-slim` for a lightweight Python environment.
2. **Working Directory**: Sets `/app` as the working directory.
3. **Install Dependencies**: Copies `requirements.txt` and installs dependencies.
4. **Copy Source Code**: Adds application files to the container.
5. **Expose Port**: Exposes port **5002** to the host.
6. **Run Application**: Executes `app.py` using Python.

### 📌 **Dockerfile Code**
```dockerfile
# Use a lightweight Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the application port
EXPOSE 5002

# Run the application
CMD ["python", "app.py"]
```

---


# 📌 Docker Compose (docker-compose.yml)
Docker Compose manages the multi-container deployment with two services:

## 🔹 Services:
### **web:** The Flask application.
- Built from the **Dockerfile**.
- Exposes **port 5000** to the host.
- **Depends on** Redis to function properly.

### **redis:** Redis server for the counter.
- Uses the latest **Redis** image.
- Exposes **port 6379** for communication.

## 🔹 Explanation of `docker-compose.yml`
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis
  redis:
    image: "redis:latest"
    ports:
      - "6379:6379"
```

---

# 📌 Summary ✅  
I successfully completed the **CoderCo Containers Challenge** by:  

✅ Creating a **Flask application** with a visit counter using **Redis**  
✅ Writing a **Dockerfile** to containerize the Flask app  
✅ Using **Docker Compose** to manage the multi-container setup  
✅ Implementing **Redis for persistent storage**  

This setup is a **basic multi-container architecture**, setting the foundation for **scalable deployments** in real-world projects. 🚀  
