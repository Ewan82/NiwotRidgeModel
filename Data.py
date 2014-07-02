import numpy as np
from matplotlib.mlab import csv2rec
dat=csv2rec('NiwotRidgeModelDat.csv')

class dalecData( ):

  def __init__(self):

max(dat.ta_fill[(dat.jd==190) & (dat.year==2010)])
