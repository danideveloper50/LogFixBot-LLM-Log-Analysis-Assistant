class Evaluator:
    def evaluate(self, bot_output):
        score = 0
        keywords = ["root cause", "fix", "issue", "steps"]
        for kw in keywords:
            if kw in bot_output.lower():
                score += 1
        return {
            "coverage_score": score / len(keywords),
            "summary": "Good coverage" if score > 2 else "Needs improvement"
        }
