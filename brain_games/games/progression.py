import random


def init():
    print('What number is missing in the progression?')


def main():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    stop = start + 10 * step
    progression = [str(i) for i in range(start, stop, step)]
    items = random.choice(progression)
    progression[progression.index(items)] = '..'
    return ' '.join(progression), items
