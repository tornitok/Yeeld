from time import sleep

import pytest

@pytest.mark.parametrize("login_flow", ["email", "phone"])
def test_success_log_in(login_page, login_flow):
    if login_flow == "email":
        login_page.auth_flow(is_email_flow=True)
    else:
        login_page.auth_flow(is_email_flow=False)
    sleep(3)
    login_page.is_url_valid()

def test_sign_up(login_page):
    login_page.sign_up_flow()

# @pytest.mark.parametrize(
#     'user_name, password, error_message',
#     [
#         ('tomsmith@mail.com', '123456', 'Неверное имя пользователя или пароль.'),
#         ('', '123456', 'Поле E-Mail адрес обязательно для заполнения.'),
#         ('tomsmith@mail.com', '', 'Неверное имя пользователя или пароль.'),
#         ('', '', 'Поле E-Mail адрес обязательно для заполнения.'),
#         ('123@ts.ts', '', 'Поле E-Mail адрес должно быть действительным электронным адресом.')
#     ],
#     ids=[
#         'invalid_credentials',
#         'empty_email',
#         'empty_password',
#         'empty_fields',
#         'non_existent_email'
#     ]
# )
# def test_unsuccessful_log_in(login_page, user_name, password, error_message):
#     login_page.enter_user_name(user_name)
#     login_page.enter_password(password)
#     login_page.click_button()
#     login_page.is_error_message_correct(error_message)