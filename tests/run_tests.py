import sqlite3
import os
import sys

# Official solutions to compare against (40 entries)
SOLUTIONS = {
    "01_Intro_to_Select": "SELECT * FROM products;",
    "02_Selecting_Columns": "SELECT name, price FROM products;",
    "03_Column_Aliases": "SELECT name AS Product_Title, price AS Current_Rate FROM products;",
    "04_Distinct_Categories": "SELECT DISTINCT category_id FROM products;",
    "05_Limit_Results": "SELECT * FROM products LIMIT 5;",
    "06_Basic_Sorting": "SELECT * FROM products ORDER BY name ASC;",
    "07_Sorting_by_Price": "SELECT * FROM products ORDER BY price DESC;",
    "08_Filter_Equality": "SELECT * FROM users WHERE is_premium = 1;",
    "09_Filter_Inequality": "SELECT * FROM products WHERE price > 100;",
    "10_Stock_Check": "SELECT * FROM products WHERE stock_quantity = 0;",
    "11_Logical_AND": "SELECT * FROM products WHERE category_id = 1 AND price > 100;",
    "12_Logical_OR": "SELECT * FROM orders WHERE status = 'pending' OR status = 'shipped';",
    "13_In_Operator": "SELECT * FROM categories WHERE name IN ('Electronics', 'Books', 'Sports');",
    "14_Between_Operator": "SELECT * FROM orders WHERE total_amount BETWEEN 50 AND 200;",
    "15_Like_Wildcard": "SELECT * FROM products WHERE name LIKE '%SQL%';",
    "16_Is_Null": "SELECT * FROM employees WHERE manager_id IS NULL;",
    "17_Is_Not_Null": "SELECT * FROM employees WHERE manager_id IS NOT NULL;",
    "18_Concatenation": "SELECT first_name || ' ' || last_name AS full_name FROM employees;",
    "19_String_Length": "SELECT * FROM users WHERE length(username) = 8;",
    "20_Date_Filtering": "SELECT * FROM orders WHERE order_date >= '2026-04-16';",
    "21_Count_Rows": "SELECT COUNT(*) FROM users;",
    "22_Sum_Total": "SELECT SUM(total_amount) FROM orders WHERE status = 'delivered';",
    "23_Avg_Price": "SELECT AVG(price) FROM products;",
    "24_Min_Max": "SELECT MIN(price), MAX(price) FROM products;",
    "25_GroupBy_Basics": "SELECT category_id, COUNT(*) FROM products GROUP BY category_id;",
    "26_Having_Clause": "SELECT category_id, COUNT(*) FROM products GROUP BY category_id HAVING COUNT(*) > 2;",
    "27_Inner_Join": "SELECT p.name, c.name FROM products p JOIN categories c ON p.category_id = c.category_id;",
    "28_Multi_Table_Join": "SELECT u.username, p.name FROM users u JOIN orders o ON u.user_id = o.user_id JOIN order_items oi ON o.order_id = oi.order_id JOIN products p ON oi.product_id = p.product_id;",
    "29_Left_Join": "SELECT u.username, o.order_id FROM users u LEFT JOIN orders o ON u.user_id = o.user_id;",
    "30_Self_Join": "SELECT e.first_name AS employee, m.first_name AS manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.employee_id;",
    "31_Subquery_WHERE": "SELECT * FROM users WHERE user_id NOT IN (SELECT user_id FROM orders);",
    "32_Subquery_ALL": "SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);",
    "33_Correlated_Subquery": "SELECT * FROM products p1 WHERE price > (SELECT AVG(price) FROM products p2 WHERE p1.category_id = p2.category_id);",
    "34_Exists_Operator": "SELECT * FROM categories c WHERE EXISTS (SELECT 1 FROM products p WHERE p.category_id = c.category_id AND p.stock_quantity = 0);",
    "35_Case_Basics": "SELECT username, CASE WHEN is_premium = 1 THEN 'Premium' ELSE 'Standard' END AS status FROM users;",
    "36_Case_Ranges": "SELECT name, CASE WHEN price < 50 THEN 'Bargain' WHEN price <= 200 THEN 'Mid' ELSE 'Luxury' END AS level FROM products;",
    "37_CTE_Basics": "WITH TopUsers AS (SELECT user_id FROM orders GROUP BY user_id HAVING COUNT(*) > 2) SELECT * FROM users WHERE user_id IN TopUsers;",
    "38_Window_RowNumber": "SELECT name, category_id, ROW_NUMBER() OVER(PARTITION BY category_id ORDER BY price DESC) as rank FROM products;",
    "39_Window_Ranking": "SELECT name, price, RANK() OVER(ORDER BY price DESC) as rnk FROM products;",
    "40_Running_Total": "SELECT order_id, order_date, total_amount, SUM(total_amount) OVER(ORDER BY order_date) as running_total FROM orders;"
}

