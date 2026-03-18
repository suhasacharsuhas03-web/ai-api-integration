import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def query_huggingface(prompt):
    try:
        # Simulated response (fallback due to API issues)
        return f"Hugging Face Response: Artificial Intelligence is the ability of machines to think and learn like humans. (Prompt: {prompt})"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Querying Hugging Face...")
    result = query_huggingface(user_input)
    print("Response:")
    print(result)