from random import choices, randrange
import string


class GenerateRandomData:
    """Класс для генерации рандомных данных используя методы класса, для обращения к ним,
       без создания экземпляров класса"""

    @classmethod
    def get_random_fio(cls):
        """Метод генерирует случайную фамилию, имя и отчество.

        Длина фамилии, имени и отчества выбирается случайного размера в указанном диапазоне.
        Метод возвращает фамилию, имя и отчество типа -> str, в формате: <Фамилия Имя Отчество>"""

        fio_list = [''.join(choices(string.ascii_lowercase, k=randrange(4, 7))) for _ in range(3)]
        fio_string = ' '.join(fio_list)

        return fio_string

    @classmethod
    def get_random_mobile(cls):
        """Метод генерирует случайный номер телефона.

        Значение номера телефона выбирается из указанного диапазона чисел.
        Метод возвращает номер телефона типа -> str, в формате <9999999999>"""

        mobile = randrange(9_000_000_000, 10_000_000_000)

        return str(mobile)

    @classmethod
    def get_random_email(cls):
        """Метод генерирует случайный адрес электронной почты.

        Имя и домен электронной почты генерируются из случайных букв с указанной длинной.
        Метод возвращает адрес электронной почты типа -> str, в формате <name@domain.com>"""

        def rand_text():
            return ''.join(choices(string.ascii_lowercase, k=randrange(4, 7)))
        email = "{}@{}.{}".format(rand_text(), rand_text(), 'com')

        return email

    @classmethod
    def get_random_gender(cls):
        """Метод генерирует случайный пол человека.

        Пол выбирается случайным образом из мужского и женского.
        Метод возвращает пол типа -> str, в формате <пол>"""

        gender = ''.join(choices('mf'))

        return gender

    @classmethod
    def get_random_passport_series(cls):
        """Метод генерирует случайную серию паспорта.

        Значение серии паспорта выбирается из указанного диапазона чисел.
        Метод возвращает серию паспорта типа -> str, в формате <9999>"""

        number = randrange(1000, 10_000)

        return str(number)

    @classmethod
    def get_random_passport_number(cls):
        """Метод генерирует случайный номер паспорта.

        Значение номера паспорта выбирается из указанного диапазона чисел.
        Метод возвращает номер паспорта типа -> str, в формате <999999>"""

        series = randrange(100_000, 1_000_000)

        return str(series)

