from langgraph.graph import StateGraph, START, END
from state import CustomerState
from nodes import extract_financial_entities, compute_financial_ratios, assess_risk, generate_explanation

def build_workflow():
    builder = StateGraph(CustomerState)
    builder.add_node("extract_entities", extract_financial_entities)
    builder.add_edge(START, "extract_entities")
    builder.add_edge("extract_entities", END)
    return builder.compile()

