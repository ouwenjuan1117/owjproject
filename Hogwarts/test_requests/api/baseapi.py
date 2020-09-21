import requests


class BaseApi:

    def send_requests(self, req: dict):
        """为了能够让requests独立出来，将来换技术栈不麻烦，对requests进行二次封装"""
        # req = {
        #     'method':"get",
        #     'url':"xxxxx",
        #     "params":{},
        #     "json":{}
        # }
        # 等同于requests.request('method':"get",'url':"xxxxx","params":{},"json":{} )
        return requests.request(**req)
