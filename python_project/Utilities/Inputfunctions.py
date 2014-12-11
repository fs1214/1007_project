'''
Created on 2014.12.9

@author: apple
'''

import re
import pandas.io.data as web
import datetime
from Utilities.Exceptions import *

def IsValidStockName(stock_name,start_date,end_date):
    """
    Check whether the input is a valid stock name between this period.
    """
    if isinstance(stock_name, str):
        #Check whether input of list has a valid form
        try:
            df =web.DataReader(stock_name,'yahoo',start_date,end_date)
        except:
            return False
        else:
            return True
    else:
        return False

def ParseStockName(stock_name):
    """
    Parse stock name when the input is a valid stock name.
    """
    return stock_name.upper()

def IsValidDate(date_string):
    """
    Check whether the input is a valid date.
    """
    if isinstance(date_string, str):
        #Check whether input of list has a valid form
        try:
            datetime.datetime.strptime(date_string, '%Y/%m/%d')
            return True
        except ValueError:
            return False
    else:
        return False

def ParseDate(date_string):
    """
    Parse when the input is a valid date.
    """
    return datetime.datetime.strptime(date_string, '%Y/%m/%d')
        

def IsEmptyInput(stock_name,start_date,end_date):
    """
    Check whether the input is null or not.
    """
    if stock_name == '' or start_date == '' or end_date == '':
        return True
    else:
        return False

def IsValidDateRange(start_string, end_string):
    """
    Check whether the end_string is more than start_string
    """
    start_date = ParseDate(start_string)
    end_date = ParseDate(end_string)
    if end_date > start_date:
        return True
    else:
        return False

def IsValidEndDate(end_string):
    """
    Assume the end date is a valid date, then check whether the end date is before the current time
    """
    end_date = ParseDate(end_string)
    if end_date <= datetime.datetime.now():
        return True
    else:
        return False


def IsValidNum(num_string):
    """
    Check whether the trade amount is positive integer.
    """
    try:
        num = int(num_string)
    except:
        return False
    if num < 0:
        return False
    else:
        return True

def ParseValidNum(num_string):
    """
    Parse when the trade amount input is valid.
    """
    if IsValidNum(num_string):
        return int(num_string)
    else:
        raise TradeAmountException()       

def IsEmptyPortfolio(dictionary):
    """
    Check whether the portfolio is empty.
    """
    if dictionary == {}:
        return True
    else:
        return False
    
