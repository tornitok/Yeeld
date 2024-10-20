from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from support.assertions import Assertions
from config import Secrets, URL


class LoginPage(BaseObject):
    SIGN_IN_BUTTON = (By.XPATH, '//button[contains(@class, "mantine-Button-root") and .="Sign In"]')
    SIGN_IN_WITH_EMAIL_BUTTON = (By.XPATH, '//button[.//span[text()="Sign In With Email"]]')
    SIGN_IN_WITH_PHONE_BUTTON = (By.XPATH, '//button[.//span[text()="Sign In With Phone"]]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '._1e5f8lj1')
    USER_NAME_FIELD = (By.XPATH, '//input[@placeholder="example@gmail.com"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@placeholder="••••••••"]')
    USER_PHONE_FIELD = (By.XPATH, '//input[@type="text"]')
    SECURITY_VERIFICATION_INPUT = (By.XPATH, '//input[@type="tel" and @inputmode="numeric"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '#error_message')
    SEARCH_BOX = (By.XPATH, '//input[@placeholder="Search..."]')
    DROPDOWN = (By.XPATH, '//button[@aria-haspopup="listbox"]')
    DROPDOWN_LIST = (By.XPATH, '//div[@role="listbox"]/div[position()=1]')

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions()

    def auth_flow(self, is_email_flow=True):
        """High-level function to handle email or phone login."""
        if is_email_flow:
            self.sign_in_email_flow()
        else:
            self.sign_in_phone_flow()

    def sign_in_email_flow(self):
        """Handles the email login flow."""
        self.click_sign_in_button()
        self.click_sign_in_with_email()
        self.enter_credentials_email()
        self.complete_login()

    def sign_in_phone_flow(self):
        """Handles the phone login flow."""
        self.click_sign_in_button()
        self.click_sign_in_with_phone()
        self.choose_country_code()
        self.enter_credentials_phone()
        self.complete_login()

    def complete_login(self):
        """Handles common steps after entering credentials."""
        self.click_continue()
        self.enter_verification_code()
        self.click_continue()

    def enter_credentials_email(self):
        """Enter email and password."""
        self.enter_email()
        self.enter_password()

    def enter_credentials_phone(self):
        """Enter phone and password."""
        self.enter_phone()
        self.enter_password()

    def enter_email(self, user_name=Secrets.USER_NAME_CLIENT):
        self.send_keys(self.USER_NAME_FIELD, user_name)

    def enter_phone(self, phone_number=Secrets.PHONE_NUMBER):
        self.send_keys(self.USER_PHONE_FIELD, phone_number)

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

    def choose_country_code(self, default_country_name='Russian Federation'):
        """Selects the country code in the dropdown."""
        self.click(self.DROPDOWN)
        self.send_keys(self.SEARCH_BOX, default_country_name)
        self.click(self.DROPDOWN_LIST)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def is_url_valid(self):
        self.assertion.assert_equal(
            actual=self.get_current_url(),
            expected=URL.MAIN_PAGE
        )

    def is_error_message_correct(self, message):
        actual_message = self.get_text(self.ERROR_MESSAGE)
        self.assertion.assert_equal(expected=message, actual=actual_message)