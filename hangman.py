# Импортируем необходимый модуль для рандомного подбора слов
import random

# Импортируем предложенный набор слов
from hangman_guessing import guess_list

# Импортируем и печатаем название игры
from hangman_life import game_name
print(game_name)




def the_game():
    tries = 6
    failed = 0
    word_underscore = "______"
    guessing_word = random.choice(guess_list).lower()
    print(guessing_word, "2", "3")
    # guessing_letter = str(input("Guess a letter: "))

    for guessing_letter in guessing_word:
        # guessing_letter = str(input("Guess a letter: "))
        if guessing_letter not in guessing_word:
            print("_")
        print(guessing_letter)
    else:
        print("something")





the_game()




