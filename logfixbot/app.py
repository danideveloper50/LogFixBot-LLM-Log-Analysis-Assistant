from logfixbot.chatbot import LogFixBot

if __name__ == "__main__":
    bot = LogFixBot("data/sample_logs.txt", hf_model_name="facebook/bart-large-mnli")
    output = bot.run()
    print("\n=== LogFixBot Analysis ===\n")
    print(output)
