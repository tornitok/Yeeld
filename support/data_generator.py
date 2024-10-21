import random
import string
import os
import json


class DataGenerator:
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(ROOT_PATH, "country_codes.json")

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

    @staticmethod
    def get_random_country(file_path=file_path) -> str:
        """
        Get a random country from a JSON file containing country names.

        :param file_path: Path to the JSON file with country data.
        :return: Random country name.
        """
        with open(file_path, 'r') as file:
            country_data = json.load(file)
        country_names = [country['name'] for country in country_data]
        return random.choice(country_names)



generator = DataGenerator()
generate_email = generator.generate_string(10)
generate_country = generator.get_random_country()
