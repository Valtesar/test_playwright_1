from random import choices, randrange
import string


class GenerateRandomData:
    def __init__(self):
        pass

    @classmethod
    def get_random_fio(cls):
        fio = [''.join(choices(string.ascii_lowercase, k=randrange(2, 7))) for _ in range(3)]
        return fio

    @classmethod
    def get_random_mobile(cls):
        mobile = randrange(9_000_000_000, 9_999_999_999)
        return mobile

    def get_random_email(self):
        pass


if __name__ == '__main__':
    x = GenerateRandomData()
    print(x.get_random_fio())
    print(GenerateRandomData.get_random_fio())
    print(GenerateRandomData.get_random_mobile())
