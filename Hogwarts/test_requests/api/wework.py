import requests


class WeWork:

    def get_token(self):
        """token 的定义，获取token"""
        # 每个企业都拥有唯一的corpid，获取此信息可在管理后台“我的企业”－“企业信息”
        corp_id = "ww9c9dfb3253386139"
        # # 获取通讯录管理secret，在“管理工具”-“通讯录同步”里面查看
        corp_secret = "ow77plErSKg8EbcJ5n6kPcioaqpgZbGeCoT063nn1Ow"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        # 返回获取到的access_token
        return r.json()["access_token"]