"""
Data Analyzer template for AIToolMaker.
"""

DATA_ANALYZER_TEMPLATE = """import streamlit as st
import pandas as pd
import google.generativeai as genai
from api_key import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("{{ model }}")

# Page config
st.set_page_config(page_title="{{ tool_name }}", layout="centered")

st.title("{{ tool_name }}")
st.write("Upload your CSV and ask questions about it.")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    column_names = ", ".join(df.columns)
    
    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Display previous Q&A
    if st.session_state.chat_history:
        st.subheader("Previous Q&A")
        for i, (q, a) in enumerate(st.session_state.chat_history):
            st.markdown(f"**Q{i+1}:** {q}")
            st.markdown(f"**A{i+1}:** {a}")
            st.markdown("---")
    
    # Question input
    user_query = st.text_input("Ask a question about your data")
    
    if user_query:
        with st.spinner("Thinking..."):
            csv_sample = df.to_csv(index=False)
            
            prompt = (
                f"The dataset has the following columns: {column_names}.\\n"
                f"Here are the rows:\\n{csv_sample}\\n"
                f"Now answer this question: {user_query}"
            )
            
            try:
                response = model.generate_content(prompt)
                answer_text = response.text
                
                st.subheader("Answer")
                st.write(answer_text)
                
                # Save to history
                st.session_state.chat_history.append((user_query, answer_text))
                
            except Exception as e:
                st.error(f"Model error: {str(e)}")
"""