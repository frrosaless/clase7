# -*- coding: utf-8 -*-
"""e3_franco_rosales_e2_s7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tIhlz5LCVDBKeaxMkvM2mrvrrm1N-b-g
"""

import random as rd
import numpy as np

matriz = np.zeros((3,3), dtype=int)
for i in range(3):
  matriz[i,i] = i + 1

print(matriz)