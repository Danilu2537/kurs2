import requests
import random
import game_classes


def load_random_word(address="https://api.npoint.io/72550900315d27573391"):
    """
    Эта функция загружает набор слов в виде json из сети,
    создает экземпляр класса BasicWord из случайного слова и возвращает его
    """
    basic_words = requests.get(address).json()
    basic_word = random.choice(basic_words)
    game_word = game_classes.BasicWord(basic_word["word"], basic_word["subwords"])
    return game_word
