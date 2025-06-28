# AI Chatbot using NLP (Natural Language Processing)
- This project is submitted as part of Task - 3 for the internship with CodTech. It demonstrates the use of NLP libraries in Python to build a basic interactive chatbot that responds to user inputs based on intent classification.

## Objective
- Build an AI-powered chatbot using Natural Language Processing (NLP)

- Train the chatbot to recognize user intents

- Provide relevant responses based on trained data

- Demonstrate text processing and basic machine learning integration

## Features
- Intent-based chatbot using NLTK and scikit-learn

- Responds to user queries like greetings, thanks, farewells, etc.

- Learns patterns from a customizable intents.json file

- Easy to extend with new intents and responses

- Works directly in the terminal/command line

## Tech Stack
- Python

- NLTK – for tokenization

- scikit-learn – for intent classification

- JSON – for storing training data

- Terminal-based interface

## How to Run
- Make sure these files are present:

chatbot.py

intents.json

- Install required libraries:

pip install nltk scikit-learn

- Download NLTK resources (only once):

import nltk
nltk.download('punkt')
nltk.download('wordnet')

- Run the chatbot:

python chatbot.py
Start chatting! Type your queries or type quit to exit.

## File Structure

task3_chatbot/
├── chatbot.py         # Main chatbot logic
├── intents.json       # Predefined patterns and responses
└── README.md          # Project documentation

## Sample Interactions

You: Hello
Bot: Hi there!

You: What is your name?
Bot: I am your CodTech Assistant.

You: Bye
Bot: Goodbye!

## Deliverables
- chatbot.py – Python script for chatbot logic

- intents.json – Training data for intent classification

- README.md – Documentation file

## Author
Sowparnika S
(Intern at CodTech)
