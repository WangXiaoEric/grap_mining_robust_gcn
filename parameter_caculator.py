import numpy as np
from scipy.optimize import curve_fit

def func(X, a, b, c):
    gamma,lambda_,phi = X
    return a*gamma**2 + b*lambda_**2 + c*phi**2

# some artificially noisy data to fit
gamma = np.linspace(0.1,1.1,101)
lambda_ = np.linspace(1.,2., 101)
phi = np.linspace(1.,2., 101)
a, b, c = 10., 4., 6.
z = func((gamma,lambda_,phi), a, b, c) * 1 + np.random.random(101) / 100

# initial guesses for a,b,c:
p0 = 8., 2., 7.
res = curve_fit(func, (gamma,lambda_,phi), z, p0)
print(res)