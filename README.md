# 📚 Study Buddy - AI Chatbot for Students MIT License

Copyright (c) 2025 J2washer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


**Study Buddy** is an AI-powered chatbot designed to help **GCSE** and **A-Level** students with their studies. Built using **LangChain** and **Ollama LLM**, it can hold a context-aware conversation and answer academic questions in a helpful and coherent manner.

---

## 🚀 Features

- ✏️ Tailored for GCSE and A-Level students  
- 🧠 Maintains conversation context for more accurate responses  
- 🤖 Uses the powerful llama3.2 model via Ollama  
- 💬 Simple, interactive command-line chat interface  
- ❌ Type `exit` to end the session anytime

---

## 🛠️ Tech Stack

- Python  
- LangChain (https://www.langchain.com/)  
- Ollama (https://ollama.com/) (llama3.2 model)

---

## 📦 Installation

1. Clone the repository:

   git clone https://github.com/J2washer/study_buddy.git  
   cd study_buddy

2. Install the required dependencies:

   pip install langchain  
   pip install langchain_community  # if needed for OllamaLLM

3. Install and run Ollama (if not already installed):  
   Follow instructions at: https://ollama.com/

4. Run the chatbot:

   python study_buddy.py

---

## 🧠 How It Works

- A conversation template maintains context between turns.  
- Your input is passed along with the chat history to the llama3.2 model.  
- The AI generates responses based on your current question and previous chat.  
- The conversation continues until you type `exit`.  

---

## 📄 Example Usage

Welcome to the AI chat! Type 'exit' to end the conversation.  
You: What is photosynthesis?  
Bot: Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water...

---

## 🤝 Contributing

Feel free to fork the project and submit pull requests. Suggestions and improvements are always welcome!

---

## 📘 License

This project is open-source and available under the MIT License.

---

## 🧑‍🎓 Ideal For

- GCSE & A-Level Students  
- Revision & Homework Help  
- Learning via Q&A style chat

---

Happy studying with **Study Buddy**! 🎓✨
