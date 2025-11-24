**LogFixBot** is an intelligent log analysis tool built with **Streamlit** that leverages large language models (LLMs) for error classification and troubleshooting. It processes log files, extracts relevant error lines, provides detailed summaries, and classifies the issues using **zero-shot classification**. The app is ideal for developers and system administrators who need to quickly identify and resolve issues from log files.

---

## Features

- **Upload Log Files**: Easily upload `.txt` log files for automatic analysis.
- **Error & Stack Trace Extraction**: Automatically extracts error lines and stack traces from the logs.
- **Zero-shot Error Classification**: Uses the HuggingFace `facebook/bart-large-mnli` model to classify errors into predefined categories like **configuration error**, **authentication error**, **database error**, and more.
- **Entity Extraction**: Identifies and extracts key entities such as timestamps, error types, and file paths from the logs.
- **Log Summaries**: Generates human-readable summaries with the most likely issues and confidence scores.
- **Interactive Dashboard**: A simple, user-friendly interface built with Streamlit to visualize errors and statistics.

---

## How It Works

1. **Log Parsing**: The uploaded log file is parsed to identify error lines, stack traces, and additional entities.
2. **Zero-shot Classification**: The errors are classified using a pre-trained model (e.g., **facebook/bart-large-mnli**), which categorizes the errors into predefined labels without requiring additional training.
3. **Error Analysis**: A detailed error analysis is displayed, including the most likely causes and relevant classification labels.
4. **Interactive Web Interface**: The app is powered by Streamlit, making it easy to interact with and visualize the log analysis results.

---

## Installation

### Prerequisites

- Python 3.7+
- Pip (Python package installer)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/danideveloper50/logfixbot.git
   cd logfixbot
