from sql_agent import get_tables, execute_sql

print("Tables:")

tables = get_tables()

print(tables)

print("\nEmployee Data:")

query = """
SELECT *
FROM employees
"""

result = execute_sql(query)

print(result)