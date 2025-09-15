# 工具函数（日志/重试/路径处理）
import time

def log(msg):
    print(f"[LOG] {time.strftime('%Y-%m-%d %H:%M:%S')} - {msg}")
