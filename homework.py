import matplotlib.pyplot as plt
import numpy as np
import math

D = 1.46
Psi = 2.0328
K = 2.9167
Fa = 0.0038363
Gs = 8.12886e-9
Pas = 1.89061e-4



def main():
    ars = np.arange(0, 0.3, 0.0000001)
    acs = (2/(K*Fa))**(2/(D-1)) * Gs**2
    p1 = (2**(3-0.5*D)) * D * Psi**(1+0.25*D**2-D)/(3*math.pi**0.5*(3-2*D))
    p2 = Gs**(D-1)
    p3 = (((2-D)/D)*ars)**(0.5*D)
    p4 = (((2-D)/D)*Psi**(0.5*D-1)*ars)**(1.5-D) - acs**(1.5-D)
    p5 = Psi**(1+0.25*D**2-D)*K*Fa*ars**(0.5*D)
    p6 = ((D/(2-D))*acs)**(1-0.5*D)
    y = p1*p2*p3*p4 + p5*p6 - Pas
    plt.plot(ars, y)
    plt.title("Pas draw")
    plt.show()



if __name__ == "__main__":
    main()