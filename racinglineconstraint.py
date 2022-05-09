import numpy as np

class Racing_Line_Constraint:
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

    def constraint_vals(self,xs,ys):
        # constraint values
