class BasicWord:

    def __repr__(self):
        return "Объект содержащий базовое слово и соответствия"

    def __init__(self, basic_word: str, accept_words: list):
        """
        Функция инициализации сохраняет в объект базовое слово и набор соответствующих слов в виде списка
        """
        self.basic_word = basic_word
        self.accept_words = accept_words

    def word_is_accept(self, word: str):
        """
        Функция проверяет наличие переданного слова в списке соответствующих слов
        """
        return True if word in self.accept_words else False

    def count_words(self):
        """
        Функция возвращает количество соответствующих слов
        """
        return len(self.accept_words)


class Player:

    def __repr__(self):
        return "Объект пользователя"

    def __init__(self, name: str):
        self.name = name
        self.words = []  # использованные слова пользователем

    def count_words(self):
        """
        Возвращает количество слов пользователя
        """
        return len(self.words)

    def add_word(self, word: str):
        """
        Функция добавляет слово в список слов пользователя
        """
        self.words.append(word)

    def word_is_entered(self, word: str):
        """
        Функция определяет, вводил ли пользователь данное слово
        """
        return True if word in self.words else False
