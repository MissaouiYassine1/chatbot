from transformers import pipeline

# Load model (this may take time the first run)
chatbot = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=80
)

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "bye":
        print("Chatbot: Goodbye 👋")
        break

    if not user_input:
        print("Chatbot: Please say something 🙂")
        continue

    response = chatbot(
        user_input,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    print("Chatbot:", response[0]["generated_text"])
