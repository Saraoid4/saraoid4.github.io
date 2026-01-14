import numpy as np

def x_1(t, A=51, f_0=1):
    return A*np.cos(2*np.pi*f_0*t)

def x_2(t):
    if t <= 2:
        if t > 1:
            return 2-t
        elif t>=0:
            return t
    return 0

def heaviside(t):
    if t < 0:
        return 0
    elif t > 0:
        return 1
    return 1/2

def porte(t, T=1):
    if np.abs(t) < T/2:
        return 1/T
    elif np.abs(t) > T/2:
        return 0
    return 1/(2*T)

def affine(x, a=1, b=0):
    def y(t):
        return x(a*t - b)
    return y

def fourier(x):
    return np.fft.fftshift(np.fft.fft(x))

def inverse_fourier(Fx):
    return np.real(np.fft.ifft(np.fft.fftshift(Fx))).astype('int16')
