from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from support.assertions import Assertions
from pages.login_page import LoginPage


class ChatPage(LoginPage):
    CHAT_INPUT = (By.CSS_SELECTOR, '#chat-text')
    SEND_BUTTON = (By.CSS_SELECTOR, '.chat-send-button')
    URGENT_FLAG = (By.CSS_SELECTOR, '#urgent_flag')
    UPLOAD_BUTTON = (By.CSS_SELECTOR, '#file-upload')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.send_button')
    CHAT = (By.CSS_SELECTOR, '.sent:last-child .content_text span')
    FILE = (By.CSS_SELECTOR, '.message_image')

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions

    def enter_message(self, text):
        self.send_keys(self.CHAT_INPUT, text)

    def set_urgent_flag(self):
        self.click(self.URGENT_FLAG)

    def send_message(self):
        self.click(self.SEND_BUTTON)

    def send_image(self, image_path: str) -> None:
        self.send_keys(self.UPLOAD_BUTTON, image_path, is_visible=False)
        self.click(self.SUBMIT_BUTTON, is_present=False)

    def send_text_and_image(self, text: str, image_path: str) -> None:
        self.enter_message(text)
        self.send_message()
        self.send_image(image_path)

    def log_in(self):
        self.enter_email()
        self.enter_password()
        self.click_button()

    def is_message_sent(self, message):
        self.assertion.assert_equal(
            expected=message,
            actual=self.get_text(self.CHAT)
        )

    def is_file_sent(self, file_name):
        self.assertion.assert_equal(
            expected=file_name,
            actual=self.get_file(self.FILE)
        )