from random import sample
import math


def get_number(length):
    lst_number = sample([i for i in range(1, 10)], length)
    number = 0
    for i in range(1, length + 1):
        number = lst_number[-i] * math.pow(10, i)
    return number


def get_bulls_and_cows_from_number(number, attempt_number):
    bulls = 0
    cows = 0
    number = str(number)
    attempt_number = str(attempt_number)
    for i in range(len(str(number))):
        if number[i] == attempt_number[i]:
            bulls += 1
        elif number[i] in attempt_number:
            cows += 1
    return bulls, cows


def is_availbale_numbers(number, length):
    return True if len(str(number)) == length else ValueError(f'Нужно {length}-значное не повторяющееся')
