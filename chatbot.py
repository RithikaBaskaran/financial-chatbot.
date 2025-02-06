financial_data = {
    "total_revenue": "$500,000",
    "net_income_change": "increased by $20,000",
    "profit_margin": "15%",
    "operating_cost": "$200,000",
    "total_assets": "$1,000,000"
}

def simple_chatbot(user_query):
    responses = {
        "What is the total revenue?": f"The total revenue is {financial_data['total_revenue']}.",
        "How has net income changed over the last year?": f"The net income has {financial_data['net_income_change']}.",
        "What is the profit margin?": f"The profit margin is {financial_data['profit_margin']}.",
        "What is the current operating cost?": f"The operating cost is {financial_data['operating_cost']}.",
        "How much is the total assets?": f"The total assets are {financial_data['total_assets']}."
    }
    return responses.get(user_query, "Sorry, I can only provide information on predefined queries.")

if __name__ == "__main__":
    while True:
        user_query = input("Ask a financial question (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        print(simple_chatbot(user_query))
