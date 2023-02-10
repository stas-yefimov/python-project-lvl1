import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    game.init()

    for count in range(3):
        question, correct_answer = game.main()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').lower()

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f'Lets try again, {user_name}!')
            break
    else:
        print(f'Congratulations, {user_name}!')
