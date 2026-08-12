import pandas as pd

from report_generator import generate_report


data = pd.DataFrame({
    "name": [
        "Rahul",
        "Priya",
        "Arjun",
        "Sneha",
        "Kiran"
    ],
    "department": [
        "IT",
        "HR",
        "IT",
        "Finance",
        "IT"
    ],
    "salary": [
        50000,
        45000,
        65000,
        55000,
        70000
    ]
})


print("Generating AI report...")

report = generate_report(data)

print("\n====================")
print("AI REPORT")
print("====================")

print(report)