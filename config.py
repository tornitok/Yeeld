from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()


class Secrets:
    USER_NAME_CLIENT: Final[str] = os.getenv('EMAIL')
    PASSWORD_CLIENT: Final[str] = os.getenv('PASSWORD')
    VERIFICATION_CODE: Final[str] = os.getenv('VERIFICATION_CODE')
    PHONE_NUMBER: Final[str] = os.getenv('PHONE_NUMBER')

class URL:
    BASE_URL = 'https://amzonite:SFDKgnbd@@!13123@amzonite-dev.ibisweb3.dev'
    SIGN_IN_PAGE = f'{BASE_URL}/sign_in'
    MAIN_PAGE = f'{BASE_URL}/main'
