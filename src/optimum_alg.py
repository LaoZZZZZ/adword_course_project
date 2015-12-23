#!/usr/bin/python

from advertiser import Advertiser
import networkx as nx
#import matplotlib.pyplot as plt

def parseADFileEqualPrice(adfile):
	result = {}
	count = 0
	price = -1
	start = 0
	
	for line in open(adfile,'r'):
		count = count + 1
		if count > 1 :
			ad_temp = line.strip().split(',')
			bid_part = ad_temp[1:len(ad_temp) - 2]
			budget = float(ad_temp[-2])
			bid_list = {}
			for i in range(len(bid_part)):
				p = float(bid_part[i])
				if p > 0:
					if price == -1:
						price = p
					else:
						assert(price == p)
					bid_list[i + 1] = price	
				
			nrange = int(budget/price)
			for k, v in bid_list.items():
				if k in result:
					result[k].append((start,start + nrange))
				else:
					result[k] = [(start,start + nrange)]	
			start = start + nrange
	'''
	for index in range(len(advertisers)):
		for key in ad.bids().keys():
			if key in result:
				result[key].append(index)
			else:
				result[key] = [index]
	'''
	return (price, result, start + 1) 

def parseQuery(query_file, num_query):
	queries = []
	count = 0 
	for line in open(query_file,'r'):
		try:
			index = int(line.strip())
			if count >= num_query:
				break
			queries.append(index)
			count = count + 1
		except Exception as err:
			continue
	return queries

def generateGraph(queries, keyword_budget, price, start):
	# generate the node label
	# generate the graph
	graph = nx.Graph()
	for q in queries:
		if q in keyword_budget:
			for r in keyword_budget[q]:
				for rightnode in range(r[0], r[1]):
					graph.add_edge(start, rightnode)
		start = start + 1	
	return graph



def maximumMatching(graph):
	return len(nx.bipartite.eppstein_matching(graph))/2

def opt_simulation(advfile, query_file, num_query, outfile):
	price, key_budget, start = parseADFileEqualPrice(advfile)
	trajectory = []
	for n in num_query:
		queries = parseQuery(query_file, n)
		graph = generateGraph(queries, key_budget, price, start)
		trajectory.append(maximumMatching(graph))
	handle = open(outfile, 'w')
	for n in num_query:
		handle.write(str(n) + ',')
	handle.write('\n')
	for t in trajectory:
		handle.write(str(t*price) + ',')
	handle.write('\n')
	handle.close()
	
