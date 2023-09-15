#Cuadratura de Gauss
"""
Para la función de Roots, Weights = np.polynomial.legendre.leggauss(n), la primera fila que imprime es de 
los valores de la raíces del polinomio. La otra fila es de los valores de los pesos.
"""

#Líneas para el parcial:
    """
    Líneas de código para el parcial:
    
    n = 4
    Roots, Weights = np.polynomial.legendre.leggauss(n)
    
    t = 0.5*( (b-a)*Roots + a + b)
    Integral = 0.5*(b-a)*np.sum(Weights*f(t))
    
    """
    



