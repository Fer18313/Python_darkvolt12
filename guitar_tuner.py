# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:04:40 2021

@author: Fernando Sandoval
"""
# LIBRERIAS, UNICA NECESARIA DE INSTALACION ES SOUNDDEVICE
# LAS DEMAS ES PROBABLE QUE YA ESTEN INCLUIDAS CON SPYDER EN PYTHON 3.8


import copy
import os
import sounddevice as sndvc
import numpy as np
import scipy.fftpack
import time

#                           AJUSTES GENERALES
##############################################################################
start_tol = 1e-6 # tolerancia de comienzo
max_tol = 48000 # num_samples
steps = 12000 # step del sample
sample = 48000 #Hz
harmonics = 5 # num de harmonicos
reverb = 440 # room Hz
noise_trash = 0.2 # ruido blanco
tol_length = max_tol / sample
sample_length = 1 / sample 
poll = sample / max_tol 

###############################################################################

#                   DEFINICION DE NOTAS MUSICALES

octavas = [50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]

#   EN partituras normales: 
    
escala = ["LA","LA#","SI","DO","DO#","RE","RE#","MI","FA","FA#","SOL","SOL#"]

#   EN INGLES: 
#                 A, A#, B, C, C#, D, D#, E, F, F#, G, G#
#

###############################################################################


# Funcion que busca la frecuencia
def tuner(freq):
  i = int(np.round(np.log2(freq/reverb)*12))
  nota_parecida = escala[i%12] + str(4 + (i + 9) // 12)
  freq_match = reverb*2**(i/12)
  return nota_parecida, freq_match



hann_metodo = np.hanning(max_tol)


# Funcion que elimina ruido, busca la frecuencia  y la relaciona con una nota


def callback(reading, steps_freq, time, current):
  if not hasattr(callback, "samples_tol"):
    callback.samples_tol = [0 for _ in range(max_tol)]
  if not hasattr(callback, "note_memory"):
    callback.note_memory = ["1","2"]
  if current:
    print(current)
    return
  if any(reading):
                        # ACTUALIZACION DE LECTURAS
                        
    # INTRODUCIMOS AL ARRAY EL NUEVO SAMPLE
    callback.samples_tol = np.concatenate((callback.samples_tol, reading[:, 0])) 
    
    # ELIMINAMOS LA MEM DEL ANTERIOR SAMPLE
    callback.samples_tol = callback.samples_tol[len(reading[:, 0]):] 

    # SKIP SI NO LLEGA AL MINIMO DE LECTURA
    signal_power = (np.linalg.norm(callback.samples_tol, ord=2, axis=0)**2) / len(callback.samples_tol)
    if signal_power < start_tol:
      os.system('cls' if os.name=='nt' else 'clear')
      print("...")
      return




    # COMENZAMOS CON LOS AJUSTES DEL METODO HANNING
    
    hann_samples = callback.samples_tol * hann_metodo
    magnitud_freq = abs(scipy.fftpack.fft(hann_samples)[:len(hann_samples)//2])

    for i in range(int(62/poll)):
      magnitud_freq[i] = 0

    # PROMEDIO DE FREQ PARA ELIMINAR CUALQUIER FREQ MENOR
    
    
    for j in range(len(octavas)-1):
      begin = int(octavas[j]/poll)
      end = int(octavas[j+1]/poll)
      end = end if len(magnitud_freq) > end else len(magnitud_freq)
      prom_freq_begin = (np.linalg.norm(magnitud_freq[begin:end], ord=2, axis=0)**2) / (end-begin)
      prom_freq_begin = prom_freq_begin**0.5
      for i in range(begin, end):
        magnitud_freq[i] = magnitud_freq[i] if magnitud_freq[i] > noise_trash*prom_freq_begin else 0

    # INTERPOLACION Y NORMALIZACION
    spectrum = np.interp(np.arange(0, len(magnitud_freq), 1/harmonics), np.arange(0, len(magnitud_freq)),
                              magnitud_freq)
    spectrum = spectrum / np.linalg.norm(spectrum, ord=2, axis=0) 

    spectrum_hann = copy.deepcopy(spectrum)

    # CALCULO DE HPS PARA METODO HANNING
    for i in range(harmonics):
      tmp_spectrum_hann = np.multiply(spectrum_hann[:int(np.ceil(len(spectrum)/(i+1)))], spectrum[::(i+1)])
      if not any(tmp_spectrum_hann):
        break
      spectrum_hann = tmp_spectrum_hann

    def_max = np.argmax(spectrum_hann)
    max_freq = def_max * (sample/max_tol) / harmonics

    nota_parecida, freq_match = tuner(max_freq)
    max_freq = round(max_freq, 1)
    freq_match = round(freq_match, 1)


    # BUFFER DE SONIDO
            
    callback.note_memory.insert(0, nota_parecida)
    callback.note_memory.pop()

    os.system('cls' if os.name=='nt' else 'clear')
    if callback.note_memory.count(callback.note_memory[0]) == len(callback.note_memory):
      print(f"Guitar Tuner: {nota_parecida} {max_freq}/{freq_match}")
    else:
      print(f"...")

  else:
    print('No hay lectura')

try:
  print("Guitar Tuner v1.0")
  print("...")
  with sndvc.InputStream(channels=1, callback=callback, blocksize=steps, samplerate=sample):
    while True:
      time.sleep(0.5)
except Exception as exc:
  print(str(exc))