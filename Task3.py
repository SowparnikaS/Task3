import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json") as file:
    data = json.load(file)

# Preprocessing
patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

# Vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

# Train model
model = LogisticRegression()
model.fit(X, tags)

# Chat function
def chat():
    print("Bot: Hello! Ask me anything (type 'quit' to exit)")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            print("Bot: Goodbye!")
            break
        vec = vectorizer.transform([inp])
        prediction = model.predict(vec)[0]

        for intent in data["intents"]:
            if intent["tag"] == prediction:
                print("Bot:", random.choice(intent["responses"]))

# Run the chatbot
if __name__ == "__main__":
    chat()
