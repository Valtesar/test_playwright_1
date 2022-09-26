class FileSizeTransformation:
    """Класс для преобразования размеров файлов в разные еденицы измерения"""

    @staticmethod
    def from_kb_to_mb(values: list) -> list:
        """Метод преобразовывает список значений из КБ в МБ при необходимости"""

        result = []

        for value in values:
            if 'Кб' in value:
                value = float(value.replace(',', '.')[:-3]) / 1024
                result.append(float('{:.2f}'.format(value)))
            elif 'Мб' in value:
                result.append(float(value.replace(',', '.')[:-3]))

        return result

