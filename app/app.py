import sys
import os
import streamlit as st
import import_ipynb

# -----------------------
# ADD NOTEBOOK PATH
# -----------------------
notebook_path = "/content/drive/MyDrive/Classroom/DAB_RAG_ZakyProject/notebooks"
sys.path.append(notebook_path)

# -----------------------
# IMPORT YOUR RAG NOTEBOOK
# -----------------------
import academic_advisor_rag_llm  # This loads the notebook
from academic_advisor_rag_llm import rag_answer_with_llm  # Import the RAG function

# -----------------------
# STREAMLIT PAGE SETUP
# -----------------------
st.set_page_config(page_title="DAB - Academic Advisor", layout="wide")

st.markdown("""
<div style="text-align:center;">
    <h1>🎓 DAB</h1>
    <h3>Your smart assistant for academic questions</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#F8FAFC;padding:18px;border-radius:12px;border-left:5px solid #000;">
Ask questions about programs, courses, and requirements. 
The system retrieves relevant information and provides a concise answer.
</div>
""", unsafe_allow_html=True)

# -----------------------
# USER INPUT
# -----------------------
query = st.text_input("Type your question here", placeholder="e.g. What are the requirements for Accounting?")

if st.button("🔍 Search"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Fetching answer..."):
            try:
                # CALL RAG + LLM FUNCTION
                answer, _ = rag_answer_with_llm(query, top_k=3)  # ignore results
                st.subheader("🤖 Answer")
                st.success(answer)
            except Exception as e:
                st.error(f"Error generating answer: {e}")
