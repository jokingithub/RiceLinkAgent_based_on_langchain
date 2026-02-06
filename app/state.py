# 定义全局状态结构
# app/state.py
from typing import Annotated, TypedDict, List
from langgraph.graph.message import add_messages

class WorkflowState(TypedDict):
    # add_messages 表示新消息会附加到旧消息后，类似 n8n 的数据追加
    messages: Annotated[List[dict], add_messages] 
    base_info: dict
    next_step: str