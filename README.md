# 📚 LangGraph RAG Demo -- Agentic Document Question Answering

An interactive **Retrieval Augmented Generation (RAG)** system that
allows users to upload a PDF document and ask natural language questions
about its content.

The system retrieves relevant information from the document using
**vector search** and generates grounded answers using a **multi‑agent
reasoning pipeline** powered by LLMs.

------------------------------------------------------------------------

# 🚀 Features

-   Upload a PDF document
-   Ask questions about the document
-   Retrieve relevant chunks from the document
-   Generate answers using an LLM
-   Reflection agent verifies or improves the answer
-   Transparent AI workflow displayed in the UI

------------------------------------------------------------------------

# 🧠 System Architecture

User Question\
↓\
Vector Retrieval (FAISS)\
↓\
Relevant Document Chunks\
↓\
Generator Agent (LLM)\
↓\
Reflection Agent (Answer Verification)\
↓\
Final Answer

------------------------------------------------------------------------

# 🏗 Pipeline Overview

PDF Upload\
↓\
LangChain Loader\
↓\
Text Chunking\
↓\
Embeddings (MiniLM)\
↓\
FAISS Vector Database\
↓\
Retriever Agent\
↓\
Generator Agent (Mixtral LLM)\
↓\
Reflection Agent\
↓\
Final Answer

------------------------------------------------------------------------

# ⚙️ Tech Stack

  Component             Technology
  --------------------- ------------------
  UI                    Streamlit
  Document Processing   LangChain
  Embeddings            all-MiniLM-L6-v2
  Vector Database       FAISS
  LLM                   Mixtral 8x7B
  LLM Gateway           OpenRouter
  Language              Python

------------------------------------------------------------------------

# 🤖 Agent-Based Reasoning Pipeline

### Retriever Agent

Retrieves the most relevant document chunks using vector similarity
search.

### Generator Agent

Uses the LLM to generate an answer using retrieved context.

### Reflection Agent

Reviews the generated answer and improves clarity or correctness.

------------------------------------------------------------------------

# 🖥 Streamlit Interface

The UI displays:

-   Uploaded document preview
-   Top retrieved chunks
-   Context used by the model
-   Initial generated answer
-   Final refined answer
-   Agent workflow

This makes the reasoning process **transparent and explainable**.

------------------------------------------------------------------------

# 📂 Project Structure

langgraph-rag-demo │ ├── app.py ├── agents.py ├── rag_pipeline.py ├──
graph_flow.py ├── requirements.txt └── README.md

------------------------------------------------------------------------

# 🔧 Installation

Clone the repository:

git clone https://github.com/yourusername/langgraph-rag-demo.git\
cd langgraph-rag-demo

Create virtual environment:

python -m venv venv\
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

------------------------------------------------------------------------

# 🔑 Configure API Key

Create an environment variable for OpenRouter:

OPENROUTER_API_KEY=your_api_key_here

------------------------------------------------------------------------

# ▶ Run the Application

streamlit run app.py

------------------------------------------------------------------------

# 🧪 Example Query

Upload a payroll PDF and ask:

"What is the UAN number?"

The system retrieves the relevant chunk and generates a grounded answer.

------------------------------------------------------------------------

# 📈 Future Improvements

Possible extensions:

-   Hybrid search (BM25 + vector search)
-   Reranking models
-   Conversational memory
-   Multi-document support
-   Streaming responses
-   Full LangGraph orchestration
-   Advanced agent workflows

------------------------------------------------------------------------

# 🎯 Learning Outcomes

This project demonstrates:

-   Retrieval Augmented Generation (RAG)
-   Vector similarity search
-   LLM orchestration
-   Multi-agent reasoning
-   Prompt engineering
-   Building interactive AI applications

------------------------------------------------------------------------

# 👩‍💻 Author

**Sisilika Ramaraju**
