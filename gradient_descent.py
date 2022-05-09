import numpy as np
from problemclass import Problem

class gradient_descent:
    def __init__(self):
        self.learning_rate = 0.1
        self.problem = Problem()

    def __init__(self, learning_rate, problem):
        self.learning_rate = learning_rate
        self.problem = problem

    def minimize(self, inputxs, inputys, max_iters):
        # iteration_number = 0
        # main method of going is stopping at max iters
        returnxs = inputxs
        returnys = inputys
        for i in range(max_iters):
            grad_x, grad_y = np.zeros(len(inputxs)), np.zeros(len(inputxs))
            self.problem.gradient(grad_x, grad_y, returnxs, returnys)

            for j in range(len(returnxs)):
                returnxs[i] -= grad_x[i] * self.learning_rate
                returnys[i] -= grad_y[i] * self.learning_rate

        return (returnxs, returnys)
