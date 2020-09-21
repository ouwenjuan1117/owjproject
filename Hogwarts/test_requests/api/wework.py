import requests

from Hogwarts.test_requests.api.baseapi import BaseApi


class WeWork(BaseApi):

    # # 未封装requests之前的代码
    # def get_token(self):
    #     """token 的定义，获取token"""
    #     # 每个企业都拥有唯一的corpid，获取此信息可在管理后台“我的企业”－“企业信息”
    #     corp_id = "ww9c9dfb3253386139"
    #     # # 获取通讯录管理secret，在“管理工具”-“通讯录同步”里面查看
    #     corp_secret = "ow77plErSKg8EbcJ5n6kPcioaqpgZbGeCoT063nn1Ow"
    #     token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
    #     r = requests.get(url=token_url)
    #     # 返回获取到的access_token
    #     # return r.json()["access_token"]
    #     # 为了之后调用不再每次都传一个token参数，我们可以进行优化，直接通过继承的方式，调用方法即可
    #     self.token = r.json()["access_token"]
    #     return self.token

    # 封装requests之后的代码
    def get_token(self, corp_secret):
        """token 的定义，获取token"""
        # 每个企业都拥有唯一的corpid，获取此信息可在管理后台“我的企业”－“企业信息”
        corp_id = "ww9c9dfb3253386139"
        # # 获取通讯录管理secret，在“管理工具”-“通讯录同步”里面查看
        # corp_secret = "ow77plErSKg8EbcJ5n6kPcioaqpgZbGeCoT063nn1Ow"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        # get_token的请求信息
        req = {
            "method": "get",
            "url": token_url
        }
        # 继承BaseApi之后，调用send_requests方法
        r = self.send_requests(req)
        # 返回获取到的access_token
        # return r.json()["access_token"]
        # 为了之后调用不再每次都传一个token参数，我们可以进行优化，直接通过继承的方式，调用方法即可
        self.token = r.json()["access_token"]
        return self.token
