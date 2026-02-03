import ollama

print("🤖 Chatbot NLP (tape 'exit' pour quitter)\n")

while True:
    user_input = input("👤 Vous : ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 À bientôt !")
        break

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("🤖 Bot :", response["message"]["content"])
