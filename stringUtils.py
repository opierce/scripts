#!/usr/bin/env python3
# coding: utf-8

import re
import unittest

def convertToCamelCase(originalString):
	words = re.findall(r"[\w']+", originalString)
	finalWords = []
	for word in words[1:]:
		finalWords.append(word.capitalize())
	return words[0] + "".join(finalWords)

class TestStringUtils(unittest.TestCase):

	def testConvertToCamelCase(self):
		inputString = "wavy/red turban snail"
		expected = "wavyRedTurbanSnail"
		outputString = convertToCamelCase(inputString)
		self.assertEqual(outputString, expected)

if __name__ == '__main__':
	unittest.main()

