from game_classes import *
from utils import *


def main():
    """
    Основной код программы, пользователь инициирует экземпляр игрока и передает свое имя,
    выбирает сложность (необходимое количество угаданных слов для победы)
    """
    player = Player(input("Введите имя игрока: "))
    print(f"Привет, {player.name}")
    game_word = load_random_word()  # Экземпляр класса BasicWord
    while True:
        player_answer = input("Выберите сложность: средний или сложный? ").lower()
        if player_answer[0:4] == "сред":  # Для победы достаточно 8 угаданных слов
            difficulty = 8
            break
        if player_answer[0:4] == 'слож':
            difficulty = game_word.count_words()  # Для победы нужно угадать все слова
            break
        print(f"Некорректный ввод, {player.name}")
    print(f"Составьте {difficulty} слов из слова {game_word.basic_word.upper()}\n"
          f"Слова не должны быть короче 3 букв\n"
          f"Чтобы закончить игру, угадайте слова, или напишите \"stop\"\n"
          f"Поехали!")
    while player.count_words() != difficulty:
        player_answer = input("Введите слово: ").lower()
        if player_answer in ("stop", "стоп"):
            break
        if not len(player_answer) > 2:
            print("Слово слишком короткое")
            continue
        if not game_word.word_is_accept(player_answer):
            print("Неверно")
            continue
        if player.word_is_entered(player_answer):
            print("Уже использовано")
            continue
        print("Верно")
        player.add_word(player_answer)
    print(f"Игра завершена, {player.name}, Вы угадали {player.count_words()} слов!")  # Вывод статистики, конец


if __name__ == "__main__":
    main()
