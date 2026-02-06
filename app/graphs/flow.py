# app/graphs/research_flow.py
from langgraph.graph import StateGraph, END
from app.state import WorkflowState
from app.nodes.llm_nodes import analyzer_node
from app.nodes.tool_nodes import search_node

workflow = StateGraph(WorkflowState)

# 1. 添加节点
workflow.add_node("analyzer", analyzer_node)
workflow.add_node("search_tool", search_node)

# 2. 设置连线 (Edges)
workflow.set_entry_point("analyzer")
workflow.add_edge("analyzer", "search_tool")
workflow.add_edge("search_tool", END)

app = workflow.compile()