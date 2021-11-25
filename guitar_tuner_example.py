# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 22:47:45 2021

@author: Fernando Sandoval
"""
import numpy as np
import sounddevice as sd


#SHORT TIME FOURIER TRANSFORM CONFIG: 
    
# variables 
freq_siz = 44100 
sample = 44100 
steps = 44100/2
resolution = freq_siz / sample # 1 Hz
rec_sample = 1/ sample 
windowSAMPLE = [0 for _ in range (sample)]
cp = 440 #A4

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]



# process by which we compare and assign a note to a pitch
i= int(np.round(np.log2(F/cp)*12))
note_comparison = 




