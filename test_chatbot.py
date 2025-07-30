#!/usr/bin/env python3
"""
Test script for the Solar Chatbot
"""

from chatbot import SolarChatbot
from utils import clean_input

def test_chatbot():
    """Test the chatbot with sample queries"""
    print("Initializing Solar Chatbot...")
    bot = SolarChatbot("data/knowledge.txt")
    
    test_queries = [
        "What types of solar panels do you offer?",
        "How long does installation take?",
        "What do I need for a solar estimate?",
        "Do you provide maintenance services?",
        "How do I book a site visit?",
        "What is the weather like today?"  # This should get a fallback response
    ]
    
    print("\nTesting chatbot responses:")
    print("=" * 50)
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        response = bot.get_response(clean_input(query))
        print(f"Response: {response}")
        print("-" * 30)

if __name__ == "__main__":
    test_chatbot() 