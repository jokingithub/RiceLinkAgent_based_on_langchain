from app.nodes.llm_nodes import test_kimi_k2_5_model_stream, test_kimi_k2_5_model_invoke

# 调用测试
stream_iter = test_kimi_k2_5_model_stream("请讲个笑话")

print("Kimi 正在输入: ", end="")
for chunk in stream_iter:
    # chunk 是一个消息块对象，我们需要取其中的 .content
    print(chunk.content, end="", flush=True)
print("\n[生成完毕]")

# 调用测试  
invoke_response = test_kimi_k2_5_model_invoke("你好")
print(invoke_response)