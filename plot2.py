import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import*
import scipy.optimize as opt
import easygui

sine = pd.read_csv('data/Data.csv')

dataset = pd.read_csv('data/Data2.csv')



Amp = 0.3736*math.sqrt(2)




I = 0
F = 0

size = dataset.size / 2 - 1

fig, ax = plt.subplots()
plt.ion()

plt.scatter(dataset['Time'], dataset['V'])
plt.scatter(sine['Time'], sine['V'])

plt.show()

fieldNames = ["Initial 1", "Final 1", "Initial 2", "Final 2"]
fieldValues = easygui.multenterbox("Please select ranges to locate the minimum value of your data:",
                                   'Min Val', fieldNames)

plt.close()
plt.ioff()

if fieldValues is not None:
    findI1 = float(fieldValues[0])
    findF1 = float(fieldValues[1])
    findI2 = float(fieldValues[2])
    findF2 = float(fieldValues[3])
else:
    findI1 = 0
    findF1 = 0.00375
    findI2 = 0.00608
    findF2 = 0.00700


sel = np.empty((int(size), 2))
sel2 = np.empty((int(size), 2))


n=0
minVal = 100
for _ in range(int(size)):
    if (dataset['Time'][n] > findI1) and (dataset['Time'][n] < findF1):
        sel[n][0] = dataset['Time'][n]
        sel[n][1] = dataset['V'][n]
    else:
        sel[n][0] = nan
        sel[n][1] = nan

    if (sel[n][1] < minVal) and (sel[n][1] != nan):
        minVal = sel[n][1]
        I = n

    n = n + 1

minVal = sel[I][0]

n = 0
minVal2 = 100
for _ in range(int(size)):
    if (dataset['Time'][n] > findI2) and (dataset['Time'][n] < findF2):
        sel2[n][0] = dataset['Time'][n]
        sel2[n][1] = dataset['V'][n]
    else:
        sel2[n][0] = nan
        sel2[n][1] = nan

    if (sel2[n][1] < minVal2) and (sel2[n][1] != nan):
        minVal2 = (sel2[n][1])
        F = n

    n = n + 1

n = 0

minVal2 = sel2[F][0]

mid = (minVal2-minVal)/2 + minVal

minVal2 = round(minVal2,5)
minVal = round(minVal,5)

for _ in range(int(size)):
    if dataset['Time'][n] == (minVal):
        yVal = dataset['V'][n]
    if dataset['Time'][n] == (minVal2):
        yVal2 = dataset['V'][n]
    n = n + 1

fig, ax = plt.subplots()
plt.scatter(dataset['Time'], dataset['V'])
plt.scatter(sine['Time'], sine['V'])

plt.scatter(sel[:, 0], sel[:, 1])

plt.scatter(sel2[:, 0], sel2[:, 1])

val = Amp * np.cos(2*np.pi * 60 * abs(minVal2 - mid))


print("Center Method: ")
print(val)
print("Spike Mins: ")
print(float(minVal))
print(float(minVal2))
print("Center: ")
print(mid)

plt.axvline(x=(mid), color='black', linestyle='dashed')
plt.axvline(x=(minVal), color='black', linestyle='dashed')
plt.axvline(x=(minVal2), color='black', linestyle='dashed')
plt.axhline(y=(yVal), color='black', linestyle='dashed')
plt.axhline(y=(yVal2), color='black', linestyle='dashed')
plt.axhline(y=(val), color='red', linestyle='dashed')

plt.show()