import unittest
from translator import *

class TestStringMethods(unittest.TestCase):
	
	def setUp(self):
		pass

	def test_french_to_english(self):
		self.assertEqual(french_to_english("") , "Blank text")
		self.assertEqual(french_to_english("Bonjour") , "Hello")

	def test_english_to_french(self):
		self.assertEqual(english_to_french("") , "Blank text")
		self.assertEqual(english_to_french("Hello") , "Bonjour")


if __name__ == '__main__':
	unittest.main()
