import requests

# 企业微信机器人Webhook地址（支持环境变量）
import os
WEBHOOK_URL = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={os.environ.get('WEBHOOK_KEY', '24713e0da653b98aba4910621440bb6fa6')}"


def send_text_message(content):
    """发送文本消息到企业微信群"""
    url = WEBHOOK_URL
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        }
    }
    response = requests.post(url, json=data)
    result = response.json()
    if result.get("errcode") == 0:
        print("消息发送成功")
        return True
    else:
        print(f"消息发送失败: {result}")
        return False


def send_markdown_message(content):
    """发送markdown消息到企业微信群"""
    url = WEBHOOK_URL
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }
    response = requests.post(url, json=data)
    result = response.json()
    if result.get("errcode") == 0:
        print("Markdown消息发送成功")
        return True
    else:
        print(f"Markdown消息发送失败: {result}")
        return False
