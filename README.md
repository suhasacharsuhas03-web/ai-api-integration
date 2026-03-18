# GenAI API Integration Assignment

## 📌 Objective
This project demonstrates integration of multiple Generative AI APIs including OpenAI, Groq, Hugging Face, Google Gemini, Ollama, and Cohere.

---

## 🛠️ Technologies Used
- Python
- OpenAI API
- Groq API
- Hugging Face API
- Google Gemini API
- Ollama (Local AI)
- Cohere API
- dotenv

---

## ⚙️ Setup Instructions

1. Clone or download the project

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file and add your API keys:

   OPENAI_API_KEY=your_key  
   GROQ_API_KEY=your_key  
   HUGGINGFACE_API_KEY=your_key  
   GEMINI_API_KEY=your_key  
   COHERE_API_KEY=your_key  

4. Run any script:
   python groq_example.py

## 🔑 How to Get API Keys

To run this project, you need API keys from the following providers:

- **OpenAI**  
  Get your API key from: https://platform.openai.com/api-keys

- **Groq**  
  Get your API key from: https://console.groq.com/

- **Hugging Face**  
  Get your token from: https://huggingface.co/settings/tokens

- **Google Gemini**  
  Get your API key from: https://makersuite.google.com/app/apikey

- **Cohere**  
  Get your API key from: https://dashboard.cohere.com/

- **Ollama**  
  Download and install from: https://ollama.ai/ (no API key required)
---

## 📸 Screenshots
Screenshots of outputs are included in the `screenshots` folder.

---

## ⚠️ Notes
- OpenAI and Gemini APIs showed quota errors due to free-tier limitations.
- Hugging Face API endpoints were deprecated/unstable, so fallback responses were used.
- Ollama could not run due to system memory limitations, so fallback response was implemented.
- Cohere API required migration from Generate API to Chat API due to deprecation.
- Hugging Face API was unstable due to recent endpoint changes and returned errors.
- Error handling was implemented to manage API failures gracefully.
---

## ✅ Conclusion
This project successfully demonstrates:
- Integration of multiple AI APIs
- Secure API key management using environment variables
- Handling real-world API issues like quota limits and deprecations
- Implementation of fallback mechanisms to ensure smooth execution