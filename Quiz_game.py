#define questions, options, correct answer
# Shuffle questions
#Loop over questions
#      1 question at the time
#      Users input
import random
from termcolor import cprint

QUESTION='question'
OPTIONS='options'
ANSWER='answer'
def ask_question(index, question, options):
    print(f'Question {index} : {question}')
    for option in options:
        print(f'\t{option}')

    return input('Your answer: ').upper().strip()

def run_quiz(quiz):
    score = 0
    random.shuffle(quiz)

    for index, item in enumerate(quiz,1):
        user_answer= ask_question(index, item[QUESTION], item[OPTIONS])
        if user_answer==item[ANSWER]:
            cprint('Correct!','green')
            score+=1
        else:
            cprint(f'Incorrect!, the correct answer is {item[ANSWER]}', 'red')
    print(f'Quiz over! Your final score is {score} out of {len(quiz)}')
def main():
    quiz = [
        {
            QUESTION: 'What is the capital of France? ',
            OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
            ANSWER: 'C'
        },
        {
            QUESTION: 'What planet is known as the red planet? ',
            OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'What is the biggest ocean on Earth? ',
            OPTIONS: ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
            ANSWER: 'D'
        }
    ]

    run_quiz(quiz)
if __name__ == '__main__':
    main()
