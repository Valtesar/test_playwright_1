from random import choices, randrange
import string


class GenerateRandomData:
    def __init__(self):
        pass

    def get_random_fio(self):
        fio = [''.join(choices(string.ascii_lowercase, k=randrange(2, 7))) for _ in range(3)]
        return fio

    def get_random_mobile(self):
        pass

    def get_random_email(self):
        pass


if __name__ == '__main__':
    x = GenerateRandomData()
    x.get_random_fio()
