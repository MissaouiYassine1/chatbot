import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

def chatbot():
    print("Chatbot: Ask me something!")

    while True:
        user_input = input("You: ").strip().lower()

        if not user_input:
            print("Chatbot: Please type something 🙂")
            continue

        tokens = word_tokenize(user_input)

        if "hello" in tokens or "hi" in tokens:
            print("Chatbot: Hello 👋")
        elif "name" in tokens:
            print("Chatbot: I'm a Python chatbot.")
        elif "bye" in tokens:
            print("Chatbot: See you!")
            break
        else:
            print("Chatbot: I’m not sure I understand.")

chatbot()
