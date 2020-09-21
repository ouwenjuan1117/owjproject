import requests


class BaseApi:

    def send_requests(self, req: dict):
        return requests.request(**req)
