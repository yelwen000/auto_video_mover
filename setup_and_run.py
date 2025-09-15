# 一键初始化并运行
import os, subprocess, sys

def setup():
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ 依赖安装完成")

def run():
    subprocess.run([sys.executable, "main.py"])

if __name__ == "__main__":
    setup()
    run()
