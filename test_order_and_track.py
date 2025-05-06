# Белова Татьяна, 29-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_order_and_get_track():
    order_track = sender_stand_request.post_create_order(data.order_body).json()['track']
    response = sender_stand_request.get_order_track_number(order_track)
    assert response.status_code == 200