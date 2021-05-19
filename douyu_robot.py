from services.config import Config
from services.douyu_client import DouyuClient
from os import linesep
from datetime import datetime as date

from services.email_client import EmailClient


def add_content(line):
    global content
    content = content.__add__(line).__add__(linesep)


config = Config()
email = EmailClient(config)
date_str = date.now().strftime('%Y-%m-%d')
subject = f"斗鱼机器人🤖 {date_str} 执行报告"
content = ""

douyu = DouyuClient(config)

medals = []
gifts = []
try:
    medals = douyu.get_medals()
    if medals:
        add_content("当前拥有的粉丝牌：")
        for medal in medals:
            add_content(f"  {medal.medal_name}: https://www.douyu.com/{medal.room}")

except Exception as e:
    add_content("获取当前拥有的粉丝牌失败")

try:
    gifts = douyu.get_backpack_gifts()
    if gifts:
        add_content("当前拥有的背包礼物：")
        for gift in gifts:
            add_content(f"  礼物 {gift.name} 数量为：{gift.count}")
except Exception as e:
    add_content("获取当前拥有的背包礼物失败")

add_content("开始斗鱼礼物赠送：")

if medals and gifts:
    for medal in medals:
        try:
            gift = gifts[0]
            douyu.give_gifts(gift.id, gift_count=gift.count)
            add_content(f"  给 {medal.medal_name} 房间赠送{gift.name}成功~, 数量{gift.count}")
        except Exception as e:
            add_content("  给 {medal.medal_name} 房间赠送{gift.name}失败!!!")


email.send(subject, content)
print('执行完成')
