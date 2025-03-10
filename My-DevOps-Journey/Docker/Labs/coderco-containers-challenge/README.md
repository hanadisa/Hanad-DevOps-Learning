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
