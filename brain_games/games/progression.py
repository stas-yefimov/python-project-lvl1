import random

MEMO = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    stop = start + 10 * step
    progression = list(map(str, range(start, stop, step)))
    items = random.choice(progression)
    progression[progression.index(items)] = '..'
    return ' '.join(progression), items
