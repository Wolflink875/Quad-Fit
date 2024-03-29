import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import*
import scipy.optimize as opt
import easygui

dataset = pd.read_csv('data/Data.csv')
dataset2 = pd.read_csv('data/Data2.csv')

fixLabels = 50
labelsOn = False
phase1 = False
phase2 = True
phase3 = True

Amp = 0.2786*math.sqrt(2)



I = 0
F = 0
I2 = 0
F2 = 0
I3 = 0
F3 = 0

size = dataset.size / 2 - 1
size2 = dataset2.size / 2 - 1

fig, ax = plt.subplots()
plt.ion()

plt.scatter(dataset['Time'], dataset['V'])
plt.scatter(dataset2['Time'], dataset2['V'])
plt.show()

fieldNames = ["Plot 1 Initial", "Plot 1 Final", "Plot 2 Initial", "Plot 2 Final", "Plot 1 Guess", "Plot 2 Guess"]
fieldValues = easygui.multenterbox("Please select ranges for quadratic fit:", 'Quad Fit', fieldNames)
flip = easygui.indexbox("Note: You will need to specify when fitting for a maximum. This will invert the y-values "
                        "of the plot display. Attempting to find a maximum without inverting will result in errors.",
                        "Select One", ("Plt1","Plt2","Both"))
flip1 = False
flip2 = False
if flip == 2:
    flip1 = True
    flip2 = True
if flip == 1:
    flip2 = True
if flip == 0:
    flip1 = True
phase1 = easygui.ynbox("Display Quadratic Funtion?")
#labelsOn = easygui.ynbox("Display Labels?")

plt.close()
plt.ioff()

if fieldValues is not None:
    findI = float(fieldValues[0])
    guess = float(fieldValues[4])
    findF = float(fieldValues[1])
    findI2 = float(fieldValues[2])
    guess2 = float(fieldValues[5])
    findF2 = float(fieldValues[3])
else:
    findI = 0.00328
    guess = 0.004
    findF = 0.00698
    findI2 = 0.00413
    guess2 = 0.005
    findF2 = 0.00672

#----Determine Data Slice Size---------------------
n = 0
for _ in range(int(size)):

    if flip1 == True:
        dataset['V'][n] = -dataset['V'][n]
    if (dataset['Time'][n] == findI):
        I = n
    if (dataset['Time'][n] == findF):
        F = n

    n = n + 1

newSize = F - I + 1
int(newSize)
n = 0
for _ in range(int(size2)):

    if flip2 == True:
        dataset2['V'][n] = -dataset2['V'][n]
    if (dataset2['Time'][n] == findI2):
        I2 = n
    if (dataset2['Time'][n] == findF2):
        F2 = n

    n = n + 1

newSize2 = F2 - I2 + 1
int(newSize2)
#---------------------------------------------------
#----Creating Array For Data Slice------------------
new = np.empty((newSize,2))
j = 0
for a in range(newSize):
    new[j][0] = dataset['Time'][I+j]
    new[j][1] = dataset['V'][I+j]
    j = j+1

new2 = np.empty((newSize2,2))
j = 0
for a in range(newSize2):
    new2[j][0] = dataset2['Time'][I2+j]
    new2[j][1] = dataset2['V'][I2+j]
    j = j+1
#---------------------------------------
#---Creates Poly Fit For Data Slice-----
if (phase1 == True):
    polyline = np.linspace(findI, findF, 100)
    fit = np.poly1d(np.polyfit (new[:,0], new[:,1], 2))
    a = fit.c
    print(fit)
    def f(x):
        return (a[0] * (x ** 2) + a[1] * (x) + a[2])

    result = opt.minimize(f, guess)

    polyline2 = np.linspace(findI2, findF2, 100)
    fit2 = np.poly1d(np.polyfit (new2[:,0], new2[:,1], 2))
    b = fit2.c
    print(fit2)
    def g(x):
        return (b[0]*(x ** 2) + b[1]*(x) + b[2])

    result2 = opt.minimize(g,x0=guess2)



fig,ax = plt.subplots()
plt.ion()
plt.scatter(dataset['Time'], dataset['V'])
plt.scatter(dataset2['Time'], dataset2['V'])

plt.scatter(new[:, 0], new[:, 1])
plt.scatter(new2[:, 0], new2[:, 1])

if (phase1 == True):
    plt.plot(polyline, fit(polyline))
    plt.plot(polyline2, fit2(polyline2))


m = 0
for xy in zip(dataset['Time'], dataset['V']):

    if (m%fixLabels == 0) and (labelsOn == True):
        plt.annotate('(%.2f, %.2f)' % xy, xy=xy)

    m = m + 1

