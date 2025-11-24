import os
import requests

import os
import requests

class HuggingFaceAgent:
    """
    Sends log text to a HuggingFace model using the new Router API.
    """

    def __init__(self, model_name="facebook/bart-large-mnli"):
        self.model_name = model_name

        # HF Inference Providers endpoint
        self.api_url = f"https://router.huggingface.co/hf-inference/models/{self.model_name}"

        # ✅ load from HF_TOKEN env var
        self.hf_token = os.getenv("HF_TOKEN")
        if not self.hf_token:
            raise ValueError("ERROR: HF_TOKEN environment variable is not set.")

        self.headers = {
            "Authorization": f"Bearer {self.hf_token}",
            "Content-Type": "application/json",
        }

    def analyze_logs(self, logs):
        """
        Send logs to the HuggingFace model for inference.
        Works with zero-shot-classification models like facebook/bart-large-mnli.
        """

        # If logs is a list of lines, merge into one big string
        if isinstance(logs, list):
            text = "\n".join(logs)
        else:
            text = str(logs)

        # Zero-shot classification requires candidate_labels
        candidate_labels = [
            "configuration error",
            "authentication error",
            "database error",
            "network error",
            "timeout",
            "permission error",
            "other"
        ]

        payload = {
            "inputs": text,
            "parameters": {
                "candidate_labels": candidate_labels
            }
        }

        print("Using HF Router URL:", self.api_url)  # Debug info

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30,
            )
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}

        if response.status_code == 200:
            return response.json()

        return {
            "error": {
                "status_code": response.status_code,
                "message": response.text,
            }
        }
