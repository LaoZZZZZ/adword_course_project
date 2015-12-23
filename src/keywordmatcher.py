#!/usr/bin/python

from keywordrearranger import KeywordRearranger

class KeywordMatcher(object):
	def __init__(self, rearranger, key_set):
		self.__arranger = rearranger
		self.__keyset = key_set
	# needs more work 
	def match(self, new_key):
		new_key = self.__arranger.rearrange(new_key)
		 
