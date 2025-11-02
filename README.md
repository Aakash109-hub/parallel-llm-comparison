# ⚡ Parallel LLM Comparison Chatbot

A Streamlit-based web app that compares **two AI models side by side** using a **parallel workflow** powered by **LangGraph**.  
It’s built with `ChatGroq` and `ChatOllama` models running simultaneously for real-time comparison.

<img width="1920" height="938" alt="Screenshot 2025-11-02 162953" src="https://github.com/user-attachments/assets/c876cbd1-ed30-4f64-82e6-91045b2bfd21" />


---

## 🚀 Features

- 🧠 Compare responses from two powerful language models (Groq + Ollama)
- ⚙️ Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- 🎨 Interactive Streamlit frontend with chatbot-style input at the bottom
- 🔄 Parallel execution for real-time response comparison
- 📊 Workflow visualization included (`parallel_workflow_graph.png`)

---

## 🧱 Project Structure

```

parallel-llm-comparison/
│
├── backend.py                # LangGraph flow and model logic
├── frontend.py               # Streamlit user interface
├── .env                      # Contains API keys (not to be shared)
├── requirements.txt          # Python dependencies
├── parallel_workflow_graph.png  # Visual representation of the flow
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Aakash109-hub/parallel-llm-comparison.git
cd parallel-llm-comparison
````

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file

Inside your project folder, add:

```
GROQ_API_KEY="your_groq_api_key_here"
```

Make sure your **Ollama server** is running locally.

---

## ▶️ Run the App

```bash
streamlit run frontend.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🖼️ Workflow Graph

Your parallel flow structure is visualized below:

<img width="295" height="234" alt="parallel_workflow_graph" src="https://github.com/user-attachments/assets/f439e3d6-e3b4-463b-a38c-73d1489e476d" />

---

## 🧩 Example Prompts for Testing

Try these to explore model differences:

* *"Explain quantum computing in simple terms."*
* *"Write a 2-line motivational quote."*
* *"What is LangChain used for?"*
* *"Who invented transformers in AI?"*

---

## 🏗️ Tech Stack

* **Python**
* **LangGraph**
* **LangChain Groq**
* **LangChain Ollama**
* **Streamlit**
* **dotenv**

