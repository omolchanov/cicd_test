import random
import time


def get_random_int():
    return random.randint(1, 100)


def get_random_float():
    """Test"""
    return random.random()


def get_random_string():
    return "sfsdfsd"


def add():
    return 2+2


def main():
    print(time.time())
    print(get_random_int())
    print(get_random_float())
    print(get_random_string(), '\n')


if __name__ == '__main__':
    while True:
        main()
        time.sleep(2)
