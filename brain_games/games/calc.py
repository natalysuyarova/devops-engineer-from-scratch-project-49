import random

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}


def get_question_and_answer():
    a = random.randint(1, 25)
    b = random.randint(1, 25)
    op = random.choice(list(OPERATIONS.keys()))
    question = f'{a} {op} {b}'
    correct_answer = str(OPERATIONS[op](a, b))
    return question, correct_answer
