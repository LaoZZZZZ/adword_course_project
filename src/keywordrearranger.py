#!/usr/bin/python

from operator import itemgetter
class KeywordRearranger(object):
	def __init__(self, frequent_list):
		self.__top_list = frequent_list
	def rearrange(self, new_key):
		top_part = []
		low_part = []
		for k in new_key:
			if k in self.__top_list:
				top_part.append((self.__top_list[k],k))
			else:
				low_part.append(k)
		top_part.sort()
		freq,w = zip(*top_part)
		top_part = list(w)
		low_part.sort()
		rearranged = low_part + top_part
		return rearrangeda


if __name__ == '__main__':
	frequent_list = {'aba': 10, 'ccd':100, 'cup':15}
	arranger = KeywordRearranger(frequent_list)
	
	keys = ['aba', 'cce', 'cup','acd']
	print(arranger.rearrange(keys))
				
