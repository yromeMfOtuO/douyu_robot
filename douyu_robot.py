from datetime import datetime as date
from os import linesep

from services.config import VisionConfig
from services.douyu_client import DouyuClient
from services.email_client import EmailClient


def add_content(line):
    global content
    content = content.__add__(line).__add__(linesep)


config = VisionConfig()
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
            add_content(f"    {medal.medal_name}: https://www.douyu.com/{medal.room}")

except Exception as e:
    print(e)
    add_content("获取当前拥有的粉丝牌失败！！！")

try:
    gifts = douyu.get_backpack()
    if gifts:
        add_content("当前拥有的背包礼物：")
        for gift in gifts:
            add_content(f"    礼物 {gift.name} 数量为：{gift.amount}")
    else:
        add_content("当前背包为空！！！")
except Exception as e:
    print(e)
    add_content("获取当前拥有的背包礼物失败！！！")

if medals and gifts:
    add_content("开始斗鱼礼物赠送：")
    medal_amount = len(medals)
    for medal in medals:
        for index, gift in enumerate(gifts):
            try:
                gift_count = gift.amount
                amount = gift_count // medal_amount \
                    if len(gifts) - 1 - index else gift_count // medal_amount + gift_count % medal_amount
                douyu.give_gifts(gift.id, gift_amount=amount)
                add_content(f"    给 {medal.medal_name} 房间赠送{gift.name}成功~, 数量{gift_count}")
            except Exception as e:
                print(e)
                add_content(f"    给 {medal.medal_name} 房间赠送{gift.name}失败!!!")

email.send(subject, content)
print('执行完成')
