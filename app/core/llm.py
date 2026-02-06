# app/core/llm.py
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from langchain.chat_models import init_chat_model
from app.core.config import settings

class LLMFactory:
    _models_config: Optional[Dict[str, Any]] = None

    @classmethod
    def _load_config(cls):
        """加载 YAML 配置文件"""
        if cls._models_config is None:
            # 获取 config/models.yaml 的绝对路径
            # 假设 llm.py 在 app/core/ 下，配置文件在根目录 config/ 下
            root_dir = Path(__file__).parent.parent.parent
            yaml_path = root_dir / "app" / "core" / "models.yaml"
            
            with open(yaml_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                cls._models_config = data.get("models", {})
        return cls._models_config

    @classmethod
    def get_model(cls, model_key: str, temperature: Optional[float] = None, streaming: bool = True):
        models_defs = cls._load_config()
        info = models_defs.get(model_key)
        
        if not info:
            raise ValueError(f"Model key '{model_key}' not found in models.yaml")

        # 参数优先级逻辑：
        # 1. 如果调用 get_model 时显式传了参数，用传的
        # 2. 否则看 YAML 里有没有定义该模型的固定参数
        # 3. 最后才用全局默认值 0.7
        final_temp = temperature if temperature is not None else info.get("temperature", 0.7)

        env_key_name = info.get("env_key_name")
        api_key = getattr(settings, env_key_name, None) if env_key_name else None

        return init_chat_model(
            model=info["name"],
            model_provider=info["provider"],
            api_key=api_key,
            temperature=final_temp, # 使用计算后的 final_temp
            streaming=streaming,
            base_url=info.get("base_url"),
            **info.get("extra_params", {})
        )