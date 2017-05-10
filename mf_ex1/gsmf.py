#! /usr/bin/env python

import numpy as np
import os.path, sys
from matplotlib import pyplot as plt

# Plot
ytit ='$log(\Phi/{\\rm d}logM\,Mpc^{-3}h^{3})$'
xtit ='$log_{10}(M/{\\rm M}_{\odot}h^{-1})$'

fig = plt.figure()
plt.xlabel(xtit) ; plt.ylabel(ytit)
plt.xlim(6.5,12.5) ; plt.ylim(-5.5,0)

# Observations from Baldry
ff = 'gsmf-B12.txt' ; oh0 = 0.7
ologM, ophi, oe = np.loadtxt(ff,usecols=[0,2,3],unpack=True)
ologM = ologM + np.log10(oh0)
ologphi = np.log10(ophi) - 3. - 3*np.log10(oh0)
oerr = oe/ophi/np.log(10.)

plt.errorbar(ologM,ologphi,yerr=oerr,color='r',ecolor='r',fmt='o',label='Baldry+12')

## Schechter function from Panter'07
#oh0 = 0.71
#fs = 1.-1.222
#phis = 0.0022
#lms = np.log10(1.005) + 11. 
#mm = 10.**(ologM - lms)
#phi = np.log(10)*phis*(mm**fs)*np.exp(-mm)
#phi = np.log10(phi) - 3*np.log10(oh0)  
#plt.plot(ologM + np.log10(oh0), phi,'r',label='Panter+07 Schechter fit')

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

# Baryon fraction
fb = 0.04/0.308 

plt.plot(mass + np.log10(fb),phi,'k',label='M$_{\\rm halo, DB}$*f_b')

# Reproduce the knee
vals = np.interp(ologM,mass + np.log10(fb),phi) - ologphi 
val1 = -np.min(abs(vals)) ; epsilon = round(np.power(10.,val1),2)
plt.plot(mass + np.log10(fb), phi+val1,'k--',label='M$_{\\rm halo, DB}\cdot f_b\cdot$'+str(epsilon))

# DeLucia MF 
ff = 'delucia_gsmf.txt' 
mass, phi = np.loadtxt(ff,unpack=True)
plt.plot(mass,phi,'g',label='DeLucia+06')

# Legend
leg = plt.legend(loc=3)
leg.draw_frame(False)

###########################
plt.show()
# Save figure
plotfile = "gsmf.pdf"
fig.savefig(plotfile)
print plotfile
print 'Output:', plotfile
