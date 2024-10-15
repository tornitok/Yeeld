import os

MESSAGE = 'Test message'
URGENT_MESSAGE = 'Test urgent message'

def test_send_message(chat_page):
    chat_page.log_in()
    chat_page.enter_message(MESSAGE)
    chat_page.send_message()
    chat_page.is_message_sent(MESSAGE)

def test_send_urgent_message(chat_page):
    chat_page.log_in()
    chat_page.enter_message(URGENT_MESSAGE)
    chat_page.set_urgent_flag()
    chat_page.send_message()
    chat_page.is_message_sent(URGENT_MESSAGE)

def test_chat_send_file(chat_page):
    chat_page.log_in()
    image_path = '/Users/klim/Desktop/PsyPsy_tests/files/image.png'
    assert os.path.exists(image_path), f"Image file not found at {image_path}"
    chat_page.send_image(image_path)
    chat_page.is_message_sent()
