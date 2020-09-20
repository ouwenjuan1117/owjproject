import pytest
import requests

class TestToken:

    # 三条用例，一条正常的，一条corp_id不填，一条corp_secret不填,之后断言
    # 前面定义的是参数的名称，后面定义的是参数的具体值
    @pytest.mark.parametrize("corp_id,corp_secret,errmsgassert", [
        ("ww9c9dfb3253386139", "ow77plErSKg8EbcJ5n6kPcioaqpgZbGeCoT063nn1Ow", "ok"),
        ("", "ow77plErSKg8EbcJ5n6kPcioaqpgZbGeCoT063nn1Ow", "corpid missing"),
        ("ww9c9dfb3253386139", "", "corpsecret missing")])

    # 在定义方法的时候，需要定义出来pytest装饰器中定义的形参
    def test_token(self, corp_id, corp_secret, errmsgassert):
        """
        单接口测试校验
        """
        # 每个企业都拥有唯一的corpid，获取此信息可在管理后台“我的企业”－“企业信息”
        # corp_id = "ww9c9dfb3253386139"
        # # 获取通讯录管理secret，在“管理工具”-“通讯录同步”里面查看
        # corp_secret = "ow77plErSKg8EbcJ5n6kPcioaqpgZbGeCoT063nn1Ow"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        # 获取到接口的响应体
        # print(r.json())
        # 校验必填逻辑是否生效
        # assert r.json()['errmsg'] == "ok"
        assert r.json()['errmsg'] == errmsgassert
