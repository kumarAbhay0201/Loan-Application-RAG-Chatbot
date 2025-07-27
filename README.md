# 💬 Loan Application RAG Chatbot

This is a **Retrieval-Augmented Generation (RAG)** based chatbot built to answer questions related to past loan applications. It retrieves relevant data from historical loan records and then generates a human-like answer based on the retrieved information.

---

## 🧠 Problem Statement

The goal was to create an **intelligent Q&A chatbot** that could:
- Understand user queries related to loan applications
- Retrieve the most relevant records from a given dataset
- Generate natural language responses from that data

Example user questions:
- *"How can an unemployed woman get a loan?"*
- *"What is the maximum loan amount a man can take?"*

---

## 🚀 Features

- RAG-based architecture
- Lightweight and fully local (no paid APIs)
- Clean UI with **Streamlit**
- Supports semantic search over tabular loan data
- Uses **SentenceTransformer** for embeddings
- Uses **Flan-T5-Small** for answer generation

---


---

## ⚙️ Tech Stack

| Task                  | Technology Used                             |
|-----------------------|---------------------------------------------|
| UI                    | Streamlit                                   |
| Embeddings            | `sentence-transformers` (`MiniLM-L6-v2`)    |
| Vector Search         | FAISS                                        |
| Answer Generation     | `google/flan-t5-small` (via `transformers`) |
| Data Source           | Kaggle CSV dataset                          |

---

## ❗ Limitations & My Honest Effort

I aimed to create **GPT-3-like responses**, but I had to make tradeoffs due to limited resources:

| Constraint | Limitation |
|-----------|------------|
| No credits for GPT/Claude/Gemini | Couldn't use advanced APIs |
| No GPU / low-RAM laptop | Couldn't run heavy LLMs like Mistral or Falcon |
| Slow internet | Couldn't download 10GB models |
| CPU only | Limited to small models like Flan-T5-Small |

Despite all this, I:

- Built the full RAG pipeline from scratch.
- Explored both naive and LLM-based generations.
- Handled CSV-to-text conversion, embedding, search, and summarization.
- Maintained a neat UI for non-tech users.

---

## ✨ What Can Be Improved (If Resources Allow)

- Replace Flan-T5 with **GPT-4**, **Claude**, or **Mistral-7B-Instruct**
- Deploy the app via HuggingFace or Render
- Train a custom model on domain-specific vocabulary
- Add feedback-based learning loop

---

## 💡 Conclusion

This project is a complete proof-of-concept for a document-aware chatbot. While the responses are limited by the model size, the architecture is robust and extensible for production-grade systems.

---

## 👨‍💻 Developed by

**Abhay Kumar**  
B.Tech Student | Datascience Intern at Celebal Technology| Tech Explorer  
Email: [workwithkukmarabhay@gmail.com](mailto:workwithkukmarabhay@gmail.com)

---


