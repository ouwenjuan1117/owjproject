from Hogwarts.test_requests_homework.api.wework import WeWork


class TagManagement(WeWork):

    def create_tag(self, tag_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {
            "tagname": "hogwarts",
            "tagid": tag_id
        }
        req = {
            "method": "post",
            "url": create_url,
            "json": data
        }
        # 继承BaseApi之后，调用send_requests方法
        r = self.send_requests(req)
        # return 获取到的响应体
        return r.json()

    def update_tag(self, tag_id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagid": tag_id,
            "tagname": "广州研发中心"
        }
        req = {
            "method": "post",
            "url": update_url,
            "json": data
        }
        # 继承BaseApi之后，调用send_requests方法
        r = self.send_requests(req)
        # return 获取到的响应体
        return r.json()

    def delete_tag(self, tag_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        req = {
            "method": "get",
            "url": delete_url
        }
        r = self.send_requests(req)
        # return 获取到的响应体
        return r.json()

    def get_tag_list(self):
        get_tag_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        data = {
            "errcode": 0,
            "errmsg": "ok",
            "taglist": [
                {"tagid": 1, "tagname": "a"},
                {"tagid": 2, "tagname": "b"}
            ]
        }
        req = {
            "method": "get",
            "url": get_tag_list_url,
            "json": data
        }
        # 继承BaseApi之后，调用send_requests方法
        r = self.send_requests(req)
        # return 获取到的响应体
        return r.json()
