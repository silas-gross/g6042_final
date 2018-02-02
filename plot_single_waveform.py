# -*- coding: utf-8 -*-
"""
Created on Fri May 05 20:37:44 2017
Ploting a single waveform
@author: Silas Grossberndt
"""

import numpy as np
import matplotlib.pyplot as plt

wf=np.load("waveforms.npy")
plt.plot(wf[1002,]) #array starts at 0, so the 1003rd wave form is element 1002
plt.title("Waveform 1003") 
plt.xlabel("ADC Samples")
plt.ylabel("ADC Counts")
plt.axis([0, 4500, 2175, 2220])
plt.axvline(x=150, linestyle='dashed') 
plt.axvline(x=1800, linestyle='dashed') #done by visual inspection

plt.savefig('waveform.png') 




