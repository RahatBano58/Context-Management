# 🤖 Agentic AI Exercises with Context Management  

This project demonstrates how to build **Agentic AI Applications** using the **Gemini API (OpenAI-compatible)** with `agents` SDK in Python.  
Each exercise focuses on **context management** using `RunContextWrapper`, `function_tool`, and `pydantic` models — allowing AI agents to fetch and display structured information.  

---

## 📂 Project Structure  

📁 project-root
┣ 📄 connection.py # API connection setup
┣ 📄 bank_account.py # Exercise 01: Bank Account Context
┣ 📄 student_profile.py # Exercise 02: Student Profile Context
┣ 📄 library_book.py # Exercise 03: Library Book Context
┣ 📄 .env # Environment variables (Gemini API Key)
┗ 📄 README.md # Documentation

---

## ⚙️ Setup Instructions  

### 1. Clone the Repository
git clone https://github.com/RahatBano58/Context-Management
cd Context-Management

---

### 2. Create a Virtual Environment
.venv
.venv\Scripts\activate       # Windows

---

### 3. Configure API Key
**Create a .env file in the project root and add:**
- GEMINI_API_KEY=your_api_key_here
- OPENAI_API_KEY=your_api_key_here

---

### 4. Run Any Exercise
uv run bank_account.py

📘 **Exercises Overview**
🏦 **Exercise 01 – Bank Account Context**

- Uses BankAccount class to store account details.
- Agent fetches and displays details such as Account Number, Customer Name, Balance, and Account Type.
- Rich formatting with colors & emojis.
✅ **Run**:
- uv run bank_account.py

🎓 **Exercise 02 – Student Profile Context**
- Uses StudentProfile class to store academic records.
- Agent provides Student ID, Name, Current Semester, and Total Courses.
- Response is highlighted with emojis & colors for readability.
✅ **Run**:
- uv run student_profile.py

📚 **Exercise 03 – Library Book Context**
- Uses LibraryBook class to store library book details.
- Agent answers book-related queries (e.g., author, availability).
- Output is well-formatted with emojis & styling.
✅ **Run**:
- uv run library_book.py

---

## 🔑 Key Concepts Demonstrated
- ✅ Context Management with RunContextWrapper
- ✅ Structured Data Models using pydantic.BaseModel
- ✅ Tool Integration with @function_tool
- ✅ Agent Instructions for controlled responses
- ✅ Gemini API (OpenAI-Compatible) integration
- ✅ Rich Formatting for attractive CLI outputs

--- 
### 🌟 Example Output
**Bank Account Info Example:**
- ✨ Here is your Bank Account Info: ✨  
- 🔢 Account Number: ACC-789456  
- 👤 Customer Name: Rahat Bano  
- 💰 Account Balance: PKR 75,500.50  
- 🏦 Account Type: Savings

---

###  🚀 Future Enhancements
- Add more real-world contexts (Employee records, Hospital management, Shopping assistant).
- Extend with multi-agent collaboration using handoffs.
- Integrate with Streamlit for UI.

---

### 🙌 Acknowledgements
- Google Gemini API
- agents SDK
- Rich Library

---

## ✍️ Created By  
👩‍💻 **Rahat Bano**  
