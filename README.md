# 📚 Academic Advisor RAG System (Arabic + English)

**Description:**  
This project, part of the Zakey LLM Bootcamp, is a RAG-based chatbot that acts as an academic advisor for students at California State University and the University of the People. It answers questions about courses, graduation requirements, academic policies, and registration rules. The system supports both Arabic and English queries, providing accurate, context-aware guidance.

---

## 🏗 Project Functionalities

1. **Multilingual Question Handling**  
   - Detects if a question is in Arabic or English  
   - Translates Arabic questions to English for processing  
   - Translates the answer back to Arabic if needed  

2. **RAG-Based Context Retrieval**  
   - Uses FAISS for fast semantic search  
   - Retrieves the most relevant chunks from the academic catalog dataset  

3. **Context-Aware Answer Generation**  
   - Generates answers strictly based on retrieved content  
   - Avoids hallucinations by relying on real catalog data  

4. **User Interface**  
   - Provides an interactive web app for students  
   - Supports real-time queries in Arabic and English  

---

## 🛠 Tools Used

| Part | Tool / Library | Purpose |
|------|----------------|---------|
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`) | Convert questions and catalog chunks into vector embeddings |
| Vector Search | `faiss` | Efficient similarity search over embeddings |
| LLM / Chat & Translation | Groq `llama-3.3-8b-versatile` | Answer generation and Arabic ↔ English translation |
| UI | `streamlit`, `ngrok` | Interactive web interface for students |
| Data | `pandas`, `json` | Dataset management and preprocessing |

## 🎬 Demo

![Demo](DAB%20gif.gif)


