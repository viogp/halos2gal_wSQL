#! /usr/bin/env python

import eagleSqlTools as sql
import numpy as np

con = sql.connect("xyz", "abc", url="http://virgodb.dur.ac.uk:8080/Millennium")

the_query = """select .1*(.5+floor((log10(stellarMass)+10.)/.1)) as mass,
                      log10(count(*)/power(62.5,3.)/.1) as phi
               from millimil..DeLucia2006a
               where snapnum = 63 and stellarMass > 0 
               group by .1*(.5+floor((log10(stellarMass)+10.)/.1))
               order by mass"""

data = con.execute_query(the_query)

mass = data["mass"] 
phi = data["phi"]

outf = 'delucia_gsmf.txt'
np.savetxt(outf,data)
print 'Output file:',outf
