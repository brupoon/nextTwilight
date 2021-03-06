# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 10:19:03 2014

@author: demure
"""
import numpy as np
from matplotlib import pyplot as plt
f=r"C:\pyf\ast\iso100Mfixed.txt"
data = np.loadtxt(f)
logteff = data[:,0]
mbol = data[:,1]
#logteff_inv = list(reversed(logteff))
plt.plot(logteff, mbol, 'b.',markersize = 5)
plt.title("Isochrone, 100Myr")
plt.xlabel("logTeff")
plt.ylabel("Mbol")
plt.xlim(4.3,3.3)
plt.ylim(8,-8)