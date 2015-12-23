#!/usr/bin/python
from optimum_alg import opt_simulation
import sys

# simulation for opt alg
if __name__ == '__main__':
	adfile = sys.argv[1]
	query_file = sys.argv[2]
	outfile = 'revenue_trajectory.csv' 
	if len(sys.argv) >= 4:
		outfile = str(sys.argv[3])
	num_query = range(10, 300, 10)	
	#num_query = [0]	
	#num_query = [2000]#, 1000, 1500, 2000]		
	import time	
	start = time.time()
	opt_simulation(adfile, query_file, num_query, outfile)
	print("Runing time in second " + str(time.time() - start))
