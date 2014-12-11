'''
Created on Dec 11, 2014

@author: ds-ga-1007
'''
import unittest
from ClassPackage.StockClass import *
from Utilities.Exceptions import *

class TestStockClass(unittest.TestCase):
    """
    Test whether the instance of StockClass is valid
    """

    def setUp(self):
        print 'Test the validity of intervals'
        self.stockclass = None

    def tearDown(self):
        print 'TestStockClass Over!'


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()