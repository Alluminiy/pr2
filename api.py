import requests


# a: dict[str, dict[str, dict]]


class RequestManager:
    BASE_URL = 'https://fakestoreapi.com'

    def get(self, endpoint: str):
        response = requests.get(self.BASE_URL + endpoint)
        return response.json()



