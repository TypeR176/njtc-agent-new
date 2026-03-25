from uapi import UapiClient
from uapi.errors import UapiError
import os
import json

# 类名规范：首字母大写
class Weather:
    def __init__(self):
        token = os.getenv("UAPI_KEY")
        self.client = UapiClient(
            base_url="https://uapis.cn",
            token=token
        )

    def get_weather_data(self, city):
        try:
            result = self.client.misc.get_misc_weather(city=city)
            weather_str = (
                f"城市：{result.get('city', city)}\n"
                f"天气：{result.get('weather')}\n"
                f"当前温度：{result.get('temperature')}℃\n"
                f"体感温度：{result.get('feels_like')}℃\n"
                f"湿度：{result.get('humidity')}%\n"
                f"风向：{result.get('wind_direction')}\n"
                f"风力：{result.get('wind_power')}\n"
                f"空气质量：{result.get('aqi_category')}\n"
                f"更新时间：{result.get('report_time')}"
            )
            return weather_str
        except UapiError as exc:
            print(f"API error: {exc}")
            return None

if __name__ == '__main__':
    weather = Weather()
    res = weather.get_weather_data("内江")
    print(res)
    print(type(res))