import prompt
import random


def is_even(number):
    return True if number % 2 == 0 else False


def game(name):
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    for count in range(3):
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ').lower()
        if is_even(number):
            if answer == 'yes':
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f'Lets try again, {name}!')
                break
        if not is_even(number):
            if answer == 'no':
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f'Lets try again, {name}!')
                break
    else:
        print(f'Congratulations, {name}!')
