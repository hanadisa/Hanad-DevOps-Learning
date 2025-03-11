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

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Docker/Labs/coderco-containers-challenge/Images/start-up.png?raw=true" width="900">

📸 **Screenshot of Welcome Page:**

<img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Docker/Labs/coderco-containers-challenge/Images/welcome-page.png?raw=true" width="600">

<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration Of Count Page</h2>
  <div style="width: 200px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/Docker/Labs/coderco-containers-challenge/Images/count-page.gif?raw=true" alt="Count Page GIF" width="75%" />
  </div>
</div>
