from chatbot import PDFChatbot

def text_based_chatbot():
    # Initialize the chatbot with the PDF file
    chatbot = PDFChatbot("input.pdf") 

    print("Welcome to the PDF Chatbot!")
    print("Type 'exit' to quit the chatbot.")
    print("-----------------------------------")

    while True:
        # Get user input
        user_query = input("You: ")
        
        # Exit the chatbot
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break

        # Get the chatbot's response
        response = chatbot.ask(user_query)

        # Print the response
        print(f"Bot: {response}")
        print("-----------------------------------")

if __name__ == "__main__":
    text_based_chatbot()