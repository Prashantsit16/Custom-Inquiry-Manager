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

<img width="1536" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/52ef89b4-8500-425d-ae3e-3f4ab187b81c" />


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

## 📈 Project Workflow

1. User submits an inquiry through the web interface.
2. Flask receives and validates the request.
3. Amazon Bedrock generates an AI summary, category, and priority.
4. The inquiry is stored using SQLAlchemy in SQLite.
5. Amazon SES sends confirmation and admin notification emails.
6. CloudWatch collects logs for monitoring.
7. The dashboard displays all submitted inquiries.

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

Health Endpoint:

```
GET /health
```

Example Response:

```json
{
    "status":"healthy",
    "application":"Custom Inquiry Manager",
    "version":"1.0"
}
```
---

## ⭐ Key Highlights

- 🤖 AI-powered inquiry analysis using Amazon Bedrock
- 📧 Automated email notifications with Amazon SES
- ☁️ Deployed on AWS EC2
- 📊 CloudWatch log monitoring
- 🐳 Docker containerization
- 🚀 Production deployment with Gunicorn
- ❤️ Health monitoring endpoint (`/health`)
- 💾 SQLAlchemy ORM with SQLite

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

2. The updated site with user inout under SQLLite
   <img width="1786" height="844" alt="Screenshot 2026-08-01 185826" src="https://github.com/user-attachments/assets/0f35b6ed-756e-43cf-a79e-4e39764f3414" />
   
3. Running on Gunnicorn
   <img width="1201" height="254" alt="image" src="https://github.com/user-attachments/assets/a053cd09-91f5-438e-a7b5-3a1eb396a618" />

4. Dashboard
   <img width="1886" height="906" alt="dashboard png" src="https://github.com/user-attachments/assets/8708e44b-2663-4ab9-ac00-2d90d9d45026" />

5. Inquiry Details
   <img width="1894" height="915" alt="inquiry-details png" src="https://github.com/user-attachments/assets/e5676931-613c-4d0e-944b-d6bb62a76483" />

6. Docker Container
   <img width="1451" height="121" alt="docker-running png" src="https://github.com/user-attachments/assets/2fdc9a38-28dd-4909-9e4f-50a077a11346" />
   
      
     
