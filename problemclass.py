import numpy as np

class Problem:
    def __init__(self):
        self.epsilon = 1e-8
        self.batch_num = 5

    def cost_fun(self,xs,ys):
        cost = 0.0
        for i in range(1,len(xs)-1):
            k = curvatureVal(xs,ys,i)
            dxb = xs[i]-xs[i-1]
            dyb = ys[i]-ys[i-1]
            dxf = xs[i+1]-xs[i]
            dyf = ys[i+1]-ys[i]
            dsb = np.sqrt(dxb*dxb+dyb*dyb)
            dsf = np.sqrt(dxf*dxf+dyf*dyf)
            ds = 0.5 * (dsf + dsb)
            costVal += np.sqrt(abs(k))*ds

    def perturbed_param(retval, xs, ys, i):
        costval = cost_fun(xs, ys)
        retval = costval
        

    def gradient(grad_x, grad_y, xs, ys):
        pf_x, pf_y = 0.0, 0.0
        pb_x, pf_y = 0.0, 0.0
        old_xs, old_ys = xs, ys
        per_xs, per_ys = xs, ys
        for i in range(len(xs)-batch_num+1):
            for j in range(batch_num):
                per_xs[i+j] += epsilon
                per_ys[i+j] += epsilon

            perturbed_param(pf_y, old_xs, per_ys, i) # keep x const
            perturbed_param(pf_x, per_xs, old_ys, i) # keep y const
            
            for j in range(batch_num):
                per_xs[i+j] -= 2.0 * epsilon
                per_ys[i+j] -= 2.0 * epsilon

            perturbed_param(pb_y, old_xs, per_ys, i) # keep x const
            perturbed_param(pb_x, per_xs, old_ys, i) # keep y const            

            grad_x[i] = 0.5 * (pb_x + pf_x) / epsilon
            grad_y[i] = 0.5 * (pb_y + pf_y) / epsilon

            per_xs, per_ys = old_xs, old_ys # reset values
