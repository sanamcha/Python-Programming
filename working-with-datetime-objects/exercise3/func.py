"""
A simple function computing time elapsed

Author: SANAM MAHARJAN
Date:   Sep 15, 2025
"""
# import datetime
from datetime import date, datetime


def past_a_week(d1,d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.
    
    If d1 is after d2, or d2 is less than a week after d1, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.  If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The second event
    Precondition: d2 is EITHER a date object or a datetime object
    """
	# HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
	# convert date to datetime objects
    if type(d1) is date and type(d1) is not datetime:
	    d1 = datetime.combine(d1, datetime.min.time())
    if type(d2) is date and type(d2) is not datetime:
	    d2 = datetime.combine(d2, datetime.min.time())

	# compute the difference
    delta = d2-d1
	# Return True if at least 7 full days
    return delta.days >= 7

