from random import sample


def get_number():
    lst_number = sample([i for i in range(1, 10)], 4)
    number = lst_number[0] * 1000 + lst_number[1] * 100 + lst_number[2] * 10 + lst_number[3]
    return number


def get_bulls_and_cows_from_number(number, attempt_number):
    bulls = 0
    cows = 0
    number = str(number)
    attempt_number = str(attempt_number)
    for i in range(4):
        if number[i] == attempt_number[i]:
            bulls += 1
        elif number[i] in attempt_number:
            cows += 1
    return bulls, cows


def is_availbale_numbers(number):
    return True if len(str(number)) == 4 else ValueError('Нужно 4-значное не повторяющееся')