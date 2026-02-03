import ollama

messages = []

print("🤖 Chatbot avec mémoire (exit pour quitter)\n")

while True:
    user_input = input("👤 Vous : ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="mistral",
        messages=messages
    )

    bot_reply = response["message"]["content"]
    messages.append({"role": "assistant", "content": bot_reply})

    print("🤖 Bot :", bot_reply)
