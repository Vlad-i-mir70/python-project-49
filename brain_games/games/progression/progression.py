from random import randint


def brain_progression():
    number1 = randint(1, 20)
    number2 = randint(120, 150)
    number3 = randint(1, 10)
    number4 = randint(0, 9)
    progression = range(number1, number2, number3)
    list_progr = list(progression)
    result = progression[number4]
    collect = ''
    for i in list_progr[:10]:
        if i == result:
            collect = collect + ' ..'
        else:
            collect = collect + ' ' + str(i)
    print(f' Question:{collect}')
    return result
