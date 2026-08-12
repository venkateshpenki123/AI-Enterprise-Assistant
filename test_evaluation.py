from evaluation import evaluate_answer


answer = """
Employees receive 20 days of paid annual leave
and can work remotely two days per week.
"""


keywords = [
    "20 days",
    "remote",
    "two days"
]


result = evaluate_answer(
    answer,
    keywords
)


print("Evaluation Result:")
print(result)