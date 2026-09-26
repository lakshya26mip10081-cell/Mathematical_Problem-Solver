import random


def generate_random_number(start, end):
    if start > end:
        return None

    return random.randint(start, end)