import numpy as np
import matplotlib.pyplot as plt

def dft(nums):
    resulting_array = []
    N = len(nums)
    for k in range(N):
        sum = 0.0
        for n in nums:
            sum += n * np.power(np.e, (2j * np.pi * k)/N)
        resulting_array.append(sum)
    return resulting_array


Fs = 500;  # taxa de amostragem
Ts = 1.0/Fs; # periodo de amostragem
t = np.arange(0,1,Ts) # vetor de tempo

f = 15
x1_n = np.sin(2*np.pi*f*t + 0)
f = 20;
x2_n = np.sin(2*np.pi*f*t + 0)

x_n = x1_n + x2_n

n = len(x_n) # tamanho do sinal
k = np.arange(n) #vetor em k
T = n/Fs
frq = k/T # os dois lados do vetor de frequencia
frq = frq[range(int(n/2))] # apenas um lado

X = dft(x_n)

print(X)

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,x_n)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(X),'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|X(freq)|')
