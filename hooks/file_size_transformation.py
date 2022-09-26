class FileSizeTransformation:
    """Класс для преобразования размеров файлов в разные еденицы измерения"""

    @staticmethod
    def from_kb_to_mb(values: list) -> list:
        """Метод преобразовывает список значений из КБ в МБ при необходимости"""

        values_in_kb = []

        for value in values:
            if 'Кб' in value:
                value = float(value.replace(',', '.')[:-3]) / 1024
                values_in_kb.append(float('{:.2f}'.format(value)))
            elif 'Мб' in value:
                values_in_kb.append(float(value.replace(',', '.')[:-3]))

        return values_in_kb

