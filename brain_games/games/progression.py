from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    start = randint(1, 20)
    finish = randint(120, 150)
    step = randint(1, 10)
    progression = range(start, finish, step)
    return progression


def get_question_and_answer():
    position = randint(0, 9)
    progression = make_progression()
    right_answer = str(progression[position])
    list_progr = list(progression)
    list_progr[position] = '..'
    collect = ''
    for i in list_progr[:10]:
        collect = collect + ' ' + str(i)
    question = collect.lstrip()
    return right_answer, question
