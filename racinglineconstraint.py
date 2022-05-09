import numpy as np

class Racing_Line_Constraint:
    def __init__(self):
        self.KMAX = 0.5
        self.TRACKWIDTH = 1.50

    def curvature_val(self,xs,ys,i):
        dxb = xs[i]-xs[i-1]
        dyb = ys[i]-ys[i-1]
        dxf = xs[i+1]-xs[i]
        dyf = ys[i+1]-ys[i]
        dsb = np.sqrt(dxb*dxb + dyb*dyb)
        dsf = np.sqrt(dxf*dxf + dyf*dyf)
        term_one = (dxb/dsb + dxf/dsf) * (dyf/dsf - dyb/dsb)/(dsf + dsb)
        term_two = (dyb/dsb + dyf/dsf) * (dxf/dsf - dxb/dsb)/(dsf + dsb)
        return term_one-term_two

    def cost_fun(self,xs,ys):
        cost = 0.0
        for i in range(1,len(xs)-1):
            k = self.curvature_val(xs,ys,i)
            dxb = xs[i]-xs[i-1]
            dyb = ys[i]-ys[i-1]
            dxf = xs[i+1]-xs[i]
            dyf = ys[i+1]-ys[i]
            dsb = np.sqrt(dxb*dxb+dyb*dyb)
            dsf = np.sqrt(dxf*dxf+dyf*dyf)
            ds = 0.5 * (dsf + dsb)
            cost += np.sqrt(abs(k))*ds

    def kmax_constraint(self,xs,ys,i):
        kval = self.curvature_val(xs, ys, i)
        return kval - self.KMAX

    def friction_constraint(self,xs,ys,i):
        k = self.curvature_val(xs, ys, i)
        mug = 9.8
        vsq = k / mug
        return abs(k * vsq - mug)

    def constraint_vals(self,xs,ys,i):
        # constraint values
        # returns a list with all of the constraint values
        return [self.kmax_constraint(xs, ys, i),
                self.friction_constraint(xs,ys,i)]
        
