📊 Financial Chatbot

📌 Project Overview

This chatbot is designed to answer predefined financial queries based on analyzed financial data.
It provides insights into key financial metrics such as total revenue and net income changes.

⚡ Features

Responds to common financial queries.

Uses predefined answers based on available financial data.

Can be tested using command-line input, Postman, or cURL.

How to Run the Chatbot
1️⃣ Clone the Repository (if using GitHub)
```bash git clone https://github.com/your-username/financial-chatbot.git
cd financial-chatbot
```
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Run the Chatbot
```bash
python app.py
```
This will start the chatbot server at:
➡️ http://127.0.0.1:5000

🔗 API Endpoint (if using Flask)

📌 Endpoint: /chat
Method: POST
Content-Type: application/json

📌 Example API Request using cURL:
```bash
curl -X POST http://127.0.0.1:5000/chat \
-H "Content-Type: application/json" \
-d '{"query": "What is the total revenue?"}'
```
📌 Example API Request in JSON Format:
```json
{
   "query": "What is the total revenue?"
}
```
📌 Example API Response:
```json
{
   "response": "The total revenue is $500,000."
}
```
⚠️ Limitations

❌ The chatbot only understands predefined financial queries.

❌ No real-time financial data processing.

❌ Lacks advanced NLP (Natural Language Processing).

📂 Project Folder Structure

📂 Financial-Chatbot

│── chatbot.py          # Chatbot logic  

│── app.py              # API for chatbot  

│── financial_data.csv  # Financial dataset  

│── documentation1      # Data Analysis

│── README.md           # Documentation  


👤 Author

Name: Rithika Baskaran

📧 Email: rithi.basky@gmail.com

📌 Affiliation: University of Maryland, College Park


