#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
A = B = 1.0
#%%
def f(R):
    return ((A/R**12) - (B/R**6))
#%%
def SMC():
    x_old = np.random.uniform(0.2,2)
    E1 = f(x_old)
    
    energy = []
    x_val = []
    x_val.append(x_old)
    energy.append(E1)
    for i in np.arange(100):
        h = 0.1 * np.random.uniform(-0.05,0.05)
        x_new = x_old + h
        E2 = f(x_new)
        if((E2-E1) <= 0):
            x_old = x_new    
            E1 = E2
            x_val.append(x_old)
            energy.append(E1)
            print("x is %f and energy is %f"%(x_new,E2))
    
    plt.plot(x_val,energy)
    plt.show()
    ind = np.argmin(energy)
    x_min = x_val[ind]
    print(x_min)
#%%    
def MMC():
    x_old = np.random.uniform(0.2,2)
    E1 = f(x_old)
#%%    
    energy = []
    x_val = []
    for i in np.arange(1000):
        h = 0.1 * np.random.uniform(-0.05,0.05)
        x_new = x_old + h
        E2 = f(x_new)
        r=np.random.uniform(0,1)
        if(r < np.exp(-(E2-E1))):
            x_old = x_new    
            E1 = E2
            x_val.append(x_old)
            energy.append(E1)
            print("x is %f and energy is %f"%(x_new,E2))
    
    plt.plot(x_val,energy)
    plt.show()
    ind = np.argmin(energy)
    x_min = x_val[ind]
    print(x_min)
#%%