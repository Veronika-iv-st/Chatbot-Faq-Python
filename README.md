# 🛍️ Chat FAQ with Python

This project is a virtual assistant that answers frequently asked questions from an online store.  
It is developed in Python using **LangChain** and **OpenAI**, and simulates a basic chatbot with no memory, using predefined fixed answers.

---

## 🚀 What does this project do?

- The user can write typical questions such as:
  - "What are your opening hours?"
  - "Do you ship internationally?"
- The assistant responds clearly, using only the predefined information.
- The chat runs in a loop and ends when the user types `salir` (exit).

---

## 🧰 Technologies and libraries used

- [Python](https://www.python.org/) (recommended: 3.10+)
- [LangChain](https://python.langchain.com/)
- [LangChain Community](https://python.langchain.com/docs/integrations/)
- [OpenAI](https://openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) — to load API keys from a `.env` file

---

## 📦 Installation

Follow these steps to run the project in your local environment:

### 1. Clone the repository


git clone https://github.com/your_username/chat_faq.git
cd chat_faq
2. Create and activate a virtual environment

python -m venv venv
.\venv\Scripts\Activate   # on Windows
# or
source venv/bin/activate  # on Mac/Linux
3. Install dependencies

pip install langchain langchain-community openai python-dotenv
🔐 Configuration
Create a .env file in the root of the project with your OpenAI key:

OPENAI_API_KEY=your_key_here
You can get your key from: https://platform.openai.com/account/api-keys

▶️ Usage
Run the chatbot in your console:

python app.py
Then type your questions.
To exit, type salir (exit).