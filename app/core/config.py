# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # --- 这里的变量名必须与 .env 中的键名完全一致 ---
    
    # OpenAI / 默认
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_API_BASE: str = "https://api.openai.com/v1"

    # DashScope (通义千问) - 建议单独定义，不要和 OpenAI 混用
    DASHSCOPE_API_KEY: Optional[str] = None
    
    # Moonshot (Kimi)
    KIMI_API_KEY: Optional[str] = None
    
    # DeepSeek
    DEEPSEEK_API_KEY: Optional[str] = None

    # Anthropic
    ANTHROPIC_API_KEY: Optional[str] = None

    # OpenRouter
    OPENROUTER_API_KEY: Optional[str] = None

    # LangChain Tracing
    LANGCHAIN_TRACING_V2: bool = False
    LANGCHAIN_API_KEY: Optional[str] = None
    LANGCHAIN_PROJECT: str = "my-workflow-app"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()