from services.config import Config
from services.douyu_client import DouyuClient

config = Config()
douyu = DouyuClient(config)
douyu.give_gifts(config.properties['giftConfig']['giftId'])
