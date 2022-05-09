import numpy as np

from racinglineconstraint import Racing_Line_Constraint
class Problem:
    def __init__(self):
        self.epsilon = 1e-8
        self.batch_num = 5
        self.constraint = Racing_Line_Constraint()

    def perturbed_param(self,retval, xs, ys, i):
        costval = self.cost_fun(xs, ys)
        retval = costval        

    def gradient(self, grad_x, grad_y, xs, ys):
        pf_x, pf_y = 0.0, 0.0
        pb_x, pb_y = 0.0, 0.0
        old_xs, old_ys = xs, ys
        per_xs, per_ys = xs, ys
        for i in range(len(xs)-self.batch_num+1):
            for j in range(self.batch_num):
                per_xs[i+j] += self.epsilon
                per_ys[i+j] += self.epsilon

            self.perturbed_param(pf_y, old_xs, per_ys, i) # keep x const
            self.perturbed_param(pf_x, per_xs, old_ys, i) # keep y const
            
            for j in range(self.batch_num):
                per_xs[i+j] -= 2.0 * self.epsilon
                per_ys[i+j] -= 2.0 * self.epsilon

            self.perturbed_param(pb_y, old_xs, per_ys, i) # keep x const
            self.perturbed_param(pb_x, per_xs, old_ys, i) # keep y const

            grad_x[i] = 0.5 * (pb_x + pf_x) / self.epsilon
            grad_y[i] = 0.5 * (pb_y + pf_y) / self.epsilon

            per_xs, per_ys = old_xs, old_ys # reset values
