import configuration
import data
import requests

# 1. запрос на создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                    json=order_body,
                    headers=data.headers)
response = post_new_order(data.order_body)

# 2. сохранить номер трека заказа
track_order = response.json()["track"]


# 3. выполнить запрос на получение заказа по треку заказа
def get_order_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDER,
                        params={"t": track_order})