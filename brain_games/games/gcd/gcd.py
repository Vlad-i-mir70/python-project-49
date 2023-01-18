from random import randint


def gcd():
    number1 = randint(10, 99)
    number2 = randint(10, 99)
    #print(f' numb1 {number1}')
    print(f'Question: {number1} {number2}')
    i = number1 + 1
    while 1 < i <= number1 + 1:
        i -= 1
        if number1 % i == 0:
            k = number2 + 1
            while 1 < k <= number2 + 1:
                k -= 1
                if number2 % k == 0 and k == i:
                    return k