#!/usr/bin/python

import os
import sys
import networkx as nx

class KeywordChunkDivider(object):
	def __init__(self):
		self.__chunks = []
		# keep track of those keyword that have already been in one chunk
		self.__checked_advertisers = set()
		# keep track of those keyword that has already been visited 
		# in the current traversal
		self.__visited_advertisers = set()
	def findChunks(self, adv_key_table):
		self.__chunks = []
		self.__checked_advertisers.clear()
		self.__visited_advertisers.clear()
		nad = len(adv_key_table)
		
		for ad in range(nad):	
			if not ad in self.__checked_advertisers:
				chunk = set() 
				start = 0
				while start < len(adv_key_table[ad]):
					if adv_key_table[ad][start] > 0:
						break
					start = start + 1
				self.dfs(ad, start, chunk, adv_key_table)
				if len(chunk) > 0:
					self.__chunks.append(chunk)
		return self.__chunks
	def dfs(self, ad, k, chunk, table):
		
		if ad < len(table) and  not ad in self.__checked_advertisers:
			self.__visited_advertisers.add(ad)
			chunk.add(k)
			j = ad + 1
			while j < len(table):
				if table[j][k] > 0:
					self.dfs(j, k, chunk, table)
				j = j + 1
			j = 0
			for j in range(len(table[ad])):
				if table[ad][j] > 0 and j != k:
					self.dfs(ad, j, chunk, table)	
					
			self.__visited_advertisers.remove(ad)
			self.__checked_advertisers.add(ad)

if __name__ == '__main__':
	graph = [[0,1, 1],[1,0,0], [0,0,1]]
	divider = KeywordChunkDivider()
	print(divider.findChunks(graph))
			
			
