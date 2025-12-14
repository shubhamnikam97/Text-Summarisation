# 🦜 LangChain Website Summarizer

A Streamlit-based web application that summarizes content from **websites** using **LangChain** and **Groq LLMs**.  
Simply paste a URL, provide your Groq API key, and get a concise 300-word summary.

---

## 🚀 Features

- 📄 Summarize **any public website**
- 🤖 Powered by **LangChain** and **Groq LLaMA 3.1**
- 🧠 Custom prompt-based summarization
- ⚡ Fast and interactive **Streamlit UI**

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq (LLaMA 3.1 8B Instant)**
- **URL Document Loaders**

---
## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/langchain-url-summarizer.git
cd langchain-url-summarizer
```

2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---
## 🔑 Requirements

Make sure you have:
- Python 3.9+
- A valid Groq API Key

Get your API key from:
👉 https://console.groq.com

---
## ▶️ Running the App
```bash
streamlit run "filepath\app.py"
```

---
## 🧪 How to Use
- Enter your Groq API Key in the sidebar
- Paste a website URL
- Click "Summarize the Content from Website"
- Wait for the summary to be generated 🎉

---
## 🧠 Model Details
- LLM: llama-3.1-8b-instant
- Summarization Chain: load_summarize_chain
- Chain Type: stuff
- Summary Length: ~300 words

---
## 📁 Project Structure
```bash
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

---

