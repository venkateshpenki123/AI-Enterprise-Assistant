def evaluate_answer(answer, expected_keywords):

    if not answer:
        return {
            "score": 0,
            "status": "Failed"
        }

    answer_lower = answer.lower()

    matched = 0

    for keyword in expected_keywords:

        if keyword.lower() in answer_lower:
            matched += 1

    score = (
        matched / len(expected_keywords)
    ) * 100

    if score >= 80:
        status = "Excellent"

    elif score >= 50:
        status = "Good"

    else:
        status = "Needs Improvement"

    return {
        "score": round(score, 2),
        "status": status
    }