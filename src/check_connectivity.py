#!/usr/bin/python

import os
import numpy as np
from partition_proc import BipartieGraph as BP
def parseADFile(adfile):
	keyword = []
	advertisers = []
	table = np.genfromtxt(adfile, delimiter = ',', skip_header = 1)
	
	return table

if __name__ == '__main__':
	adfile = 'advister_info.csv'
	
	table = parseADFile(adfile)
	adv_table = table[:,1:table.shape[1] - 2]
	
	print(len(adv_table), len(adv_table[0]))
	g = BP(adv_table)
	print(g.isConnected())
	print(g.nComponents())
		


