# AI-Based Skill Gap Analyzer

A web-based application that analyzes a candidate's resume against job requirements to identify available skills, missing skills, and the overall skill gap percentage.

## Project Overview

The AI-Based Skill Gap Analyzer helps candidates understand how well their current skills match the requirements of different job roles.

The application allows a user to upload a resume and select a job role. The system extracts skills from the resume, compares them with the skills required for the selected job, and displays:

* Required skills
* Available skills
* Missing skills
* Skill gap percentage

##  Features

* Resume upload
* Supports PDF, DOCX, and TXT files
* Automatic resume text extraction
* Skill identification from resume content
* Job-wise skill comparison
* Missing skill detection
* Skill gap percentage calculation
* React-based user interface
* Django REST-style backend APIs
* MySQL database integration

## How It Works

```text
User
  ↓
Upload Resume
  ↓
Resume Text Extraction
  ↓
Skill Identification
  ↓
Select Job Role
  ↓
Compare Resume Skills with Job Skills
  ↓
Calculate Skill Gap
  ↓
Display Results
```

##  Technologies Used

### Frontend

* React.js
* HTML
* CSS
* Vite

### Backend

* Python
* Django
* Django REST-style API endpoints

### Database

* MySQL

### Other Libraries

* pypdf
* python-docx
* django-cors-headers
* python-dotenv

## Database

The application uses MySQL database `skill_gap_analyzer`.

Main tables include:

* `users`
* `resumes`
* `skills`
* `jobs`
* `resume_skills`
* `job_skills`

The database stores user information, uploaded resumes, available skills, job requirements, and the relationship between resumes/jobs and skills.

## Skill Gap Calculation

The skill gap percentage is calculated based on the number of missing skills compared with the total required skills.

```text
Skill Gap % = (Missing Skills / Total Required Skills) × 100
```

For example, if a job requires 3 skills and the candidate has 2 of them:

```text
Missing Skills = 1
Total Required Skills = 3

Skill Gap = (1 / 3) × 100
          = 33.33%
```

##  Project Structure

```text
AI-Skill-Gap-Analyzer/
│
├── backend/
│   ├── analyzer/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

##  How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Apekshashetty30/AI-Skill-Gap-Analyzer.git
cd AI-Skill-Gap-Analyzer
```

### 2. Backend Setup

Go to the backend folder:

```bash
cd backend
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install Django mysqlclient python-dotenv pypdf python-docx django-cors-headers
```

### 3. Configure Environment Variables

Create a `.env` file inside the `backend` folder:

```text
DB_PASSWORD=your_mysql_password
```

Do not upload the `.env` file to GitHub.

### 4. Configure MySQL

Create the MySQL database:

```sql
CREATE DATABASE skill_gap_analyzer;
```

Update the database configuration in Django settings with your MySQL username, database name, host, and port.

### 5. Run the Backend

From the `backend` folder:

```bash
python manage.py migrate
python manage.py runserver
```

The backend will run at:

```text
http://127.0.0.1:8000/
```

### 6. Run the Frontend

Open another terminal and go to the frontend folder:

```bash
cd frontend
npm install
npm run dev
```

The frontend will run at:

```text
http://localhost:5173/
```

## Security

Sensitive information such as database passwords is stored in environment variables and excluded from Git using `.gitignore`.

The `.env` file should never be committed to the repository.

## Future Enhancements

* User authentication and registration
* NLP-based resume analysis
* Machine learning-based skill extraction
* Job recommendation based on candidate skills
* Personalized learning recommendations for missing skills
* Candidate dashboard
* Resume improvement suggestions
* More advanced job matching

## Project

**AI-Based Skill Gap Analyzer**

Built using React.js, Django, Python, and MySQL.
