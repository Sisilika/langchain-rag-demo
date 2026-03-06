from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents import retrieve_docs, generate_answer, reflect_answer


class AgentState(TypedDict):
    question: str
    retriever: object
    context: str
    docs: list
    answer: str
    final_answer: str


workflow = StateGraph(AgentState)

workflow.add_node("retrieve", retrieve_docs)
workflow.add_node("generate", generate_answer)
workflow.add_node("reflect", reflect_answer)

workflow.set_entry_point("retrieve")

workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "reflect")
workflow.add_edge("reflect", END)

app = workflow.compile()