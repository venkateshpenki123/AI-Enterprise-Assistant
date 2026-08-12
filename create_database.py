import sqlite3

connection = sqlite3.connect("enterprise.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL,
    experience INTEGER
)
""")

employees = [
    (1, "Rahul", "IT", 50000, 2),
    (2, "Priya", "HR", 45000, 3),
    (3, "Arjun", "IT", 65000, 5),
    (4, "Sneha", "Finance", 55000, 4),
    (5, "Kiran", "IT", 70000, 6)
]

cursor.executemany("""
INSERT OR IGNORE INTO employees
(id, name, department, salary, experience)
VALUES (?, ?, ?, ?, ?)
""", employees)

connection.commit()
connection.close()

print("Enterprise database created successfully!")