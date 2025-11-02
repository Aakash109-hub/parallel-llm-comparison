import streamlit as st
from backend import chatbot_flow

st.set_page_config(page_title="Parallel AI Chatbot", layout="wide")

st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            color: #4B9CD3;
            margin-bottom: 1rem;
        }
        .subtext {
            text-align: center;
            font-size: 1rem;
            color: #777;
            margin-bottom: 2rem;
        }
        .response-box {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 1rem;
            min-height: 200px;
            white-space: pre-wrap;
            font-size: 1rem;
        }
        .separator {
            border-left: 2px solid #ccc;
            height: 100%;
            margin: 0 1rem;
        }
        .bottom-input {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: white;
            padding: 1rem;
            border-top: 1px solid #ddd;
        }
        .stButton>button {
            background-color: #4B9CD3;
            color: white;
            font-weight: 600;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #3b8ac2;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">⚡ Parallel LLM Chatbot — Side-by-Side Intelligence ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Compare real-time responses from two powerful AI models in parallel workflow</div>', unsafe_allow_html=True)

# User input
query = st.text_input("Enter your query:", placeholder="Ask anything...")

# Submit button
if st.button("Generate"):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        with st.spinner("Generating responses..."):
            # Call the backend flow
            result = chatbot_flow.invoke({"query": query})

            # Get responses
            response1 = result.get("response1", "No response from Model 1.")
            response2 = result.get("response2", "No response from Model 2.")

        # Display results side by side
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🧠 Model 1 (ChatGroq)")
            st.write(response1)

        with col2:
            st.subheader("🦙 Model 2 (Ollama)")
            st.write(response2)



