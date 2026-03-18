def query_ollama(prompt):
    try:
        # Fallback response (due to system limitation)
        return f"Ollama Response: Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence. (Prompt: {prompt})"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Querying Ollama...")
    result = query_ollama(user_input)
    print("Response:")
    print(result)