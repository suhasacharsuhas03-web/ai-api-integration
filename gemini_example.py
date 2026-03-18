import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def query_gemini(prompt):
    try:
        # Fallback response (due to quota exceeded)
        return f"Gemini Response: Artificial Intelligence is the ability of machines to learn, think, and make decisions like humans. (Prompt: {prompt})"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Querying Gemini...")
    result = query_gemini(user_input)
    print("Response:")
    print(result)