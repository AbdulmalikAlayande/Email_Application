import random

from utils.Alphabet import Alphabet


class Id_Generator:

    @staticmethod
    def generate_id(list_of_the_objects):
        integer_part_of_id = 1
        string_integer = len(list_of_the_objects) + 10 + integer_part_of_id
        pair = "".join(random.sample(list(str(Alphabet)), 2)).upper()
        return f"{pair}{integer_part_of_id + string_integer}{len(list_of_the_objects)}".upper()
