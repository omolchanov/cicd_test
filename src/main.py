import random


def get_random_int():
    return random.randint(1, 100)


def get_random_float():
    return random.random()


if __name__ == '__main__':
    print(get_random_int())
    print(get_random_float())