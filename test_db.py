# test_db.py
import sqlite3

# Connect to database (creates hospital.db if it doesn't exist)
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# ✅ Create admin table with UNIQUE username
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# ✅ Insert default admin only if not exists
cursor.execute("""
INSERT OR IGNORE INTO admin (username, password)
VALUES (?, ?)
""", ("admin", "admin123"))

conn.commit()
conn.close()

print("✅ Admin table ready & default admin user inserted (username=admin, password=admin123)")
