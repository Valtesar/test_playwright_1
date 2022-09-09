from random import choices, randrange
import string


class GenerateRandomData:

    @classmethod
    def get_random_fio(cls):
        fio_list = [''.join(choices(string.ascii_lowercase, k=randrange(4, 7))) for _ in range(3)]
        fio_string = ' '.join(fio_list)
        return fio_string

    @classmethod
    def get_random_mobile(cls):
        mobile = randrange(9_000_000_000, 9_999_999_999)
        return str(mobile)

    @classmethod
    def get_random_email(cls):
        def rand_text():
            return ''.join(choices(string.ascii_lowercase, k=randrange(4, 7)))
        email = "{}@{}.{}".format(rand_text(), rand_text(), 'com')
        return email

    @classmethod
    def get_random_gender(cls):
        gender = ''.join(choices('mf'))
        return gender


if __name__ == '__main__':
    print(GenerateRandomData.get_random_gender())
