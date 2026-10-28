import random

DESCRIPTION = 'What number is missing in the progression?'

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(length, start, step):
    return [start + i * step for i in range(length)]


def get_question_and_answer():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = generate_progression(length, start, step)

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
