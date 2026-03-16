# 名称：sk-cb00e2a5fe1c44e2ae7a464845008adb
# key：deepseek-api-key-01
# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
import json

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


def multi_turn_with_reasoner():
    messages = [
        {"role": "user", "content": "解释一下什么是量子纠缠"}
    ]
    
    # 第一轮调用
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=messages,
        stream=False
    )
    
    # 记录本轮回复
    reasoning = response.choices[0].message.reasoning_content
    answer = response.choices[0].message.content
    
    # 打印推理过程和最终答案
    print("【第一轮推理】\n", reasoning)
    print("【第一轮答案】\n", answer)
    
    # 准备下一轮对话：将上一轮的最终答案作为助手消息加入历史
    # 注意：不要加入 reasoning_content
    messages.append({"role": "assistant", "content": answer})
    
    # 加入新的用户问题
    messages.append({"role": "user", "content": "那它在量子计算中有什么应用？"})
    
    # 第二轮调用
    response2 = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=messages,
        stream=False
    )
    
    # 打印第二轮结果
    print("\n【第二轮推理】\n", response2.choices[0].message.reasoning_content)
    print("【第二轮答案】\n", response2.choices[0].message.content)

def chat_with_thinking_using_chat_model():
    response = client.chat.completions.create(
        model="deepseek-chat",   # 使用 chat 模型
        messages=[
            {"role": "user", "content": "计算 23 * 17 的结果，并分步解释"}
        ],
        extra_body={
            "thinking": {"type": "enabled"}   # 开启思考模式
        },
        stream=False
    )
    
    # 此时响应中也会包含 reasoning_content 字段
    reasoning = response.choices[0].message.reasoning_content
    final = response.choices[0].message.content
    
    print("=== 推理过程 ===")
    print(reasoning)
    print("\n=== 最终答案 ===")
    print(final)

def chat_with_request():
    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('DEEPSEEK_API_KEY')}"
        },
        json={
            "model": "deepseek-reasoner",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ],
            "stream": False
        }
    )
    print(response)
    print(response.json())
    print(json.loads(response.text)['choices'][0]['message']['reasoning_content'])
    print(json.loads(response.text)['choices'][0]['message']['content'])

if __name__ == "__main__":
    # chat_with_deepseek_chat()
    # chat_with_deepseek_reasoner()
    # multi_turn_with_reasoner()
    # chat_with_thinking_using_chat_model()
    chat_with_request()


