#! /usr/bin/env python

import sys
import numpy as np
from halotools.sim_manager import UserSuppliedHaloCatalog
from halotools.empirical_models import PrebuiltHodModelFactory


# Read the SQL query result skipping the header
ff = '../sql_xyz.txt' ; f = open(ff,'r')
data = f.readlines() ; f.close()

# Count number of lines that are not header
nl = 0
for line in data:
    if line[0].isdigit():
        nl = nl + 1
print nl,' haloes'    
xm, ym, zm, mass = [np.zeros(shape=(nl)) for i in range(4)]

ids, upid = [np.arange(0,nl) for i in range(2)]

nl = 0
for line in data:
    if(line[0].isdigit()):
        xm[nl] = float(line.split(',')[0])
        ym[nl] = float(line.split(',')[1])
        zm[nl] = float(line.split(',')[2])

        mass[nl]  = float(line.split(',')[5])*1e10

        ids[nl] = long(float(line.split(',')[7]))
        upid[nl] = abs(ids[nl]-long(float(line.split(',')[8])))-1

        nl = nl + 1

halo_catalog = UserSuppliedHaloCatalog(simname='miliMillennium',\
                                       redshift = 0.0,\
                                       Lbox = 62.5,\
                                       particle_mass = 8.6e8,\
                                       halo_x = xm,\
                                       halo_y = ym,\
                                       halo_z = zm,\
                                       halo_mvir = mass,\
                                       halo_id = ids,\
                                       halo_upid = upid)

halos = halo_catalog.halo_table
print(halos.keys())

model = PrebuiltHodModelFactory('zheng07', conc_mass_model='dutton_maccio14')
model.populate_mock(halocat = halo_catalog)
#print model
