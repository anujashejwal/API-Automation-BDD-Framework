# API Automation Framework (BDD) – Python

## 🚀 Overview
This project is a scalable API Automation Framework built using Python, Requests, and Behave (BDD).  
It validates REST APIs with structured step definitions, reusable payloads, configuration handling, and Allure reporting.

---

## 🛠 Tech Stack
- Python
- Requests
- Behave (BDD Framework)
- Allure Reporting
- Config-based Environment Handling

---

## 📂 Project Structure

```
BackEndAutomation/
│
├── features/
│   ├── BookAPI.feature
│   ├── github.feature
│   └── steps/
│       └── stepImpl.py
│
├── utilities/
│   ├── configurations.py
│   ├── resources.py
│
├── properties.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ✅ Features Implemented
- BDD Scenario Execution
- Dynamic Payload Generation
- API Response Validation
- Status Code Assertions
- Public API Testing (GitHub)
- Environment Configuration Handling
- Allure HTML Reporting
- Session-based Authentication

---

## ▶️ How To Run

### Install Dependencies
```
pip install -r requirements.txt
```

### Run Tests
```
behave
```

### Generate Allure Report
```
behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
allure serve AllureReports
```

---

## 📊 Reporting
Allure reports provide:
- Test summary
- Pass/Fail trends
- Attachments
- Environment details

---

## 👩‍💻 Author
Anuja Shejwal  
QA Automation Engineer