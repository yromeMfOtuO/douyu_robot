import json
import requests

class DouyuClient:
    __headers = {
        # 'authority': 'www.douyu.com',
        # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        # 'accept': 'application/json, text/plain, */*',
        # 'x-requested-with': 'XMLHttpRequest',
        # 'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        # 'content-type': 'application/x-www-form-urlencoded',
        # 'origin': 'https://www.douyu.com',
        # 'sec-fetch-site': 'same-origin',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-dest': 'empty',
        # 'referer': 'https://www.douyu.com/417813',
        # 'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': 'dy_did=481f21aebf814b417b0242c300081501; acf_did=481f21aebf814b417b0242c300081501; PHPSESSID=iil2s5p1kq13u1ij8jbpu1bab6; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2F022%2F19%2F19%2F35_avatar_; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1619527597; acf_auth=f349SDur%2FJM6Wtdr2pXUeYEqlpU4Js2o%2BoX53lyFULvdGTPYslJ7RAeMLoVrtPahnSRE6zuH3jrwU9EkGooCe7CAna%2B947iSMfFRJECG8oHFNyxeYPyKmPcE; dy_auth=f781sCnUGCCC2RaIQTmC3JKmBB3FxRDLfrhC9R9PqFwSZJbhz%2BPzf8HCf9URxFaLzxgdIV38x2c%2FoeCqqAPr6NJr8Ey8rl4IhaBsUy3dmrzuUgF29G68s5MP; wan_auth37wan=1f55c2ff2d32nTZp2Aubh%2BJ1vrxpLBrKlZPJmPsOtQI1R0L4UFilkU7O1jyaSc17PXJOO73%2FV9UHRnEwdHQg3s%2FNUWuAqzLD%2BBsmupZ4pplDuPsAAQ; acf_uid=22191935; acf_username=qq_d8UckaWl; acf_nickname=%E5%91%86%E5%91%86%E5%91%86%E5%91%86%E8%AF%97%E4%BA%BA; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=44434536; acf_biz=1; acf_stk=57d61f85a29e579f; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1621345549',
    }

    def __init__(self, config) -> None:
        self.__room_id = config.properties['giftConfig']['roomId']
        self.__acf_did = config.properties['douyuCookies']['acf_did']
        self.__acf_auth = config.properties['douyuCookies']['acf_auth']
        self.__headers['referer'] = f"https://www.douyu.com/{self.__room_id}"
        self.__cookies = {
            # "dy_did": "481f21aebf814b417b0242c300081501",
            "acf_did": self.__acf_did,
            # "PHPSESSID": "iil2s5p1kq13u1ij8jbpu1bab6",
            "acf_auth": self.__acf_auth  # 这个是关键 cookie
            # "dy_auth": "f781sCnUGCCC2RaIQTmC3JKmBB3FxRDLfrhC9R9PqFwSZJbhz%2BPzf8HCf9URxFaLzxgdIV38x2c%2FoeCqqAPr6NJr8Ey8rl4IhaBsUy3dmrzuUgF29G68s5MP"
        }

    def give_gifts(self, gift_id, gift_count=10):
        data = {
            'propId': gift_id,
            'propCount': str(gift_count),
            'roomId': f"{self.__room_id}",
            'bizExt': '{"yzxq":{}}'  # 暂时未用到的参数
        }
        try:
            response = requests.post('https://www.douyu.com/japi/prop/donate/mainsite/v1',
                                     headers=self.__headers, data=data, cookies=self.__cookies)
            # print(response.text)
            if response.status_code != 200:
                raise Exception(f"请求错误，异常码：{response.status_code}")
            result = json.loads(response.text)
            if result['error'] != 0:
                raise Exception(f"礼物赠送失败，失败原因：{result['msg']}")
        except Exception as e:
            raise Exception(e)

