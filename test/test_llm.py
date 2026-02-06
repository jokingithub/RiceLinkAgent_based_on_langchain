# scripts/test_factory.py
import sys
import os
from pathlib import Path

# 将项目根目录添加到 python 路径，确保能导出 app 模块
sys.path.append(str(Path(__file__).parent.parent))

from app.core.llm import LLMFactory
from langchain_core.language_models.chat_models import BaseChatModel

def test_llm_initialization():
    print("--- 开始测试 LLM 工厂 ---")
    
    # 1. 测试加载特定的模型
    test_models = ["qwen3-max-preview","kimi-k2.5","deepseek-v3.2"] 
    
    for model_key in test_models:
        try:
            print(f"\n正在尝试初始化模型: {model_key}...")
            llm = LLMFactory.get_model(model_key)
            
            # 验证返回的对象类型
            if isinstance(llm, BaseChatModel):
                print(f"✅ 成功! 对象类型: {type(llm)}")
                # 打印模型的一些元数据（可选）
                if hasattr(llm, "model_name"):
                    print(f"   模型名称: {llm.model_name}")
                elif hasattr(llm, "model"):
                    print(f"   模型名称: {llm.model}")
                response = llm.invoke("你好，请自我介绍")
                print(f"模型回复: {response.content}")
            else:
                print(f"❌ 失败: 返回的对象不是预期的 ChatModel 类型")
                
        except Exception as e:
            print(f"❌ 初始化 {model_key} 出错: {e}")

    # 2. 测试不存在的模型（边界情况）
    try:
        print("\n测试不存在的模型标识符...")
        LLMFactory.get_model("non-existent-model")
    except ValueError as e:
        print(f"✅ 成功捕获预期错误: {e}")

if __name__ == "__main__":
    test_llm_initialization()