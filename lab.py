import sqlite3
import os
import sys
import argparse
from datetime import datetime

# Path Configuration
DB_PATH = 'data/lab.db'
EXERCISES_DIR = 'exercises'

MODULES = {
    "Module 1: Basic Retrieval": range(1, 6),
    "Module 2: Sorting & Simple Filter": range(6, 11),
    "Module 3: Advanced Filtering": range(11, 16),
    "Module 4: Nulls & Strings": range(16, 21),
    "Module 5: Aggregations": range(21, 26),
    "Module 6: Having & Joins": range(26, 31),
    "Module 7: Subqueries": range(31, 36),
    "Module 8: Advanced Analytics": range(36, 41)
}

def get_rank(passed_count):
    if passed_count <= 5: return "☕ Coffee Intern", "Listen, we've all been there. Just focus on finding the right columns for now."
    if passed_count <= 15: return "📊 Junior Reporter", "You're actually generating data people use. Keep it up!"
    if passed_count <= 25: return "🕵️ Data Sleuth", "You're digging deeper. The patterns are starting to make sense."
    if passed_count <= 35: return "🏢 Senior Architect", "You're designing complex views. The database engine fears you."
    return "👑 Master of Data", "You speak the language of the machine. The data bows to your will."

def check_connection():
    if not os.path.exists(DB_PATH):
        print("✗ ERROR: data/lab.db not found. Run: python3 lab.py setup")
        return False
    return True

def show_score():
    if not check_connection(): return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT exercise_id, is_passed FROM _lab_progress")
        results = dict(cursor.fetchall())
        total_p = sum(results.values())
        total_q = 40

        rank_name, narrative = get_rank(total_p)
        
        print("\n" + "="*50)
        print(f"RANK: {rank_name}")
        print(f"MESSAGE: {narrative}")
        print("="*50)

        for mod_name, ex_range in MODULES.items():
            mod_passed = 0
            print(f"\n{mod_name}")
            print("-" * 40)
            for i in ex_range:
                prefix = f"{i:02d}"
                found_key = next((k for k in results.keys() if k.startswith(prefix)), None)
                status = "✓" if (found_key and results[found_key]) else " "
                ex_disp = found_key if found_key else f"{prefix}_(Not Attempted)"
                print(f" [{status}] {ex_disp}")
                if found_key and results[found_key]: mod_passed += 1
            print(f"Module Score: {mod_passed}/{len(ex_range)}")
            
        print("\n" + "=" * 50)
        percentage = (total_p / total_q * 100)
        print(f"OVERALL PERFORMANCE: {total_p}/{total_q} ({percentage:.1f}%)")
        print("=" * 50)
    finally:
        conn.close()

def explain_lesson(target):
    if not target:
        print("Error: Specify a lesson number to explain (e.g., 01).")
        return
    
    # Simple pedagogical mappings for logical execution order
    logic_order = [
        "1. FROM (Identify the source table)",
        "2. JOIN (Connect related tables)",
        "3. WHERE (Filter out rows that don't match)",
        "4. GROUP BY (Bundle rows into groups)",
        "5. HAVING (Filter groups based on aggregate values)",
        "6. SELECT (Choose the final columns/calculate expressions)",
        "7. ORDER BY (Sort the final results)",
        "8. LIMIT (Restrict total rows returned)"
    ]
    
    print(f"\n--- LOGICAL EXECUTION FLOW (Page {target}) ---")
    print("Databases read SQL differently than humans. Here is how this query is actually processed:")
    print("-" * 60)
    for step in logic_order:
        print(step)
    print("-" * 60)
    print("PRO TIP: Always focus on your 'FROM' and 'WHERE' first. If the source is wrong, the SELECT doesn't matter!")

def main():
    parser = argparse.ArgumentParser(description="SQL Lab Intelligent Controller")
    parser.add_argument('command', choices=['status', 'score', 'test', 'setup', 'explain'], help="Command to run")
    parser.add_argument('target', nargs='?', help="Lesson number or prefix")
    
    args = parser.parse_args()
    
    if args.command == 'status':
        if check_connection(): print("✓ Lab environment is healthy.")
    elif args.command == 'score':
        show_score()
    elif args.command == 'setup':
        import setup_lab
        setup_lab.setup_database()
    elif args.command == 'test':
        from tests import run_tests
        success = run_tests.main(args.target)
        if not success:
            sys.exit(1)
    elif args.command == 'explain':
        explain_lesson(args.target)

if __name__ == "__main__":
    main()
