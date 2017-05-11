#! /usr/bin/env python

import eagleSqlTools as sql
import numpy as np

con = sql.connect("xyz", "abc", url="http://virgodb.dur.ac.uk:8080/Millennium")

the_query = """select x,y,z,velx,vely,velz,
                   np,m_Crit200,halfmassRadius,vmax,
                   haloID,firstHaloInFOFgroupId
               from millimil..MPAHalo 
               where snapnum = 63"""

data = con.execute_query(the_query)

outf = 'sql_haloes.txt'
np.savetxt(outf,data)
print 'Output file:',outf
