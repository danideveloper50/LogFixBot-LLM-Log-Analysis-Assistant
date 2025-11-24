from logfixbot.parser import LogParser
from logfixbot.extractor import EntityExtractor
from logfixbot.huggingface_agent import HuggingFaceAgent


class LogFixBot:
    def __init__(self, log_path, hf_model_name=None):
        self.parser = LogParser(log_path)
        self.extractor = EntityExtractor()
        self.hf_model = HuggingFaceAgent(model_name=hf_model_name) if hf_model_name else None

    def run(self):
        # 1. Parse the raw log file
        logs = self.parser.read_logs()
        errors = self.parser.extract_errors(logs)
        traces = self.parser.extract_stack_traces(logs)

        # 2. Extract entities from each error line
        entities = [
            {
                "raw_line": line,
                "entities": self.extractor.extract_entities(line)
            }
            for line in errors
        ]

        # Base result object (DICT)
        result = {
            "summary": "",
            "stats": {
                "total_lines": len(logs),
                "error_lines": len(errors),
                "has_stack_trace": bool(traces),
            },
            "errors_sample": errors[:10],     # first 10 errors
            "stack_traces": traces,
            "entities": entities,
        }

        # 3. Call the HF model
        if self.hf_model:
            hf_output = self.hf_model.analyze_logs(errors)
            result["model_output"] = hf_output

            # If we got a list of {label, score}, build a human summary
            if isinstance(hf_output, list) and hf_output and "label" in hf_output[0]:
                top = max(hf_output, key=lambda x: x.get("score", 0.0))
                others = sorted(
                    hf_output, key=lambda x: x.get("score", 0.0), reverse=True
                )[1:3]
                other_str = ", ".join(
                    f"{o['label']} ({o['score']:.2f})" for o in others
                )

                result["summary"] = (
                    f"Most likely issue: **{top['label']}** "
                    f"(confidence {top['score']:.2f}). "
                    f"Other possible categories: {other_str}."
                )
        else:
            result["model_output"] = {"error": "HuggingFace model not initialized"}
            result["summary"] = "HuggingFace model is not configured."

        return result


if __name__ == "__main__":
    log_path = "data/sample_logs.txt"
    bot = LogFixBot(log_path, hf_model_name="facebook/bart-large-mnli")
    output = bot.run()
    print(output)
