
import json
import re

# Load JSON file
with open("faqs.json", "r") as file:
    data = json.load(file)

print("Welcome to Customer Support Chatbot!")
print("Type bye, exit or quit to stop.")

while True:

    user = input("\nYou: ").lower().strip()

    # Exit
    if re.search(r"\b(bye|exit|quit)\b", user):
        print("Bot: Thank you! Goodbye!")
        break

    # Greetings
    elif any(re.search(r"\b" + re.escape(g) + r"\b", user)
             for g in data["greetings"]):
        print("Bot: Hello! How can I help you?")

    # Check FAQs
    else:
        found = False

        for faq in data["faqs"]:
            question = faq["question"].lower()

            # Match important words
            words = re.findall(r"\b\w+\b", question)
            keywords = [w for w in words if len(w) > 3]

            if sum(word in user for word in keywords) >= 2:
                print("Bot:", faq["answer"])
                found = True
                break

        # Fallback
        if not found:
            print("Bot: Sorry, I didn't understand your question.")
            print("Bot: Please try asking about hours, projects or certificates.")
