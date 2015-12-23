#!/usr/bin/python

from advertiser import Advertiser

def generalizedBL(adv, keyword):
	return -1 * adv.phi(keyword)

def naiveBL(adv, keyword):
	return -1 * adv.remainingBudget()

def naiveGreedy(adv, keyword):
	return -1 * adv.bids()[keyword]



if __name__ == '__main__':
	bids = {'sofa':10.0, 'spray':1.0}
	budget = 100.0
	ad = Advertiser(1,budget, bids)
	print(generalizedBL(ad, 'sofa'))	
	print(naiveBL(ad, 'sofa'))	
	print(naiveGreedy(ad, 'sofa'))	
