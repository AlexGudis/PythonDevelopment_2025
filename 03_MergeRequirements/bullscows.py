import cowsay
import argparse
import os
import sys

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



print(bullscows('apple', 'papaaaa'))

