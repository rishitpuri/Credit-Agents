from langgraph.graph import StateGraph, START, END
from state import CreditAgentState
from nodes import extract_financial_entities, validate_with_web_search

def build_workflow():
    builder = StateGraph(CreditAgentState)
    builder.add_node("extract_entities", extract_financial_entities)
    builder.add_node("validate_web", validate_with_web_search)

    builder.add_edge(START, "extract_entities")
    builder.add_edge("extract_entities", "validate_web")
    builder.add_edge("validate_web", END)

    return builder.compile()


