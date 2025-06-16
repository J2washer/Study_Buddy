from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:

You are an AI assistant designed to help GCSE / A-Level students with their studies.
You should answer the question based on the conversation history provided.
"""

model = OllamaLLM(model="llama3.2") 
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print ("Welcome to the AI chat! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("BYE!")
            break
        
        
        result = chain.invoke({"context":context, "question": user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nBot: {result}\n"

if __name__ == "__main__":
    handle_conversation()


# This code is a simple chat application using LangChain and OllamaLLM.
# It allows users to have a conversation with an AI model, maintaining context throughout the interaction.
# The user can type messages, and the AI will respond based on the conversation history.
# The conversation can be ended by typing 'exit'.
