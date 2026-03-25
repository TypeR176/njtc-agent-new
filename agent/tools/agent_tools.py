from langchain_core.tools import tool
from rag.rag_service import RagSummarizeService
import random
from api.weather import Weather
from api.location import Location
from api.hotboard import HotBoard

rag = RagSummarizeService()
weather = Weather()
location = Location()
hotboard = HotBoard()

user_ids = ["1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008"]
month_arr = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06", "2025-07", "2025-08",
             "2025-09", "2025-10", "2025-11", "2025-12"]

user_names = ["薛俊豪", "朱建磊", "付玺铮", "李新阳"]

external_data = {}

@tool(description="从向量存储中检索参考资料")
def rag_summarize(query: str) -> str:
    return rag.rag_summarize(query)

@tool(description="获取用户的姓名，以纯字符串形式返回")
def get_user_name() -> str:
    return random.choice(user_names)

@tool(description="获取当前月份，以纯字符形式返回")
def get_current_month() -> str:
    return random.choice(month_arr)

@tool(description="获取指定城市的天气，传入city城市名字，以纯字符串的形式返回")
def get_weather(city: str) -> str:
    return weather.get_weather_data(city)

@tool(description="获取用户所在城市的名称，以纯字符串形式返回")
def get_user_location() -> str:
    return location.get_user_location()

@tool(description="获取用户的ID，以纯字符串形式返回")
def get_user_id() -> str:
    return random.choice(user_ids)

@tool(description="获取实时热点信息")
def get_hotboard() -> str:
    return hotboard.get_hotboard()