def extract_query(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        content = f.read()
    parts = content.split('-- TODO: Write your query below.')
    if len(parts) < 2:
        return None
    q = parts[1].strip().split(';')[0]
    return (q + ';') if q else None

def run_query(db, query):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        cols = [d[0] for d in cursor.description]
        conn.close()
        return res, cols
    except Exception as e:
        return str(e), []

def get_diagnostic_hint(expected_res, expected_cols, actual_res, actual_cols):
    """Analyze the result sets and provide pedagogical hints."""
    if isinstance(actual_res, str):
        return f"Syntax Error: {actual_res}"
    
    # Check Columns
    if len(expected_cols) != len(actual_cols):
        return f"Column Mismatch: Expected {len(expected_cols)} columns, but you returned {len(actual_cols)}."
    
    expected_cols_lower = [c.lower() for c in expected_cols]
    actual_cols_lower = [c.lower() for c in actual_cols]
    if expected_cols_lower != actual_cols_lower:
        return f"Column Name Mismatch: You returned {actual_cols}, but the expected headers are {expected_cols}."

    # Check Row Count
    if len(expected_res) != len(actual_res):
        return f"Row Mismatch: Expected {len(expected_res)} rows, but you returned {len(actual_res)}. Double-check your WHERE clause or JOIN type."

    # Check Content (if counts match but data doesn't)
    if expected_res != actual_res:
        # Check if it's just sorting
        if sorted(expected_res) == sorted(actual_res):
            return "Data Match but Order Mismatch: You have the right data! Just check your ORDER BY clause."
        return "Calculation Mismatch: The row count and columns are correct, but the values inside don't match. Check your logic or calculation formulas."

    return "Unknown Logic Error: Check your query again."

def update_progress(db, ex_id, passed):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO _lab_progress (exercise_id, level, is_passed, last_attempt)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    """, (ex_id, ex_id, int(passed)))
    conn.commit()
    conn.close()

def main(target_file=None):
    print("--- SQL LAB INTELLIGENT AUTOGRADER ---")
    all_passed = True
    db_path = 'data/lab.db'
    if not os.path.exists(db_path):
        print("Error: data/lab.db not found. Run 'python3 lab.py setup' first.")
        return

    sorted_lessons = sorted(SOLUTIONS.keys())
    lessons_to_test = [l for l in sorted_lessons if l.startswith(target_file)] if target_file else sorted_lessons

    if not lessons_to_test:
        print(f"No lessons found matching: {target_file}")
        return

    for lesson in lessons_to_test:
        sol_q = SOLUTIONS[lesson]
        file_path = f"exercises/{lesson}.sql"
        print(f"Testing {lesson}.sql... ", end="")
        
        student_q = extract_query(file_path)
        if not student_q:
            print("FAIL (No query found)")
            update_progress(db_path, lesson, False)
            continue
            
        expected_res, expected_cols = run_query(db_path, sol_q)
        actual_res, actual_cols = run_query(db_path, student_q)
        
        if expected_res == actual_res and expected_cols == actual_cols:
            print("PASS ✓")
            update_progress(db_path, lesson, True)
        else:
            print("FAIL ✗")
            hint = get_diagnostic_hint(expected_res, expected_cols, actual_res, actual_cols)
            print(f"    💡 HINT: {hint}")
            update_progress(db_path, lesson, False)
            all_passed = False
    
    return all_passed

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    success = main(target)
    if not success:
        sys.exit(1)
