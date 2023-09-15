from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

class Integrator:
    
    def __init__(self,x,f):
        
        self.x = x
        self.h = self.x[1] - self.x[0]
        self.y = f(self.x)
        
        self.Integral = 0.

class Simpson(Integrator):
    
    def __init__(self,x,f):
        Integrator.__init__(self,x,f)
        
    def GetIntegral(self):
        
        self.Integral = 0.
        
        self.Integral += self.y[0] + self.y[-1]
        
        for i in range( len(self.y[1:-1]) ):
            
            if i%2 == 0:
                self.Integral += 4*self.y[i+1]
            else:
                self.Integral += 2*self.y[i+1]
          
        return self.Integral*self.h/3

class error(Integrator):
    
    def __init__(self,x,f)
    
    def Geterror(self):
        
        self.error = 0.
        
        self.error += (f(x+4*h)- 4*(f(x+3*h))+ 6*(f(x+2*h)) - 4*(f(x+h)) + f(x) )/h**4
    