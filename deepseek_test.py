# 名称：sk-cb00e2a5fe1c44e2ae7a464845008adb
# key：deepseek-api-key-01
# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com/v1")

def chat_with_deepseek_chat():
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个乐于助人的助手。"},
            {"role": "user", "content": "介绍一下 Python 的装饰器"}
        ],
        temperature=0.7,        # 控制随机性，仅在 deepseek-chat 中有效
        top_p=0.9,
        max_tokens=1024,         # 输出长度限制
        stream=False
    )
    
    # 打印最终回复
    print(response.choices[0].message.content)

def chat_with_deepseek_reasoner():
    response = client.chat.completions.create(
        model="deepseek-reasoner",   # 使用 reasoner 模型
        messages=[
            {"role": "user", "content": "9.11 和 9.9 哪个数字大？"}
        ],
        # temperature 等参数会被忽略，但传入也不会报错
        max_tokens=2048,              # 可以设置输出长度上限
        stream=False
    )
    
    # 获取推理过程
    reasoning_content = response.choices[0].message.reasoning_content
    # 获取最终答案
    final_content = response.choices[0].message.content
    
    print("=== 推理过程 ===")
    print(reasoning_content)
    print("\n=== 最终答案 ===")
    print(final_content)

if __name__ == "__main__":
    # chat_with_deepseek_chat()
    chat_with_deepseek_reasoner()
