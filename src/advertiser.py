#!/usr/bin/python

import math
# An object that represents the advertiser
class Advertiser(object):
	def __init__(self,ad_id, budget, bids):
		assert(budget > 0)
		self.__id = ad_id
		self.__budget = float(budget)
		self.__bids = bids
		self.__remaining = budget
		self.__minimum_bid = min(self.__bids.values())
	def remainingBudget(self):
		return self.__remaining 
	# check if this advertiser still have enough budget for the bids.
	def inGreen(self, keyword):
		return self.__remaining >= self.__bids[keyword]
	def isDrained(self):
		return self.__remaining < self.__minimum_bid
	def bids(self):
		return self.__bids
	def spend(self, keyword):
		assert(keyword in self.__bids)
		self.__remaining = self.__remaining - self.__bids[keyword]
	def phi(self, keyword):
		assert(keyword in self.__bids)
		return self.__bids[keyword] * (1 - math.exp(-1 * self.remainingBudget()/self.__budget))		
	def hasBid(self, keyword):
		return keyword in self.__bids		
	def __eq__(self, other):
		return self.__id == other.__id
	def __hash__(self):
		return self.__id
	def __ne__(self, other):
		return self.__id != other.__id
	def adID(self):
		return self.__id
	def __str__(self):
		return ','.join(self.__id)
if __name__ == '__main__':
	bids = {'sofa':10.0, 'spray': 1.0}
	query = ['sofa', 'spray']
	budget = 100.0
	
	ad = Advertiser(budget, bids)
	for q in query:
		print(ad.remainingBudget(),ad.phi(q))
		ad.spend(q)
	
	
