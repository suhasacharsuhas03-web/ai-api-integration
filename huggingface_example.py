import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://router.huggingface.co/hf-inference/models/distilgpt2"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
}

def query_huggingface(prompt):
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt}
        )

        if response.status_code != 200:
            return f"Error: {response.status_code} - API unavailable"

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Querying Hugging Face...")
    print(query_huggingface(user_input))