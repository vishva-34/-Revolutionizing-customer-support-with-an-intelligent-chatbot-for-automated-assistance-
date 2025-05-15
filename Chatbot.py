import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Function to process user input and classify it into categories
def classify_intent(user_input):
    doc = nlp(user_input.lower())
    keywords = [token.lemma_ for token in doc]

    if any(keyword in keywords for keyword in ["track", "order", "status", "shipping"]):
        return "track_order"
    elif any(keyword in keywords for keyword in ["return", "refund", "exchange"]):
        return "return_order"
    elif any(keyword in keywords for keyword in ["product", "item", "price", "availability"]):
        return "product_inquiry"
    elif any(keyword in keywords for keyword in ["exit", "bye", "nothing", "no"]):
        return "exit"
    else:
        return "unknown"

# Function to handle chatbot responses
def chatbot():
    print("Chatbot: Hello! Welcome to ShopMate. How can I help you today?")
    
    while True:
        user_input = input("User: ")
        intent = classify_intent(user_input)

        if intent == "track_order":
            order_number = input("Chatbot: Sure! Could you please provide your order number?\nUser: ")
            print(f"Chatbot: Got it! Your order #{order_number} is expected to arrive in 2 days. Would you like more details?")
        
        elif intent == "return_order":
            order_number = input("Chatbot: I can help with returns. Can you provide your order number?\nUser: ")
            print(f"Chatbot: I've found your order #{order_number}. Would you like a refund or exchange?")
        
        elif intent == "product_inquiry":
            product_name = input("Chatbot: Can you tell me the name or description of the product you're looking for?\nUser: ")
            print(f"Chatbot: The {product_name} is in stock. Would you like to add it to your cart or know more details?")
        
        elif intent == "exit":
            print("Chatbot: Thank you for visiting ShopMate! Have a great day!")
            break
        
        else:
            print("Chatbot: I’m sorry, I didn’t understand that. Could you please rephrase or ask something else?")

chatbot()
