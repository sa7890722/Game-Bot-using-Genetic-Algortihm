import numpy as np


class Brain:
    def __init__(self):
        self.layers = 2  # input layer and output layer :
        self.weights = np.random.random(12).reshape(2, 6)

    def get_action(self, input):
        input = np.array(input).reshape(6, 1)
        output = np.matmul(self.weights, input)
        if output[0] > output[1]:
            return 1
        else:
            return 0

    def remove_brain(self):
        del self

    def print_brain(self):
        print(self.weights)

    def get_weights(self):
        return self.weights

    def update_weights(self, new_weights):
        for i in range(2):
            for j in range(4):
                self.weights[i][j] = new_weights[i][j]

