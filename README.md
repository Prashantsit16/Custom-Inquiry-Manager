# 🚀 AI-Powered Customer Inquiry Manager

An end-to-end customer inquiry management system built with **Flask**, **Amazon Bedrock**, **Amazon SES**, **Docker**, **CloudWatch**, and **AWS EC2**.

---

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![CloudWatch](https://img.shields.io/badge/Amazon-CloudWatch-orange)
![Bedrock](https://img.shields.io/badge/Amazon-Bedrock-purple)
![SES](https://img.shields.io/badge/Amazon-SES-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Overview

AI-Powered Customer Inquiry Manager is a production-ready web application that streamlines customer inquiry management using Generative AI and AWS cloud services.

Users can submit inquiries through a responsive web interface, where Amazon Bedrock automatically analyzes the message, generates an AI summary, assigns a category and priority, and stores the inquiry in a SQLite database. Email notifications are sent using Amazon SES, while Amazon CloudWatch provides centralized logging and monitoring. The application is containerized with Docker and deployed on an AWS EC2 instance using Gunicorn as the production WSGI server.

This project demonstrates end-to-end backend development, cloud deployment, AI integration, monitoring, and production best practices.

## ✨ Features

- Submit customer inquiries through a modern web interface
- AI-powered categorization using Amazon Bedrock
- Automatic priority assignment
- Dashboard for tracking inquiries
- Email notifications using Amazon SES
- Dockerized deployment
- Production-ready with Gunicorn
- CloudWatch log monitoring
- Health endpoint for monitoring

---

## 🏗 Architecture

(Architecture diagram here)

---

## ⚙ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Flask |
| Database | SQLite + SQLAlchemy |
| AI | Amazon Bedrock |
| Email | Amazon SES |
| Monitoring | Amazon CloudWatch |
| Deployment | AWS EC2 |
| Containerization | Docker |
| Production Server | Gunicorn |

---

## ☁ AWS Services Used

- Amazon EC2
- Amazon Bedrock
- Amazon SES
- Amazon CloudWatch
- IAM

---

## 📂 Project Structure

```text
Custom-Inquiry-Manager/
├── app.py
├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── services/
├── templates/
├── static/
└── screenshots/
```

---

## 🚀 Running Locally

```bash
git clone <repo>

cd Custom-Inquiry-Manager

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python app.py
```

---

## 🐳 Running with Docker

```bash
docker compose up --build
```

---

## ❤️ Health Check

```
GET /health
```

Response

```json
{
  "status": "healthy",
  "application": "Custom Inquiry Manager",
  "version": "1.0"
}
```

---

## 📊 Monitoring

- Amazon CloudWatch Logs
- Structured application logging
- Gunicorn logs
- Health endpoint

---

## 🔮 Future Improvements

- User Authentication
- PostgreSQL support
- CI/CD Pipeline using GitHub Actions
- Kubernetes deployment
- JWT Authentication
- Redis caching

---

## Progress Shots

1. Standard template i built
   <img width="1134" height="744" alt="image" src="https://github.com/user-attachments/assets/2cfbfe6e-c9b8-4a73-b7a3-b0643a44f7ce" />

3. The updated site with user inout under SQLLite
   <img width="1786" height="844" alt="Screenshot 2026-08-01 185826" src="https://github.com/user-attachments/assets/0f35b6ed-756e-43cf-a79e-4e39764f3414" />
     
