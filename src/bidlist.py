#!/usr/bin/python
import heapq
from advertiser import Advertiser
# Holds a list of advertisers who bid the keyword
class BidList(object):
	def __init__(self, bid_keyword, order_function):
		self.__keyword = bid_keyword
		self.__advertiser = []
		self.__orderfunc = order_function
		self.__changed = set() 
	def empty(self):
		return len(self.__advertiser) == 0
	def size(self):
		return len(self.__advertiser)
	def push(self, ad):
		if ad.hasBid(self.__keyword) and ad.inGreen(self.__keyword):
			item = (self.__orderfunc(ad,self.__keyword),ad)
			heapq.heappush(self.__advertiser, item)
	def pop(self):
		if len(self.__advertiser):
			# if the top one is in the changed list
			# then need to update the list and reheapify.
			if self.__advertiser[0][1] in self.__changed:
				updated = []
				for i in range(len(self.__advertiser)):
					if self.__advertiser[i][1] in self.__changed:
						if self.__advertiser[i][1].inGreen(self.__keyword):
							value = self.__orderfunc(self.__advertiser[i][1],self.__keyword) 
							updated.append((value, self.__advertiser[i][1]))
					else:
						updated.append(self.__advertiser[i])
				self.__advertiser = updated
				self.__changed.clear()
				heapq.heapify(self.__advertiser)
		if len(self.__advertiser) == 0:
			raise IndexError("out of range. There is no advertiser for keyword " + self.__keyword)
		return heapq.heappop(self.__advertiser)[1]
	# Called when one the value of one add is changed
	# Only reheapify only if the changed ad is the largest one
	def heapify(self, ad):
		if ad.hasBid(self.__keyword):
			self.__changed.add(ad)
	def __eq__(self, other):
		return self.__keyword == other.__keyword
	def __hash__(self):
		return self.__keyword
	def __ne__(self, other):
		return not self.__eq__(other)
	def __len__(self):
		return len(self.__advertiser)


if __name__ == '__main__':
	ad1 = Advertiser(1,40, {"sofa":19, "spray": 19.499})
	ad2 = Advertiser(2,39.5, {"sofa":20, "spray": 19.5})
	ad3 = Advertiser(3,20, {"spray": 20})

	sofa = BidList("sofa")
	spray = BidList("spray")
	sofa.push(ad1)
	sofa.push(ad2)
	spray.push(ad1)
	spray.push(ad2)
	spray.push(ad3)
	for i in range(3):	
		temp = spray.pop()
		print(temp.adID(), temp.remainingBudget())
	spray.push(ad1)
	spray.push(ad2)
	spray.push(ad3)
	print("***********deleting***********")		
	while not sofa.empty():
		temp = sofa.pop()
		temp.spend("sofa")
		print(temp.adID(), temp.remainingBudget())	
		spray.heapify(temp)
	print("***************updated*********")
	print(len(spray))
	while not spray.empty():	
		temp = spray.pop()
		temp.spend('spray')
		print(temp.adID(), temp.remainingBudget())
