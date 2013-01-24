__author__ = 'liuminzhao'

import math

prime= [x for x in range(2,1000000) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]

