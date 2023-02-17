import random

MEMO = 'What is the result of the expression?'


def get_question_and_answer():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operation = random.choice('+-*')
    expression = f'{operand1} {operation} {operand2}'

    if operation == '+':
        result = operand1 + operand2
    elif operation == '-':
        result = operand1 - operand2
    else:
        result = operand1 * operand2

    return expression, str(result)
