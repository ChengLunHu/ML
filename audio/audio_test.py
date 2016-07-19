import re, math, collections, itertools, os
from pylab import*
from scipy.io import wavfile

# RT_POLARITY_POS_FILE = os.path.join('Test_Mic12_16K.wav')
sampFreq, snd = wavfile.read('D:\\Py_Lib\\AudioEffectsAndPlayback\\audio\\Test_Mic12_16K.wav')

s1 = snd[:,0]

####################
# Time domain
####################
timeArray = arange(0, snd.shape[0], 1)

subplot(211)
plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Sample')
axis([0, snd.shape[0], -2**15, 2**15-1])

####################
# Freq. domain
####################
n = len(s1)
p = fft(s1)
nUniquePts = ceil((n+1)/2.0)
p = p[0:nUniquePts]
p = abs(p)
p = p / float(n)  # scale by the number of points so that
p = p ** 2
if n % 2 > 0: # we've got odd number of points fft
    p[1:len(p)] = p[1:len(p)] * 2
else:
    p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

x = arange(0, p.shape[0], 1)
subplot(212)
plot(x, 10*log10(p), color='k')
ylabel('Amplitude')
xlabel('Sample')
axis([0, p.shape[0], min(10*log10(p)), max(10*log10(p))])

show()
