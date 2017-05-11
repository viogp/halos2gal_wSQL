#! /usr/bin/env python

import numpy as np

x = np.arange(10)
print 'Lenght of x=',len(x)

j = 0
for i in range(len(x)):
     if x[i]>2:
            j = j + 1
            print i,j
