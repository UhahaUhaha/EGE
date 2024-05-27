import json
import os
import random
vowels = "уеыаоэяиюё"


class Word:
    def __init__(self, word_as_dict):
        self.word = word_as_dict["word"]
        self.context = word_as_dict["context"]
        self.stress = word_as_dict["stress"]
        self.capitalized = word_as_dict["capitalized"]
        vowel = 0
        for i in range(len(self.word)):
            if self.word[i] not in vowels:
                continue
            if i == self.stress:
                self.stress = vowel
            vowel += 1
        self.cnt = vowel


def print_progress(current, total, bars):
    filled_bars = current * bars // total
    empty_bars = bars - filled_bars
    print("[" + "■" * filled_bars + " " * empty_bars + "]", f"({current+1}/{total})")


def main():
    os.system("cls")
    files = [
        "Слова.json"
    ]
    words = []
    for f in files:
        dictionary = json.loads(open(f, "r", encoding="UTF-8").read())
        for word in dictionary["list"]:
            words.append(Word(word))
    try:
        n = int(input(f"Введите количество слов (или нажмите Enter, чтобы запустить все слова)\nВсего {len(words)} слов\n"))
    except:
        n = len(words)
    if 0 < n <= len(words):
        pass
    else:
        n = len(words)
    random.shuffle(words)
    words = words[:n]
    mistakes = []
    for index, word in enumerate(words):
        print_progress(index, len(words), 20)
        symbol_length = len(str(word.cnt)) + 1
        print(word.word, end=" ")
        if word.context:
            print("(", *word.context, ")", end='')
        print()
        for i in range(symbol_length):
            print(" " * i, end='')
            vowel = 0
            for j, c in enumerate(word.word):
                if j % symbol_length == i:
                    if c in vowels:
                        print(str(vowel + 1).ljust(symbol_length), end="")
                    else:
                        print("".ljust(symbol_length), end='')
                if c in vowels:
                    vowel += 1
            print()
        waiting_for_input = True
        while waiting_for_input:
            try:
                n = int(input())
            except ValueError:
                print("Ошибка ввода!")
            except:
                print("Непредвиденная ошибка!")
                break
            else:
                waiting_for_input = False
        if waiting_for_input:
            break
        if n != word.stress + 1:
            print("Неправильно!")
            mistakes.append(word)
        else:
            print("Правильно!")
        print(word.capitalized)
        print()
        input()
        os.system("cls")
    if mistakes:
        print("Ошибки:")
    else:
        print("Ошибок нет!")
    for word in mistakes:
        print(word.capitalized, end=" ")
        if word.context:
            print("(", *word.context, ")", end='')
        print()


if __name__ == "__main__":
    main()
    print()
    input("Нажмите Enter 2 раза, чтобы закрыть")
    input()
