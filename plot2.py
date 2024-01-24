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
A = 0
B = 0

size = dataset.size / 2 - 1

fig, ax = plt.subplots()
plt.ion()

plt.scatter(dataset['Time'], dataset['V'])
plt.scatter(sine['Time'], sine['V'])

plt.show()

fieldNames = ["Initial 1", "Final 1", "Initial 2", "Final 2", "Initial 3", "Final 3", "Initial 4", "Final 4"]
fieldValues = easygui.multenterbox("Please select ranges to locate the minimum value of your data:",
                                   'Min Val', fieldNames)

plt.close()
plt.ioff()


findI1 = float(fieldValues[4])
findF1 = float(fieldValues[5])
findI2 = float(fieldValues[6])
findF2 = float(fieldValues[7])
findI3 = float(fieldValues[0])
findF3 = float(fieldValues[1])
findI4 = float(fieldValues[2])
findF4 = float(fieldValues[3])



sel = np.empty((int(size), 2))
sel2 = np.empty((int(size), 2))
sel3 = np.empty((int(size), 2))
sel4 = np.empty((int(size), 2))


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


n = 0
minVal3 = 100
for _ in range(int(size)):
    if (dataset['Time'][n] > findI3) and (dataset['Time'][n] < findF3):
        sel3[n][0] = dataset['Time'][n]
        sel3[n][1] = dataset['V'][n]
    else:
        sel3[n][0] = nan
        sel3[n][1] = nan

    if (sel3[n][1] < minVal3) and (sel3[n][1] != nan):
        minVal3 = (sel3[n][1])
        A = n

    n = n + 1

n = 0

minVal3 = sel3[A][0]


n = 0
minVal4 = 100
for _ in range(int(size)):
    if (dataset['Time'][n] > findI4) and (dataset['Time'][n] < findF4):
        sel4[n][0] = dataset['Time'][n]
        sel4[n][1] = dataset['V'][n]
    else:
        sel4[n][0] = nan
        sel4[n][1] = nan

    if (sel4[n][1] < minVal4) and (sel4[n][1] != nan):
        minVal4 = (sel4[n][1])
        B = n

    n = n + 1

n = 0

minVal4 = sel4[B][0]


mid = (minVal2-minVal)/2 + minVal
mid2 = (minVal4-minVal3)/2 + minVal3
mid = round(mid,5)
mid2 = round(mid2,5)

minVal2 = round(minVal2,5)
minVal = round(minVal,5)
minVal3 = round(minVal3,5)
minVal4 = round(minVal4,5)

for _ in range(int(size)):
    if sel[n][0] == (minVal):
        yVal = sel[n][1]
    if sel2[n][0] == (minVal2):
        yVal2 = sel2[n][1]
    if sel3[n][0] == (minVal3):
        yVal3 = sel3[n][1]
    if sel4[n][0] == (minVal4):
        yVal4 = sel4[n][1]
    n = n + 1

fig, ax = plt.subplots()
plt.scatter(dataset['Time'], dataset['V'])
plt.scatter(sine['Time'], sine['V'])

plt.scatter(sel[:, 0], sel[:, 1])

plt.scatter(sel2[:, 0], sel2[:, 1])

plt.scatter(sel3[:, 0], sel3[:, 1])

plt.scatter(sel4[:, 0], sel4[:, 1])

val = Amp * np.cos(2*np.pi * 60 * abs(minVal2 - mid))
val2 = Amp * np.cos(2*np.pi * 60 * abs(minVal4 - mid2))


print("Center Method: ")
print(val)
print(val2)
print("Spike Mins: ")
print(float(minVal))
print(float(minVal2))
print(float(minVal3))
print(float(minVal4))
print("Center: ")
print(mid)
print(mid2)

plt.axvline(x=(mid), color='black', linestyle='dashed')
plt.axvline(x=(mid2), color='black', linestyle='dashed')

plt.axvline(x=(minVal), color='black', linestyle='dashed')
plt.axvline(x=(minVal2), color='black', linestyle='dashed')
plt.axvline(x=(minVal3), color='black', linestyle='dashed')
plt.axvline(x=(minVal4), color='black', linestyle='dashed')

plt.axhline(y=(yVal), color='black', linestyle='dashed')
plt.axhline(y=(yVal2), color='black', linestyle='dashed')
plt.axhline(y=(yVal3), color='black', linestyle='dashed')
plt.axhline(y=(yVal4), color='black', linestyle='dashed')

plt.axhline(y=(val), color='red', linestyle='dashed')
plt.axhline(y=(val2), color='red', linestyle='dashed')


plt.show()