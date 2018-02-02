# -*- coding: utf-8 -*-
"""
Created on Wed May 03 23:49:02 2017
Reading in the wave forms from an xml document
@author: Silas Grossberndt
"""
#import cPickle as pl #cPickle was used to attempt to run faster, but it was too slow compared to numpy save
import numpy as np
import matplotlib.pyplot as plt
#import Pandas as pan
import bs4 as bs
waveform=np.ones((20000, 4096)) # to act as a holding spot for the data read in
def fileopen(f1n):
    souped=bs.BeautifulSoup(open(f1n), "lxml") #prepare the file for reading
    i=0 #index for the waveforms
    for text in souped.stripped_strings:
        tl=text.strip().split() #each "text" line is a full waveform, so we break on spaces
        #print (len(tl)) #testing
        for alpha in range(len(tl)): #to index within the waveform
            waveform[i, alpha]=float(tl[alpha]) #as tl is currently a string 
            #if alpha==0:
                #print tl[alpha]
        i=i+1 #move to next waveform
    print waveform[20,30] #test that something is read in 
    plt.plot(waveform[20,]) #sanity check on code
    plt.show()
    return []             

fileopen("CsI.xml")
np.save("waveforms", waveform) #works faster than Pickle, as Pickle was crashing my compiler



