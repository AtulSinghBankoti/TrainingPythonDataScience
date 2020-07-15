"""
#maths
scipy.io
scipy.integrate
scipy.special
scipy.linalg
scipy.stats

#signal
scipy.signal
scipy.fftpack

#spatial 
scipy.interpolate
scipy.optimize
scipy.spatial
scipy.ndimage
"""
import scipy.io as sio
import numpy as np

a = np.arange(10)
print("Created an array a")
print(a)

print("Create .mat file -> my.mat from array a")
sio.savemat("my.mat", {'myvar':a})
print("Print the output of matlab file:")
matfilecontent = sio.loadmat('my.mat')
print(matfilecontent)
print("Load variable from matlab file:")
getme = sio.whosmat('my.mat')
print(getme)