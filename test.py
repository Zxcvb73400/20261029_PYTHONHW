import sys
import os

print("--- 環境檢測開始 ---")

# 1. 輸出 Python 直譯器的完整路徑
interpreter_path = sys.executable
print(f"使用的 Python 路徑: {interpreter_path}")

# 2. 輸出 Conda 環境名稱
# Conda 環境通常會設定這個變數
env_name = os.environ.get('CONDA_DEFAULT_ENV')
print(f"環境名稱 (CONDA): {env_name if env_name else '未啟用 Conda 環境'}")

# 3. 測試 Conda 環境中常見的套件 (例如 numpy)
try:
    import numpy
    print("Numpy 套件: 找到 (表示 Conda 環境正確)")
except ImportError:
    print("Numpy 套件: 未找到 (可能使用非 Conda 或基礎環境)")

print("--- 環境檢測結束 ---")