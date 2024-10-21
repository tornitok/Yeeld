import random
import string

class DataGenerator:
    @staticmethod
    def generate_string(length: int) -> str:
        """
        Generate a random string of specified length.

        :param length: Length of the string to be generated.
        :return: Randomly generated string.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))+'@test.com'

    @staticmethod
    def generate_number(min_value: int, max_value: int) -> int:
        """
        Generate a random number between specified min and max values.

        :param min_value: Minimum value of the number.
        :param max_value: Maximum value of the number.
        :return: Randomly generated number.
        """
        return random.randint(min_value, max_value)

generator = DataGenerator()
generate_email = generator.generate_string(10)
