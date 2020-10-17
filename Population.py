import sys

sys.path.append(".")
from NN import Brain


class build_population:
    def __init__(self, init_pop):
        self.idx = 1
        self.pop = init_pop
        self.ret = []

    def make_pop(self):

        for i in range(len(self.pop)):
            new_brain = Brain()
            new_brain.update_weights(self.pop[i])
            self.ret.append(new_brain)

        while len(self.ret) < 40:
            parent_brain = Brain()
            self.ret.append(parent_brain)
            self.idx = self.idx + 1
            #print(parent_brain.print_brain())
            #print("the BRAIN")
        return self.ret
