#!/usr/bin/python
from advertiser import Advertiser
import os
import sys
from balancealgorithm import BalanceAlgorithm as BAL
from order_function import *
def parseADFile(adfile):
	keyword = []
	advertisers = []
	count = 1

	for line in open(adfile,'r'):
		if count == 1:
			colnames = line.strip().split(',')
			length = len(colnames)
			keyword = colnames[1:length-2]
		else:
			ad_temp = line.strip().split(',')
			assert(len(ad_temp) == len(keyword) + 3)
			ad_id = int(ad_temp[0])
			bid_keys = {} 
			for i in range(len(keyword)):
				p = float(ad_temp[1 + i])
				if p > 0:
					bid_keys[keyword[i]] = p
			budget = float(ad_temp[-2])
			total_key = int(ad_temp[-1])
			assert(len(bid_keys) == total_key)
			advertisers.append(Advertiser(ad_id,budget, bid_keys))			
		count = count + 1
	return (keyword, advertisers)

def parseQuery(query_file, num_query):
	queries = []
	count = 0 
	for line in open(query_file,'r'):
		count = count + 1
		if count != 1:
			queries.append(int(line.strip()) - 1)
			if count > num_query:
				break
	return queries
def simulation(adfile, query_file, order_func, outfile, num_query):
	keywords, ads = parseADFile(adfile)
	queries = parseQuery(query_file, num_query)		
	print('Number of keywords: ' + str(len(keywords)), 'Number of advertiser: ' + str(len(ads)), 'Number of queries: ' + str(len(queries)))
	test_al = BAL(ads, order_func)
	revenues = []	
	num_drained_advertisers = []
	drained_ids = []
	for q in queries:
		ad = test_al.query(keywords[q],1)
		revenues.append(test_al.revenue())
		num_drained_advertisers.append(test_al.accumulativeDrainedAdvertisers())	
		drained_advertisers = test_al.currentDrainedAdvertisers()
		ids = [str(ad.adID()) for ad in drained_advertisers]
		drained_ids.append(' '.join(ids))
	handle = open(outfile, 'w')
	for i in range(len(revenues)):
		handle.write(str(revenues[i]) + ',' + str(num_drained_advertisers[i]) + ',' + drained_ids[i] +'\n')
	handle.close()

if __name__ == '__main__':
	adfile = sys.argv[1]
	query_file = sys.argv[2]
	order_func = sys.argv[3]
	if order_func == 'ng':
		order_func  = naiveGreedy
	elif order_func == 'nbl':
		order_func = naiveBL
	else:
		assert(order_func == 'gbl')
		order_func = generalizedBL
	outfile = 'revenue_trajectory_bl.csv' 
	if len(sys.argv) >= 5:
		outfile = str(sys.argv[4])
	num_query = 1000
	if len(sys.argv) >= 6:
		num_query = int(sys.argv[5])
		
	import time	
	start = time.time()
	simulation(adfile, query_file, order_func, outfile, num_query )
	print("Runing time in second " + str(time.time() - start))
