import streamlit as st
from logfixbot.chatbot import LogFixBot

st.title("LogFixBot — LLM Log Analysis Assistant")

uploaded = st.file_uploader("Upload log file", type=["txt"])

if uploaded:
    temp_path = "temp_logs.txt"
    with open(temp_path, "wb") as f:
        f.write(uploaded.read())

    bot = LogFixBot(temp_path, hf_model_name="facebook/bart-large-mnli")
    result = bot.run()

    # If result is a plain list, just show it raw and stop
    if isinstance(result, list):
        st.subheader("Raw Model Output")
        st.json(result)
    else:
        # Main Summary
        if "summary" in result and result["summary"]:
            st.markdown(f"### 📝 Summary\n{result['summary']}")

        # Stats
        st.markdown("### 📊 Log Statistics")
        st.json(result.get("stats", {}))

        # Error Samples
        st.markdown("### 🔍 Extracted Error Lines")
        errors = result.get("errors_sample", [])
        if errors:
            st.code("\n".join(errors))
        else:
            st.write("No error lines detected.")

        # Stack Traces
        st.markdown("### 🔥 Stack Traces")
        traces = result.get("stack_traces", [])
        if traces:
            st.code("\n".join(traces))
        else:
            st.write("No stack traces detected.")

        # Extracted Entities
        st.markdown("### 🧩 Extracted Entities")
        st.json(result.get("entities", []))

        # Model Output
        st.markdown("### 🤖 Model Prediction (Zero-shot Classification)")
        st.json(result.get("model_output", {}))

