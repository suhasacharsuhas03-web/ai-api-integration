import os
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.chat(
            model="command-r-plus-08-2024",   #  currently supported model
            message=prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Querying Cohere...")
    result = query_cohere(user_input)
    print("Response:")
    print(result)