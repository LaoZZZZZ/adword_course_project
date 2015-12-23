#!/usr/bin/python


import networkx as nx

class BipartieGraph(object):
	def __init__(self, adv_table):
		self.init(adv_table)
	def init(self, adv_table):
		self.__n_ad = len(adv_table)
		self.__graph = None
		if self.__n_ad > 0:
			self.__n_key = len(adv_table[0])
			self.__graph = nx.Graph()
			for i in range(self.__n_ad):
				for j in range(self.__n_key):
					if adv_table[i][j] > 0:
						self.__graph.add_edge(i, self.__n_ad + j, weight = adv_table[i][j])

	def nComponents(self):
		if self.__graph:
			return nx.number_connected_components(self.__graph)
		else:
			return 0
	def isConnected(self):
		if self.__graph:
			return nx.is_connected(self.__graph)
		else:
			return false


if __name__ == '__main__':

	adv_table = [[0,1,1],[0,1,0], [1,0,1]]
	
	bg = BipartieGraph(adv_table)
	print(bg.isConnected())
	print(bg.nComponents())
			
	
