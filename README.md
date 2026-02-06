# RiceLink Agent - 基于 LangChain 的智能工作流系统

一个基于 LangChain 和 LangGraph 构建的灵活、可扩展的 AI 智能体系统，支持多个 LLM 服务商集成，用于构建复杂的多步骤工作流。

## 🌟 主要特性

- **多 LLM 支持**：集成 OpenAI、DashScope（通义千问）、Moonshot（Kimi）、DeepSeek、Anthropic 等多个 LLM 服务商
- **灵活的工作流框架**：基于 LangGraph 构建有向无环图（DAG）工作流
- **模块化架构**：清晰的代码组织结构，易于扩展和维护
- **节点系统**：支持 LLM 节点、逻辑节点、工具调用节点等多种节点类型
- **完整的日志系统**：内置日志记录和调试功能
- **环境配置管理**：使用 Pydantic 进行配置管理，支持 .env 文件

## 📁 项目结构

```
.
├── app/                          # 主应用程序目录
│   ├── main.py                   # 应用入口点
│   ├── server.py                 # 服务器启动配置
│   ├── state.py                  # 工作流状态定义
│   ├── core/                     # 核心模块
│   │   ├── config.py             # 配置管理（API Keys 等）
│   │   ├── llm.py                # LLM 集成和初始化
│   │   ├── logger.py             # 日志系统
│   │   └── models.yaml           # 模型配置文件
│   ├── graphs/                   # 工作流图定义
│   │   └── flow.py               # 主工作流图
│   ├── nodes/                    # 节点定义
│   │   ├── llm_nodes.py          # LLM 相关节点
│   │   ├── logic_nodes.py        # 逻辑处理节点
│   │   └── tool_nodes.py         # 工具调用节点
│   ├── tools/                    # 自定义工具库
│   ├── prompts/                  # 提示词模板
│   └── logs/                     # 日志输出目录
├── test/                         # 测试模块
│   └── test_llm.py              # LLM 功能测试
├── pyproject.toml                # Python 项目配置
├── langgraph.json                # LangGraph 配置
└── README.md                     # 项目文档
```

## 🚀 快速开始

### 环境要求

- Python 3.9 或更高版本
- pip 或其他 Python 包管理器

### 安装

1. 克隆项目：
```bash
git clone <repository-url>
cd RiceLinkAgent_based_on_langchai
```

2. 安装依赖：
```bash
pip install -e .
# 或
pip install -r requirements.txt
```

### 配置

在项目根目录创建 `.env` 文件，配置所需的 API Keys：

```bash
# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_API_BASE=https://api.openai.com/v1

# DashScope (通义千问)
DASHSCOPE_API_KEY=sk-...

# Moonshot (Kimi)
KIMI_API_KEY=sk-...

# DeepSeek
DEEPSEEK_API_KEY=sk-...

# Anthropic
ANTHROPIC_API_KEY=sk-...

# OpenRouter
OPENROUTER_API_KEY=sk-...

# LangChain 追踪（可选）
LANGCHAIN_TRACING_V2=false
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT=my-workflow-app
```

> ⚠️ **注意**：不要将实际的 API Keys 提交到版本控制。始终将 `.env` 文件添加到 `.gitignore`。

### 运行

启动应用：
```bash
python app/main.py
```

或启动服务器：
```bash
python app/server.py
```

运行测试：
```bash
pytest test/
```

## 📚 核心概念

### State（状态）
定义在 [app/state.py](app/state.py) 中，代表工作流执行过程中的状态和数据。

### Graph（工作流图）
定义在 [app/graphs/flow.py](app/graphs/flow.py) 中，使用 LangGraph 构建的有向无环图，定义了节点间的执行流程。

### Nodes（节点）

#### LLM 节点
位于 [app/nodes/llm_nodes.py](app/nodes/llm_nodes.py)，用于调用 LLM 进行推理和生成。

#### 逻辑节点
位于 [app/nodes/logic_nodes.py](app/nodes/logic_nodes.py)，用于条件判断、数据转换等逻辑处理。

#### 工具节点
位于 [app/nodes/tool_nodes.py](app/nodes/tool_nodes.py)，用于集成外部工具和 API 调用。

### Tools（工具）
定义在 [app/tools/](app/tools/) 目录，包含可被 Agent 调用的各类工具函数。

### Config（配置）
定义在 [app/core/config.py](app/core/config.py)，使用 Pydantic 管理所有配置和环境变量。

## 🔧 配置管理

项目使用 Pydantic Settings 进行配置管理，所有配置项必须与 `.env` 文件中的键名完全一致：

```python
from app.core.config import settings

# 获取配置值
api_key = settings.OPENAI_API_KEY
```

## 📖 使用示例

### 创建简单的工作流

```python
from app.graphs.flow import create_workflow
from app.state import State

# 创建工作流
workflow = create_workflow()

# 执行工作流
result = workflow.invoke({
    # 初始输入
})
```

### 添加自定义节点

1. 在 [app/nodes/](app/nodes/) 目录创建节点函数
2. 在 [app/graphs/flow.py](app/graphs/flow.py) 中添加到工作流图
3. 配置节点之间的连接

## 🧪 测试

项目包含测试套件，位于 [test/](test/) 目录：

```bash
# 运行所有测试
pytest test/ -v

# 运行特定测试
pytest test/test_llm.py -v
```

## 📝 日志

项目使用 Python 的 logging 模块，配置在 [app/core/logger.py](app/core/logger.py)：

```python
from app.core.logger import get_logger

logger = get_logger(__name__)
logger.info("消息")
```

日志输出到 [app/logs/](app/logs/) 目录。

## 🤝 扩展性

### 添加新的 LLM 服务商

1. 在 [app/core/config.py](app/core/config.py) 中添加 API Key 配置
2. 在 [app/core/llm.py](app/core/llm.py) 中实现初始化逻辑
3. 在 [app/core/models.yaml](app/core/models.yaml) 中定义模型信息

### 添加新的工具

1. 在 [app/tools/](app/tools/) 目录创建工具文件
2. 定义工具函数，使用 LangChain 的 tool 装饰器
3. 在节点中调用和集成

## 📋 依赖

主要依赖包括：
- `langchain` - LLM 应用框架
- `langgraph` - 工作流图构建
- `pydantic` - 数据验证和配置管理
- `python-dotenv` - 环境变量管理

详见 [pyproject.toml](pyproject.toml)

## 🐛 故障排除

### API Key 问题
- 确认 `.env` 文件中的 API Keys 正确配置
- 检查 API Key 是否有效且未过期
- 验证 API 请求限额和权限

### LLM 调用失败
- 查看 [app/logs/](app/logs/) 中的日志文件
- 确认网络连接正常
- 检查模型名称是否正确（[app/core/models.yaml](app/core/models.yaml)）

### 导入错误
- 确认已安装所有依赖：`pip install -e .`
- 检查 Python 版本是否满足要求

## 📄 许可证

此项目采用 MIT 许可证。详见 LICENSE 文件。

## 📧 联系方式

如有问题或建议，请提交 Issue 或 Pull Request。

---

**最后更新**: 2026年2月6日
