#!/usr/bin/python

from advertiser import Advertiser 
def compare(ad1, ad2, keyword):
	if not ad2.hasBid(keyword):
		return True
	elif not ad1.hasBid(keyword) and ad2.hasBid(keyword):
		return False
	else:
		return ad1.phi(keyword) > ad2.phi(keyword)


if __name__ == '__main__':
	ad1 = Advertiser(100, {'sofa':11, 'spray':5, 'cup' : 15})
	ad2 = Advertiser(100, {'sofa':10, 'spray':1, 'iphone': 80})
	print(compare(ad1,ad2, 'sofa'))
	print(compare(ad1,ad2, 'spray'))
	print(compare(ad1,ad2, 'cup'))
	print(compare(ad1,ad2, 'iphone'))
