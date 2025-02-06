from flask import Flask, request, jsonify

app = Flask(__name__)

financial_data = {
    "total_revenue": "$500,000",
    "net_income_change": "increased by $20,000",
    "profit_margin": "15%",
    "operating_cost": "$200,000",
    "total_assets": "$1,000,000"
}

responses = {
    "What is the total revenue?": f"The total revenue is {financial_data['total_revenue']}.",
    "How has net income changed over the last year?": f"The net income has {financial_data['net_income_change']}.",
    "What is the profit margin?": f"The profit margin is {financial_data['profit_margin']}.",
    "What is the current operating cost?": f"The operating cost is {financial_data['operating_cost']}.",
    "How much is the total assets?": f"The total assets are {financial_data['total_assets']}."
}

@app.route("/chat", methods=["POST"])
def chatbot():
    user_query = request.json.get("query")
    response = responses.get(user_query, "Sorry, I can only provide information on predefined queries.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
