from time import sleep
from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from support.assertions import Assertions
from config import Secrets, URL


class LoginPage(BaseObject):
    SIGN_IN_BUTTON = (By.XPATH, '//button[contains(@class, "mantine-Button-root") and .="Sign In"]')
    SIGN_IN_WITH_EMAIL_BUTTON = (By.CSS_SELECTOR, 'button.mantine-focus-auto:nth-child(2)')
    SIGN_IN_WITH_PHONE_BUTTON = (By.CSS_SELECTOR, 'button.mantine-focus-auto:nth-child(1)')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '._1e5f8lj1')
    USER_NAME_FIELD = (By.XPATH, '//input[@placeholder="example@gmail.com"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@placeholder="••••••••"]')
    USER_PHONE_FIELD = (By.XPATH, '//input[@placeholder="(00)0000-0000"')
    SECURITY_VERIFICATION_INPUT = (By.XPATH, '//input[@type="tel" and @inputmode="numeric"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '#error_message')
    DROPDOWN = (By.XPATH, '//input[@type="tel" and @type ="button"]')
    DROPDOWN_LIST = (By.XPATH, '//input[@type="tel" and @type ="button"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions

    def auth_flow(self, is_email_flow=True):
        if is_email_flow:
            self.sign_in_email_flow()
        else:
            self.sign_in_phone_flow()

    def enter_email(self, user_name=Secrets.USER_NAME_CLIENT):
        self.send_keys(self.USER_NAME_FIELD, user_name)

    def enter_phone(self, phone_number=Secrets.PHONE_NUMBER):
        self.send_keys(self.SIGN_IN_WITH_PHONE_BUTTON, phone_number)

    def enter_password(self, password=Secrets.PASSWORD_CLIENT):
        self.send_keys(self.PASSWORD_FIELD, password)

    def enter_verification_code(self, code=Secrets.VERIFICATION_CODE):
        self.send_keys(self.SECURITY_VERIFICATION_INPUT, code)

    def click_sign_in_button(self):
        self.click(self.SIGN_IN_BUTTON)

    def click_sign_in_with_email(self):
        self.click(self.SIGN_IN_WITH_EMAIL_BUTTON)

    def click_sign_in_with_phone(self):
        self.click(self.SIGN_IN_WITH_PHONE_BUTTON)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def enter_credentials(self):
        self.enter_email()
        self.enter_password()

    def sign_in_email_flow(self):
        self.click_sign_in_button()
        self.click_sign_in_with_email()
        self.enter_credentials()
        self.click_continue()
        self.enter_verification_code()
        self.click_continue()

    def sign_in_phone_flow(self):
        self.click_sign_in_button()
        self.click_sign_in_with_phone()
        self.enter_password()
        self.click_continue()

    def is_error_message_correct(self, message):
        self.assertion.assert_equal(
            expected=message,
            actual=self.get_text(self.ERROR_MESSAGE)
        )

    def is_url_valid(self):
        sleep(3)
        self.assertion.assert_equal(
            actual=self.get_current_url(),
            expected=URL.MAIN_PAGE
        )