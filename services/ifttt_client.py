"""
通过 ifttt 实现手机通知
依然没有微信通知方便~
"""

__author__ = 'weihao.lv'

import json
import requests


class IftttClient():
    """
    ifttt 请求封装 client
    """

    def __init__(self, event, key):
        """
        初始化，通过 event 和 key 绑定一个唯一的 action trigger
        """
        self.event = event
        self.key = key

    def notify(self, **kwargs):
        """
        发送通知：
            请求 trigger 接口 -> 获取 action -> 发送对应 app 账户通知
        """
        url_ = f"https://maker.ifttt.com/trigger/{self.event}/with/key/{self.key}"
        headers_ = {
            'Content-Type': 'application/json'
        }
        payload = {
            "value1": kwargs['content'] if 'content' in kwargs else None,
            "value2": kwargs['sender'] if 'sender' in kwargs else None,
        }
        resp = requests.post(url_, data=json.dumps(payload), headers=headers_)
        print(resp.text)


if __name__ == '__main__':
    client = IftttClient('<event>', '<key>')
    client.notify(content="""
test content
    """)
