import cowsay
import argparse
import os
import sys
import random
import urllib.request

def bullscows(check_word: str, ans_word: str) -> (int, int):
    cows = 0
    buls = 0
    for i in range(len(check_word)):
        if check_word[i] in ans_word:
            if i < len(ans_word) and ans_word[i] == check_word[i]:
                buls += 1
            else:
                cows += 1

    return (buls, cows)


def ask(prompt: str, valid: list[str] = None) -> str:
    input_word = input(prompt)
    if valid is not None:
        while input_word not in valid:
            print('Inccorrect input, try again')
            input_word = input_word(prompt)    
    return input_word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    counter = 0
    word_ans = random.choice(words)
    word_from_user = ''
    while word_from_user != word_ans:
        counter += 1
        word_from_user = ask("Введите слово: ", words)
        bulls, cows = bullscows(word_from_user, word_ans)
        inform("Быки: {}, Коровы: {}", bulls, cows)

    print('Succeed!!!')
    return counter

def get_words(dict: str):
    words = []
    if dict.startswith('https://'):
        with urllib.request.urlopen(dict) as response:
            words =  response.read().decode('utf-8').splitlines()
    else:
        with open(dict, "r") as f:
            words = f.read().split('\n')
    return words


parser = argparse.ArgumentParser()
parser.add_argument(
    "dict", 
    help="File name or URL to word, which will be used in game"
)

parser.add_argument(
    "size",
    type=int,
    nargs="?",
    help="Len of used words (5 is a default)",
    default=5,
)

args = parser.parse_args()
words = get_words(args.dict)
print(words[0:10])