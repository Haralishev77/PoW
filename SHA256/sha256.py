from hashlib import sha256

"""
короче типа как-то так это должно быть, понятное дело все функции надо самому сделать
"""
class SHA256:
    def __init__(self):
        self._sha256 = sha256()

    def update(self, data):
        """
        Обновляет хеш объект новыми данными.
        
        :param data: Байтовые данные для обновления хеша.
        """
        self._sha256.update(data)

    def digest(self):
        """
        Возвращает хеш в виде байтов.

        :return: Байтовый объект с хешем.
        """
        return self._sha256.digest()

    def hexdigest(self):
        """
        Возвращает хеш в виде шестнадцатеричной строки.

        :return: Строка с шестнадцатеричным представлением хеша.
        """
        return self._sha256.hexdigest()

    def reset(self):
        """
        Сбрасывает объект хеша для нового вычисления.
        """
        self._sha256 = sha256()