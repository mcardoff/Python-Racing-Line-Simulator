class gradient_descent:
    def __init__(self):
        self.learning_rate = 0.1
        self.problem = Problem()

    def __init__(self, learning_rate, problem):
        self.learning_rate = learning_rate
        self.problem = problem

    def minimize(inputxs, inputys, max_iters):
        # iteration_number = 0
        # main method of going is stopping at max iters
        returnxs = inputxs
        returnys = inputys
        for i in range(max_iters):
            grad_x, grad_y = [], []
            problem.gradient(grad_x, grad_y, returnxs, returnys)

            for j in range(len(returnxs)):
                returnxs[i] -= grad_x[i]
                returnys[i] -= grad_y[i]
