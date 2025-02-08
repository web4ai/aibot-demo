import requests


class MeituanAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_restaurants(self, location):
        """
        获取指定位置的餐厅列表
        :param location: 位置 (例如: "北京")
        :return: 餐厅列表
        """
        url = f"{self.base_url}/restaurants"
        params = {
            "location": location,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_menu(self, restaurant_id):
        """
        获取指定餐厅的菜单
        :param restaurant_id: 餐厅ID
        :return: 菜单列表
        """
        url = f"{self.base_url}/restaurants/{restaurant_id}/menu"
        params = {
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def place_order(self, restaurant_id, items):
        """
        下订单
        :param restaurant_id: 餐厅ID
        :param items: 订单项列表
        :return: 订单详情
        """
        url = f"{self.base_url}/orders"
        data = {
            "restaurant_id": restaurant_id,
            "items": items,
            "api_key": self.api_key
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()


# 示例用法
if __name__ == "__main__":
    base_url = "https://api.meituan.com"
    api_key = "your_api_key_here"

    meituan_api = MeituanAPI(base_url, api_key)

    # 获取餐厅列表
    location = "北京"
    restaurants = meituan_api.get_restaurants(location)
    print("餐厅列表:", restaurants)

    # 获取指定餐厅的菜单
    if restaurants:
        restaurant_id = restaurants[0]["id"]
        menu = meituan_api.get_menu(restaurant_id)
        print("菜单列表:", menu)

        # 下订单
        items = [{"item_id": menu[0]["id"], "quantity": 1}]
        order = meituan_api.place_order(restaurant_id, items)
        print("订单详情:", order)
