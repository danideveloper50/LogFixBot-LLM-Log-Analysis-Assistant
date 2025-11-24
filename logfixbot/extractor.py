import re

class EntityExtractor:
    def extract_entities(self, log_line):
        entities = {}
        timestamp = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", log_line)
        if timestamp:
            entities["timestamp"] = timestamp.group()

        error_type = re.search(r"(ERROR|WARN|CRITICAL|EXCEPTION)", log_line)
        if error_type:
            entities["error_type"] = error_type.group()

        module = re.search(r"File \"(.+?)\"", log_line)
        if module:
            entities["file"] = module.group(1)

        return entities