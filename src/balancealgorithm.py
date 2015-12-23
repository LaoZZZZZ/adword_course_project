#!/usr/bin/python


from advertiser import Advertiser
from bidlist import BidList
from order_function import *
class BalanceAlgorithm(object):
	def __init__(self, advertisers, order_function):
		self.__ads = advertisers
		self.__revenue = 0.0
		self.__drainedkeywords = []
		self.__drainedadvertiser = set()
		self.__currentDrainedAdvertiser = set() 
		self.__orderfunc = order_function
		self.init()
	def init(self):
		self.__bids = {} 
		for ad in self.__ads:
			for keyword, price in ad.bids().items():
				if keyword in self.__bids:
					if ad.inGreen(keyword):
						self.__bids[keyword].push(ad)
				else:
					if ad.inGreen(keyword):
						bd_list = BidList(keyword, self.__orderfunc)
						bd_list.push(ad)
						self.__bids[keyword] = bd_list
	def query(self, keyword, top_k):
		matched_bids = []
		self.__currentDrainedAdvertiser.clear()
		if keyword in self.__bids:
			bdlist = self.__bids[keyword]
			while not bdlist.empty():
				try:
					top_ad = bdlist.pop()
					if top_ad.inGreen(keyword):
						matched_bids.append(top_ad)
						self.charge(matched_bids[-1], keyword)
						if matched_bids[-1].isDrained() and not matched_bids[-1] in self.__drainedadvertiser:
							self.__currentDrainedAdvertiser.add(matched_bids[-1])
						#only choose the top k ad to list
					if len(matched_bids) == top_k:
						break
				except Exception as err:
					print("All relevant advertisers has run out of budget for keyword: " + keyword)
					break
			if bdlist.empty():
				del self.__bids[keyword]
				self.__drainedkeywords.append(keyword)
		self.__drainedadvertiser.update(self.__currentDrainedAdvertiser)
		return matched_bids
	def DrainedKeywords(self):
		return self.__drainedkeywords
	def bottomUp(self):
		return len(self.__bids) == 0			
	def charge(self, ad, keyword):
		# if this advertiser still have enough balance for bid this keyword
		self.__revenue += ad.bids()[keyword]
		ad.spend(keyword)
		# heapify other keyword if necessary.
		for mykey in ad.bids().keys():
			if mykey in self.__bids:
				self.__bids[mykey].heapify(ad)
		# only if this advertiser still have enough balance for next bid
		# we will add this advertiser back to this keyword list.
		if ad.inGreen(keyword):
			self.__bids[keyword].push(ad)
	def revenue(self):
		return self.__revenue
	def accumulativeDrainedAdvertisers(self):
		return len(self.__drainedadvertiser)
	def currentDrainedAdvertisers(self):
		return self.__currentDrainedAdvertiser
			
				
if __name__ == '__main__':
	'''
	ad1 = Advertiser(1,40, {"sofa":19, "spray": 19.499})
	ad2 = Advertiser(2,40, {"sofa":20, "spray": 19.5})
	ad3 = Advertiser(3,20, {"spray": 20})
	'''
	ad1 = Advertiser(1,40, {"sofa":19})
	ad2 = Advertiser(2,40, {"sofa":20})
	advertisers = [ad1, ad2]
 	blg = BalanceAlgorithm(advertisers, naiveGreedy)
	while True:
		bidder = blg.query('sofa', 1)
		
		if len(bidder) == 0:
			break
	print(blg.revenue())
			
