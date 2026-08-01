## Overview

Custom Inquiry Manager is a Flask-based web application that allows users to submit inquiries through a web form and manage them using a dashboard.
The project demonstrates the fundamentals of Flask development, including routing, Jinja2 templating, form handling, dynamic routes, and server-side data management.

## Features
- Submit customer inquiries
- Dashboard to view all inquiries
- View individual inquiry details
- Dynamic URL routing
- Jinja2 template inheritance
- Server-side form processing
- Responsive project structure

## Technologies Used
- Python
- Flask
- HTML5
- CSS3
- Jinja2

#Structure so far
custom-inquiry-manager/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   └── details.html
│
└── static/
    └── css/
        └── style.css

## Installation

Clone the repository

```bash
git clone <repository-url>

Navigate to the project

cd custom-inquiry-manager

Create a virtual environment

python3 -m venv venv

Activate the virtual environment

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run the application

python app.py
```

---

# Section 7 — Current Limitations

This is something students almost never include, but it shows maturity.

```markdown
## Current Limitations

- Data is stored in memory and is lost when the server restarts.
- No database integration yet.
- No authentication system.
```
## Progress Shots

1. Standard template i built
   <img width="1134" height="744" alt="image" src="https://github.com/user-attachments/assets/2cfbfe6e-c9b8-4a73-b7a3-b0643a44f7ce" />

3. The updated site with user inout under SQLLite
   <img width="1786" height="844" alt="Screenshot 2026-08-01 185826" src="https://github.com/user-attachments/assets/0f35b6ed-756e-43cf-a79e-4e39764f3414" />


- Integrate SQLite or PostgreSQL
- Add user authentication
- Add edit and delete functionality
- Deploy using Docker
- Deploy on AWS        
