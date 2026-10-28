import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_question_and_answer():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{a} {b}'
    correct_answer = str(gcd(a, b))
    return question, correct_answer
