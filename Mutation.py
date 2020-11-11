import random


def mutation(child):

    for i in range(2, len(child)):
        # print(child.shape)
        rdn = random.random()
        if rdn > 0.1:
            continue
        else:
            select1 = random.randint(0, 1)
            select2 = random.randint(0, 5)
            new_weight = random.random()
            child[i][select1][select2] = new_weight

    return child
