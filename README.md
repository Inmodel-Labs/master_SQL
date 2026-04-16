# 🎓 SQL Master Class (40 Exercises)

Welcome to the Master SQL Research Lab. This lab is a professional-grade SQL training course covering 40 exercises inspired by standard SQL curricula (e.g., "Learning SQL").

## 🚀 Quick Start (Terminal)

The lab features a unified controller script `lab.py`.

1.  **Initialize the Environment**:
    ```bash
    python3 lab.py setup
    ```
2.  **Check Connection**:
    ```bash
    python3 lab.py status
    ```
3.  **Monitor Your Progress**:
    ```bash
    python3 lab.py score
    ```

## 📝 How to Complete the Lab

The lab is divided into 4 levels in the `exercises/` folder:

- **Level 1: Basics** (SELECT, Aliasing, Limits)
- **Level 2: Filtering & Sets** (BETWEEN, LIKE, UNION)
- **Level 3: Joins & Aggregations** (Inner/Left/Self Joins, GROUP BY)
- **Level 4: Advanced Analytics** (Subqueries, CTEs, Window Functions)

### Workflow:
1.  Open an exercise file in VS Code (e.g., `exercises/Level_1_Basics.sql`).
2.  Read the **PROBLEM** and **ANALYSIS** for the task.
3.  Write your query under the `-- TODO` marker.
4.  Validate your solution from the terminal:
    ```bash
    python3 lab.py test
    ```
    *You can also test a specific level: `python3 lab.py test Level_1_Basics`*

## 🐳 Running with Docker

If you prefer an isolated environment:
1.  **Build and Start**:
    ```bash
    docker-compose up -d
    ```
2.  **Run Commands Inside Container**:
    ```bash
    docker exec -it master_sql_lab python3 lab.py status
    ```

## 📊 Grading & Feedback
The terminal `score` command tracks your marks in real-time. Each exercise is validated against reference result sets to ensure your logic is sound.

Happy Querying! 🚀
