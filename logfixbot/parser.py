import re

class LogParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_logs(self):
        with open(self.filepath, "r") as f:
            return f.readlines()

    def extract_errors(self, logs):
        error_pattern = r"(ERROR|WARN|CRITICAL|EXCEPTION).*"
        return [line.strip() for line in logs if re.search(error_pattern, line)]

    def extract_stack_traces(self, logs):
        stack = []
        capture = False
        for line in logs:
            if "Traceback" in line or "Exception" in line:
                capture = True
            if capture:
                stack.append(line.rstrip())
            if line.strip() == "" and capture:
                capture = False
        return stack
