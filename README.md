# 🎓 SQL Master Class: 40-Page Journey

Welcome to the **SQL Master Class**, a professional training curriculum designed to take students from absolute SQL beginners to advanced data analysts. This lab uses an **Intelligent Tutoring System** to provide real-time feedback and diagnostic hints.

## 🚀 Quick Start

1.  **Initialize the Lab**:
    ```bash
    python3 lab.py setup
    ```
2.  **Check your Rank**:
    ```bash
    python3 lab.py score
    ```
3.  **Start Learning**: Open [exercises/01_Intro_to_Select.sql](exercises/01_Intro_to_Select.sql) and follow the instructions.

## 📖 The Curriculum
The course is divided into 8 modules across 40 standalone "pages":
- **Module 1-2**: Basic Retrieval & Sorting (Pages 01-10)
- **Module 3-4**: Advanced Filtering, Nulls & Strings (Pages 11-20)
- **Module 5-6**: Aggregations, Groups & Joins (Pages 21-30)
- **Module 7-8**: Subqueries & Advanced Analytics (Pages 31-40)

## 📊 Interactive Progress Tracking
Use the `lab.py` controller for a premium learning experience:
- `python3 lab.py status`: Verify database health and connectivity.
- `python3 lab.py test XX`: Validate your solution for Page XX and receive **Intelligent Diagnostic Hints**.
- `python3 lab.py score`: View your RPG-style **Rank** (from Coffee Intern to Master of Data) and module-wise progress.
- `python3 lab.py explain XX`: View the logical execution flow of a query (how the database engine actually thinks).

## 🎓 GitHub Classroom Autograding
This repository is fully configured for automated grading:
- **Automatic Grading**: Every time you `git push` your work, the autograder runs on GitHub.
- **Feedback**: Visit the **Actions** tab in your repository to see your detailed grading report.
- **Pass Criteria**: You must pass all 40 exercises to achieve the "Master of Data" certification.

## 🐳 Docker Support
For a pre-configured environment, run:
```bash
docker-compose up -d
docker exec -it master_sql_lab python3 lab.py status
```

Happy Querying! 🚀
