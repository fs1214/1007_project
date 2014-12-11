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


    def test_EmptyInput(self):
        """
        When some of the inputs are null, test whether it will raise the exception.
        """
        emptyinputlist = [('','',''),('','2010/1/1',''),('IBM','',''),('','2010/1/1','2010/5/1')]
        for item in emptyinputlist:
            stock_name,start_date,end_date = item
            with self.assertRaises(EmptyInputException):
                self.stockclass = Stock(stock_name,start_date,end_date)  
    
    def test_InvalidDate(self):
        """
        When the input of date is invalid, test whether it will raise the exception.
        """
        invaliddatelist = [('IBM','2010.1.1','2010.5.1'),('IBM','abc','de'),('IBM','a2010/1/1','201f/5/1')]
        for item in invaliddatelist:
            stock_name,start_date,end_date = item
            with self.assertRaises(DateInputException):
                self.stockclass = Stock(stock_name,start_date,end_date)  
    
    
    def test_InvalidDateRange(self):
        """
        When the end date is before the start date, test whether it will raise the exception.
        """
        invaliddatelist = [('IBM','2010/1/1','2009/5/1'),('IBM','2010/3/3','2010/3/2')]
        for item in invaliddatelist:
            stock_name,start_date,end_date = item
            with self.assertRaises(DateRangeException):
                self.stockclass = Stock(stock_name,start_date,end_date) 
    
    def test_InvalidEndDate(self):
        """
        When the end date is beyond the current time, test whether it will raise the exception.
        """
        invaliddatelist = [('IBM','2010/1/1','2015/5/1'),('IBM','2010/3/3','2048/3/2')]
        for item in invaliddatelist:
            stock_name,start_date,end_date = item
            with self.assertRaises(EndDateException):
                self.stockclass = Stock(stock_name,start_date,end_date)   

    def test_InvalidStockName(self):
        """
        When the stock name could not be found in the yahoo finance data between the start date and end date, 
        test whether it will raise the exception.
        """
        invalidstocklist = [('11111','2010/1/1','2010/5/1'),('cba','2010/1/1','2010/5/1'),('&*ibm','2010/1/1','2010/5/1')]
        for item in invalidstocklist:
            stock_name,start_date,end_date = item
            with self.assertRaises(StockNameInputException):
                self.stockclass = Stock(stock_name,start_date,end_date)   

    def test_ValidStock(self):
        """
        When the input of date is invalid, test whether it will raise the exception.
        """
        validstocklist = [('IBM','2010/1/1','2010/5/1'),('ibm','2013/1/1','2014/1/1')]
        for item in validstocklist:
            stock_name,start_date,end_date = item
            self.assertTrue(Stock(stock_name,start_date,end_date))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()