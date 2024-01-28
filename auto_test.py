import sender_stend_reqest
# Коваленков Егор, 12-ая когорта, финальный проект. Инженер по тестированию плюс

def positive_assert(track_order):
    order_response = sender_stend_reqest.get_order_track(track_order)
    assert order_response.status_code == 200

# Тест
def test_get_order_track_success_response():
    positive_assert(sender_stend_reqest.track_order)