import configuration
import requests

def post_create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=order_body)

def get_order_track_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_INFO_PATH + str(track))