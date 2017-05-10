#! /usr/bin/env python

import sys
import numpy as np
from halotools.sim_manager import UserSuppliedHaloCatalog
from halotools.empirical_models import PrebuiltHodModelFactory


# Read the SQL query result skipping the header
ff = 'sql_haloes.txt' ; f = open(ff,'r')
data = f.readlines() ; f.close()

# Count number of lines that are not header
nl = 0
for line in data:
    if line[0].isdigit():
        nl = nl + 1
print nl,' haloes'    
xm, ym, zm, vx, vy, vz, mass, r50, vmax = [np.zeros(shape=(nl)) for i in range(9)]

nump, ids, upid = [np.arange(0,nl) for i in range(3)]

xm, ym, zm, vx, vy, vz, nump, mass, r50, vmax, ids, upids = np.loadtxt(ff,unpack='True') 

mass = mass*np.power(10.,10.)
upid = abs(ids-upids) -1

halo_catalog = UserSuppliedHaloCatalog(simname='miliMillennium',\
                                       redshift = 0.0,\
                                       Lbox = 62.5,\
                                       particle_mass = 8.6e8,\
                                       halo_x = xm,\
                                       halo_y = ym,\
                                       halo_z = zm,\
                                       halo_vx = vx,\
                                       halo_vy = vy,\
                                       halo_vz = vz,\
                                       halo_rvir = r50,\
                                       halo_mvir = mass,\
                                       halo_id = ids,\
                                       halo_upid = upid)

halos = halo_catalog.halo_table
print(halos.keys())

model = PrebuiltHodModelFactory('leauthaud11', conc_mass_model='dutton_maccio14')
model.populate_mock(halocat = halo_catalog)
print model.mock.galaxy_table.keys() 
