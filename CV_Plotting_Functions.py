import numpy as np 
import pandas as pd
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from typing import Tuple, Optional, Iterable
from scipy.optimize import curve_fit

def CVplot(c0,compound,solvent,salt,scanrate,runs):

    fig = plt.figure(figsize= (15,7))

    for run in runs:
        path = f'{compound}_{solvent}_{salt}_{scanrate}_{run}.txt'
        data = pd.read_csv(path, delim_whitespace=True)

        if compound == 'azobenzene':
            time = data.iloc[:, 0]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 2]

        else:
            time = data.iloc[:, 2]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 0]
        
        scan = data.iloc[:, 3]
        ax = fig.add_subplot(2,len(runs),run)
        ax2 = fig.add_subplot(2,len(runs), len(runs) + run)
        ax.scatter(potential,current,s=1, label=f'{compound}{run}')
        ax2.scatter(time, current,s=1, label=f'{compound}{run}')
        ax.grid(True), ax2.grid(True)
        ax.set_xlabel('potential vs. Ag+/Ag (V)'), ax2.set_xlabel('time [s]')
        ax.set_ylabel('current (A)'),ax2.set_ylabel('current (A)')
        ax.legend()

def CVplotpercompound(compound, solvent, salt, scanrates,runs):
    fig = plt.figure(figsize= (15,7))
    ax = fig.add_subplot(1,1,1)
    for scanrate in scanrates:
        path = f'{compound}_{solvent}_{salt}_{scanrate}_1.txt'
        data = pd.read_csv(path, delim_whitespace=True)

        if compound == 'azobenzene':
            time = data.iloc[:, 0]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 2]

        else:
            time = data.iloc[:, 2]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 0]
        
        scan = data.iloc[:, 3]
        data = np.zeros((int(1/3*len(scan)), 3))
        for i in range(0, int(len(scan)*2/3)):
            if scan[i] != 1:
                data[i - int(2/3*len(scan))] = [time[i], (current[i]+current[i + int(1/3*len(scan))])/2, (potential[i]+potential[i +int(1/3*len(scan))])/2]

        ax.scatter(data[:,2],data[:,1],s=1, label=f'{scanrate}')
    ax.grid(True)
    ax.set_xlabel('potential vs. Ag+/Ag (V)')
    ax.set_ylabel('current (A)')
    ax.legend()

def CVdiffusion(compound, solvent, salt, scanrate, runs, bounds):

    for run in runs:
        path = f'{compound}_{solvent}_{salt}_{scanrate}_{run}.txt'
        data = pd.read_csv(path, delim_whitespace=True)

        if compound == 'azobenzene':
            time = data.iloc[:, 0]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 2]

        else:
            time = data.iloc[:, 2]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 0]
        
        scan = data.iloc[:, 3]
        data = np.zeros((int(1/3*len(scan)), 3))
        for i in range(0, int(len(scan)*2/3)):
            if scan[i] != 1:
                data[i - int(2/3*len(scan))] = [time[i], (current[i]+current[i + int(1/3*len(scan))])/2, (potential[i]+potential[i +int(1/3*len(scan))])/2]
        
        
        ymax = max(data[:,1])
        ydata = []
        xdata = []
        for j in range (len(data[:,2])):
            ydata.append(data[j,1])
            xdata.append(data[j,2])
            if data[j,1] == ymax:
                xmax = data[j,2]
                break
        
        
        ydata_fit = []
        xdata_fit = []
        for j in range (0, len(data[:,2])):
            if bounds[0]< data[j, 2] < bounds[1]:
                ydata_fit.append(data[j,1])
                xdata_fit.append(data[j,2])
        
        
        data_f = np.column_stack((xdata_fit, ydata_fit))
        data_fi = data_f[np.lexsort((-data_f[:, 0], data_f[:, 1]))]
        data_fit = data_fi[len(data_fi) // 2:]
        
        def yfunc(x, a, b):
            return a*x+b
        
        popt, pcov = curve_fit(yfunc, data_fit[:, 0], data_fit[:, 1])
        
    
        i = ymax - yfunc(xmax, popt[0], popt[1])
        return i
    
def CVformalpotential(compound, solvent, salt, scanrates, run):
        
        for scanrate in scanrates:
            path = f'{compound}_{solvent}_{salt}_{scanrate}_{run}.txt'
            data = pd.read_csv(path, delim_whitespace=True)

        if compound == 'azobenzene':
            time = data.iloc[:, 0]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 2]

        else:
            time = data.iloc[:, 2]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 0]
        
        scan = data.iloc[:, 3]
        data = np.zeros((int(1/3*len(scan)), 3))
        for i in range(0, int(len(scan)*2/3)):
            if scan[i] != 1:
                data[i - int(2/3*len(scan))] = [time[i], (current[i]+current[i + int(1/3*len(scan))])/2, (potential[i]+potential[i +int(1/3*len(scan))])/2]
        
def CVpeaksepparation(compound, solvent, salt, scanrate, runs):

    for run in runs:
        path = f'{compound}_{solvent}_{salt}_{scanrate}_{run}.txt'
        data = pd.read_csv(path, delim_whitespace=True)

        if compound == 'azobenzene':
            time = data.iloc[:, 0]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 2]

        else:
            time = data.iloc[:, 2]
            current = data.iloc[:, 1]
            potential = data.iloc[:, 0]


