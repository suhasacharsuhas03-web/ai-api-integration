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

---

## 📸 Screenshots
Screenshots of outputs are included in the `screenshots` folder.

---

## ⚠️ Notes
- OpenAI and Gemini APIs showed quota errors due to free-tier limitations.
- Hugging Face API endpoints were deprecated/unstable, so fallback responses were used.
- Ollama could not run due to system memory limitations, so fallback response was implemented.
- Cohere API required migration from Generate API to Chat API due to deprecation.

---

## ✅ Conclusion
This project successfully demonstrates:
- Integration of multiple AI APIs
- Secure API key management using environment variables
- Handling real-world API issues like quota limits and deprecations
- Implementation of fallback mechanisms to ensure smooth execution