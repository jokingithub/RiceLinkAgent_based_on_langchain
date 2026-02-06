# app/core/logger.py
import sys
from loguru import logger
from app.core.config import settings

def setup_logger():
    # 移除默认配置
    logger.remove()

    # 配置控制台输出 (带颜色)
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG" if settings.DEBUG else "INFO",
    )

    # 配置定期滚动的文件输出 (用于生产环境审计)
    logger.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="00:00",  # 每天零点创建一个新文件
        retention="30 days", # 保留30天
        compression="zip", # 压缩旧日志
        level="INFO",
        enqueue=True # 异步写入，不影响 AI 响应速度
    )

    return logger

# 实例化
app_logger = setup_logger()