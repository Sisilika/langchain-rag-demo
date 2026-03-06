import requests

OPENROUTER_API_KEY = "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"

def call_llm(prompt):

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mixtral-8x7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]
def generate_rag_answer(question, docs):

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant answering questions using the provided document context.

Context:
{context}

Question:
{question}

Answer clearly using the context.
"""

    return call_llm(prompt)

def retrieve_docs(state):

    question = state["question"]
    retriever = state["retriever"]

    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    return {
        **state,
        "docs": docs,
        "context": context
    }

def generate_answer(state):

    question = state.get("question")
    context = state.get("context")
    retriever = state.get("retriever")

    prompt = f"""
You are an AI assistant answering questions from a document.

Context:
{context}

Question:
{question}

Answer clearly using the context.
"""

    answer = call_llm(prompt)

    return {
        "question": question,
        "retriever": retriever,
        "context": context,
        "answer": answer
    }

def reflect_answer(state):

    question = state["question"]
    context = state["context"]
    answer = state["answer"]

    prompt = f"""
You are verifying an answer generated from a document.

Context:
{context}

Question:
{question}

Initial Answer:
{answer}

If the answer is correct, return the same answer clearly.

If the answer is incomplete or incorrect, improve it.

Return ONLY the final improved answer.
Do not explain your reasoning.
"""

    improved = call_llm(prompt)

    return {
        **state,
        "final_answer": improved
    }