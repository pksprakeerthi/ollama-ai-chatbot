import ollama

print("Welcome To AI Chatbot")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Exiting the Chatbot. Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("AI:", response["message"]["content"])