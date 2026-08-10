# 🚀 AI-Powered Customer Inquiry Manager

An end-to-end customer inquiry management system built with **Flask**, **Amazon Bedrock**, **Amazon SES**, **Docker**, **CloudWatch**, and **AWS EC2**.

---

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
     
