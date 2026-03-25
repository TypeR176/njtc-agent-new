from uapi import UapiClient
from uapi.errors import UapiError
import os
import time


class HotBoard:
    def __init__(self):
        token = os.getenv("UAPI_KEY")
        self.client = UapiClient(
            base_url="https://uapis.cn",
            token=token,
        )

    def get_hotboard(self):
        try:
            result = self.client.misc.get_misc_hotboard(type="douyin", time=int(time.time() * 1000), keyword="", time_start=0, time_end=0, limit=0,
                                                   sources=False)
            hot_str = ""
            # 获取热榜列表，无数据时默认为空列表
            hot_list = result.get("list", [])
            hot_list = hot_list[:10]

            # 遍历所有热点，提取需要的三个字段
            for index, item in enumerate(hot_list, 1):
                title = item.get("title", "无标题")
                hot_value = item.get("hot_value", "无热度")
                url = item.get("url", "无链接")

                # 拼接单条热点（格式可自定义），每条占一行
                hot_str += f"第{index}名：标题={title} | 热度={hot_value} | 链接={url}\n"

            # 如果没有热点，返回提示
            if not hot_str:
                return "未获取到热点数据"

            # 返回最终的普通字符串
            return hot_str.strip()  # strip()去掉最后一个换行
        except UapiError as exc:
            print(f"API error: {exc}")

if __name__ == '__main__':
    hot = HotBoard()
    print(hot.get_hotboard())