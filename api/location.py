from uapi import UapiClient
from uapi.errors import UapiError
import os

class Location:
    def __init__(self):
        token = os.getenv("UAPI_KEY")
        self.client = UapiClient(
            base_url="https://uapis.cn",
            token=token,
        )

    def get_user_location(self):
        try:
            result = self.client.network.get_network_myip(source="commercial")
            city = result["region"].split()[-2]
            return city
        except UapiError as exc:
            print(f"API error: {exc}")




if __name__ == '__main__':
    location = Location()
    res = location.get_user_location()
    print(res)