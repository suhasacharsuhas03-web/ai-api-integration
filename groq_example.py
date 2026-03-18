import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ updated working model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Querying Groq...")
    result = query_groq(user_input)
    print("Response:")
    print(result)