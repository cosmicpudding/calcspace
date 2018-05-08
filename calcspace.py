# CalcSpace: Given conditions, calculate the space taken by these observations
# Note: should be run on happili-01
# V.A. Moss (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$07-may-2018 17:00:00$"
__version__ = "0.1"

import os
import sys
from astropy.io import ascii
import numpy as np

totspace = 0

# conditions
cmd = 'du -sh /data*/apertif/17*'
print 'Command: %s' % cmd
results = os.popen(cmd)
for x in results:
	totspace = totspace + float(x.split()[0])

print 'Total space taken: %.2f GB' % (totspace/1e6)

