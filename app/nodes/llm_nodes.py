from app.core.llm import LLMFactory

def test_kimi_k2_5_model_stream(message: str):
    llm = LLMFactory.get_model("kimi-k2.5")

    response = llm.stream(message)
    return response

def test_kimi_k2_5_model_invoke(message: str):
    llm = LLMFactory.get_model("kimi-k2.5")

    response = llm.invoke(message)
    return response