m = 0
for xy in zip(dataset2['Time'], dataset2['V']):

    if (m%fixLabels == 0) and (labelsOn == True):
        plt.annotate('(%.2f, %.2f)' % xy, xy=xy)

    m = m + 1

plt.show()

fieldNames2 = ["Initial 1", "Final 1", "Initial 2", "Final 2"]
fieldValues2 = easygui.multenterbox("Please select ranges to locate the minimum value of your data:",
                                   'Min Val', fieldNames2)

plt.close()
plt.ioff()


if (phase2 == True) and (phase1 == True):

    diff = result.x - result2.x

    if fieldValues2 is not None:
        findI3 = float(fieldValues2[0]) + diff
        findF3 = float(fieldValues2[1]) + diff
        findI4 = float(fieldValues2[2]) + diff
        findF4 = float(fieldValues2[3]) + diff
    else:
        findI3 = 0
        findF3 = 0.00375
        findI4 = 0.00608
        findF4 = 0.00700

    datafit = np.empty((int(size2), 2))

    n = 0
    for _ in range(int(size2)):
        datafit[n][0] = dataset2['Time'][n] + diff
        if flip2 == True:
            datafit[n][1] = -1*dataset2['V'][n]
        else:
            datafit[n][1] = dataset2['V'][n]

        n = n + 1
    n=0
    for _ in range(int(size)):
        if flip1 == True:
            dataset['V'][n] = -dataset['V'][n]
        n = n + 1

    sel = np.empty((int(size), 2))
    sel2 = np.empty((int(size2), 2))

    n=0
    minVal = 100
    for _ in range(int(size)):
        if (datafit[n][0] > findI3) and (datafit[n][0] < findF3):
            sel[n][0] = datafit[n][0]
            sel[n][1] = datafit[n][1] + 0.8
        else:
            sel[n][0] = nan
            sel[n][1] = nan

        datafit[n][1] = datafit[n][1] + 0.8

        if (sel[n][1] < minVal) and (sel[n][1] != nan):
            minVal = sel[n][1]
            I3 = n

        n = n + 1

    minVal = sel[I3][0]

    n = 0
    minVal2 = 100
    for _ in range(int(size2)):
        if (datafit[n][0] > findI4) and (datafit[n][0] < findF4):
            sel2[n][0] = datafit[n][0]
            sel2[n][1] = datafit[n][1]
        else:
            sel2[n][0] = nan
            sel2[n][1] = nan

        if (sel2[n][1] < minVal2) and (sel2[n][1] != nan):
            minVal2 = (sel2[n][1])
            F3 = n

        n = n + 1

    n = 0
    yVal = nan
    yVal2 = nan

    minVal2 = sel2[F3][0]

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
    plt.scatter(datafit[:, 0], datafit[:, 1])
    plt.scatter(sel[:, 0], sel[:, 1])
    plt.scatter(sel2[:, 0], sel2[:, 1])

    val = Amp* np.cos(2*np.pi*60*(minVal-(result.x)))
    val2 = Amp * np.cos(2*np.pi * 60 * abs(minVal2 - (result.x)))
    val3 = Amp * np.cos(2*np.pi * 60 * abs(minVal2 - mid))

    print("Intersect Method: ")
    print(float(yVal))
    print(float(yVal2))
    print("Quad Method: ")
    print(float(val))
    print(float(val2))
    print("Center Method: ")
    print(val3)
    print("Quad Extrema: ")
    print(float(result.x))
    print(float(result2.x))
    print("Spike Mins (corrected): ")
    print(float(minVal))
    print(float(minVal2))
    print("Correction Val: ")
    print(float(diff))
    print("Center (corrected): ")
    print(mid)

    plt.axvline(x=(mid), color='black', linestyle='dashed')
    plt.axvline(x=(result.x), color='gray', linestyle='dashed')

    plt.axvline(x=(minVal), color='black', linestyle='dashed')
    plt.axvline(x=(minVal2), color='black', linestyle='dashed')
    plt.axhline(y=(yVal), color='black', linestyle='dashed')
    plt.axhline(y=(yVal2), color='black', linestyle='dashed')
    plt.axhline(y=(val), color='red', linestyle='dashed')
    plt.axhline(y=(val2), color='red', linestyle='dashed')
    plt.axhline(y=(val3), color='orange', linestyle='dashed')
    plt.axhline(y=(0), color='black')
    plt.scatter(sel[:, 0], sel[:, 1])

    plt.show()
