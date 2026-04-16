import sqlite3
import os

def setup_database():
    db_path = 'data/lab.db'
    schema_path = 'data/schema.sql'
    seed_path = 'data/seed.sql'

    if not os.path.exists('data'):
        os.makedirs('data')

    # Remove existing DB if it exists
    if os.path.exists(db_path):
        os.remove(db_path)

    print(f"--- Initializing {db_path} ---")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Run Schema
    with open(schema_path, 'r') as f:
        cursor.executescript(f.read())
    print("✓ Schema applied.")

    # Run Seed Data
    with open(seed_path, 'r') as f:
        cursor.executescript(f.read())
    print("✓ Seed data inserted.")

    conn.close()
    print("--- Setup Complete! ---")

if __name__ == "__main__":
    setup_database()
