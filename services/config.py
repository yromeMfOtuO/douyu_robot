import json
import os

import requests


class Config:
    """配置类从当前路径或者上级路径读取配置"""

    def __init__(self) -> None:
        # 获取config_path，向上寻找两级目录
        if os.path.exists('./douyu_config.json'):
            config_path = './douyu_config.json'
        elif os.path.exists('../douyu_config.json'):
            config_path = '../douyu_config.json'
        elif os.path.exists('../../douyu_config.json'):
            config_path = '../../douyu_config.json'
        else:
            raise Exception('未找到配置文件')

        with open(config_path) as f:
            load = json.load(f)
            print(load)
        self.properties = load

    def print(self):
        print(self.properties)


class VisionConfig:
    """
    从 vision 项目获取配置
    """
    def __init__(self):
        try:
            resp = requests.get("http://<ip>:<port>/client/config", params={"name": "douyu"})
            self.properties = json.loads(resp.content)['data']
            print(self.properties)
        except Exception as e:
            print(e)
            raise Exception("从 vision 获取配置异常")

    def print(self):
        print(self.properties)


if __name__ == '__main__':
    config = Config()
    config.print()

    vision_config = VisionConfig()
    vision_config.print()

