from random import choices, randrange
import string


class GenerateRandomData:

    @classmethod
    def get_random_fio(cls):

        fio = [''.join(choices(string.ascii_lowercase, k=randrange(2, 7))) for _ in range(3)]

        return fio

    @classmethod
    def get_random_mobile(cls):

        mobile = randrange(9_000_000_000, 9_999_999_999)

        return mobile

    @classmethod
    def get_random_email(cls):

        def rand_text():
            return ''.join(choices(string.ascii_lowercase, k=randrange(4, 7)))

        email = "{}@{}.{}".format(rand_text(), rand_text(), 'com')

        return email

