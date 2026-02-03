import ollama

# System prompt = règles du bot
system_prompt = {
    "role": "system",
    "content": """
Tu es un assistant NLP expert en informatique et Linux.

Étapes obligatoires :
1. Identifie l'intention de l'utilisateur
2. Répond simplement et clairement
3. Si c’est une commande Linux, donne la commande + explication
4. Si ce n’est pas lié à l'informatique ou Linux, refuse poliment

Intentions possibles :
- greeting
- definition
- linux_command
- troubleshooting
- explanation
- thanks
"""
}

# Mémoire de conversation
messages = [system_prompt]

print("🤖 Chatbot NLP Linux & IT (tape 'exit' pour quitter)\n")

while True:
    user_input = input("👤 Vous : ")

    if user_input.lower() == "exit":
        print("👋 À bientôt !")
        break

    # Ajout du message utilisateur
    messages.append({"role": "user", "content": user_input})

    # Appel à Ollama
    response = ollama.chat(
        model="mistral",
        messages=messages
    )

    bot_reply = response["message"]["content"]

    # Ajout de la réponse du bot à la mémoire
    messages.append({"role": "assistant", "content": bot_reply})

    print("\n🤖 Bot :")
    print(bot_reply)
    print("-" * 40)
