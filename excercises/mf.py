#! /usr/bin/env python

import numpy as np
import os.path, sys
from matplotlib import pyplot as plt

# Volume
volume = np.power(62.5,3.)

# Plot
ytit ='$log(\Phi/{\\rm d}logM\,Mpc^{-3}h^{3})$'
xtit ='$log_{10}(M/{\\rm M}_{\odot}h^{-1})$'

fig = plt.figure()
plt.xlabel(xtit) ; plt.ylabel(ytit)
plt.xlim(9.,15.) ; plt.ylim(-5.5,0)

# Read the SQL query result skipping the header
ff = 'sql_xyz.txt' ; f = open(ff,'r')
data = f.readlines() ; f.close()

# Count number of lines that are not header
nl = 0
for line in data:
    if line[0].isdigit():
        nl = nl + 1
print nl,' read lines'    
mass1, mass2, mass3, mass4 = [np.zeros(shape=(nl)) for i in range(4)]
nl = 0
for line in data:
    if(line[0].isdigit()):
        a = float(line.split(',')[3])
        if (a>0.):
            mass1[nl] = np.log10(a*0.86) +9.

        a = float(line.split(',')[4])
        if (a>0.):        
            mass2[nl] = np.log10(a) + 10.

        a = float(line.split(',')[5])
        if (a>0.):        
            mass3[nl] = np.log10(a) + 10.

        a = float(line.split(',')[6])
        if (a>0.):        
            mass4[nl] = np.log10(a) + 10.

        nl = nl + 1

hist1, bins1 = np.histogram(mass1,bins=80)
hist2, bins2 = np.histogram(mass2,bins=80)
hist3, bins3 = np.histogram(mass3,bins=100)
hist4, bins4 = np.histogram(mass4,bins=20)

dm1 = bins1[1] - bins1[0]
dm2 = bins2[1] - bins2[0]
dm3 = bins3[1] - bins3[0]
dm4 = bins4[1] - bins4[0]
print dm1,dm2,dm3,dm4

x1 = np.zeros(len(hist1))
x2 = np.zeros(len(hist2))
x3 = np.zeros(len(hist3))
x4 = np.zeros(len(hist4))

for i in range(len(hist1)):
    x1[i] = bins1[i] + dm1*0.5
for i in range(len(hist2)):
    x2[i] = bins2[i] + dm2*0.5
for i in range(len(hist3)):
    x3[i] = bins3[i] + dm3*0.5
for i in range(len(hist4)):
    x4[i] = bins4[i] + dm4*0.5

ind = np.where(hist1>0.)
plt.plot(x1[ind],np.log10(hist1[ind]/dm1/volume),'k',label='from np')

ind = np.where(hist2>0.)
plt.plot(x2[ind],np.log10(hist2[ind]/dm2/volume),'r',label='from m_Mean200')

ind = np.where(hist3>0.)
plt.plot(x3[ind],np.log10(hist3[ind]/dm3/volume),'b',label='from m_Crit200')

ind = np.where(hist4>0.)
plt.plot(x4[ind],np.log10(hist4[ind]/dm4/volume),'g',label='from m_TopHat')

#
# Read the SQL query result skipping the header
ff = 'sql_mf_mcrit.txt' ; f = open(ff,'r')
data = f.readlines() ; f.close()

# Count number of lines that are not header
nl = 0
for line in data:
    if line[0].isdigit():
        nl = nl + 1
print nl,' read lines'    
mass, phi = [np.zeros(shape=(nl)) for i in range(2)]
nl = 0
for line in data:
    if(line[0].isdigit()):
        mass[nl] = float(line.split(',')[0])+0.1*0.5
        phi[nl]  = float(line.split(',')[1])
        nl = nl + 1
#print mass,phi
plt.plot(mass,phi,'c',label='MF query')

# Legend
leg = plt.legend(loc=3)
leg.draw_frame(False)

###########################
plt.show()
## Save figure
plotfile = "hmf.pdf"
fig.savefig(plotfile)
print plotfile
print 'Output:', plotfile
