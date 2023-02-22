import random
import operator

MEMO = 'What is the result of the expression?'


def get_question_and_answer():
    operation_and_symbol = (('+', operator.add),
                            ('-', operator.sub),
                            ('*', operator.mul))
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operation_symbol, operation = random.choice(operation_and_symbol)

    expression = f'{operand1} {operation_symbol} {operand2}'
    result = operation(operand1, operand2)
    return expression, str(result)
