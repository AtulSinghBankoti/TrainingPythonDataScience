import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt


a = np.array([1, 4, 5, 1, 3, 5, 3, -1, -3])

print(scipy.fftpack.fft(a))

# fft transforms the time domain signal to frequency (sinusodial) domain signal.
#number of items taken per second
item_rate=1024
frequency = 2
 
total = item_rate *  frequency
#x axis -> time 
time = np.linspace(0, 2, total)
print(time)

# time series
#there are two sine waves
# 1. one with magnitude of 25  at 60 Hz
# 2. one with magnitude of 4 at 10 Hz
freq1 = 60
freq2 = 180
magnitude1 = 25
magnitude2 = 4
waveform1 = magnitude1 * np.sin(2*np.pi*freq1*time)
waveform2 = magnitude2 * np.sin(2*np.pi*freq2*time)

#add some noise to waveforms
noise = np.random.normal(0, 3, total)

# add noise to waveforms to get time data
timedata = noise + waveform1 + waveform2


plt.plot(time, timedata)
plt.title("Time domain signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

#convert time series plot to frequency plot

freqdata = scipy.fftpack.fft(timedata)
#nyquist shannon sampling theorem
frequency =np.linspace(0, 1024, 1024)
y = 2/total*np.abs(freqdata[0:np.int(1024)])

plt.plot(frequency, y)
plt.title("Frequency domain signal")
plt.xlabel("frequency in hz")
plt.ylabel("amplitude")
plt.show()
