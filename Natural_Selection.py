import random
import numpy as np


def join(a, b):
    ar = []
    for i in range(2):
        for j in range(6):
            select_value = random.random()
            if select_value <= 0.55:
                ar.append(a[i][j])
            else:
                ar.append(b[i][j])
    ar = np.array(ar)
    ar = ar.reshape(2, 6)
    return ar


def new_population(fitness):
    new_pop = []

    first = fitness[0][2].get_weights()
    second = fitness[1][2].get_weights()
    third = fitness[2][2].get_weights()
    fourth = fitness[3][2].get_weights()

    new_pop.append(first)
    new_pop.append(second)

    # print(first, second)

    new_pop.append(join(first, second))

    for i in range(20):
        r1 = random.randint(0, 10)
        r2 = random.randint(0, 19)
        new_pop.append(join(fitness[r1][2].get_weights(), fitness[r2][2].get_weights()))

    '''
    for i in range(2):
        new_pop.append(join(first, second))
    for i in range(2):
        new_pop.append(join(first, third))
    for i in range(2):
        new_pop.append(join(second, third))
    for i in range(2):
        new_pop.append(join(first, fourth))
    for i in range(2):
        new_pop.append(join(second, fourth))
    for i in range(2):
        new_pop.append(join(third, fourth))
'''
    # print(new_pop)
    return new_pop
