"""
A simple function comparing datetime objects.

Author: SANAM MAHARJAN
Date:   Sep 10, 2025
"""
# import datetime
from datetime import datetime, date

def is_before(d1,d2):
	"""
	Returns True if event d1 happens before d2.

	Values d1 and d2 can EITHER be date objects or datetime objects.
	If a date object, assume that it happens at midnight of that day. 

	Parameter d1: The first event
	Precondition: d1 is EITHER a date object or a datetime object

	Parameter d2: The first event
	Precondition: d2 is EITHER a date object or a datetime object
	"""
	# HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
	if isinstance(d1, date) and not isinstance(d1, datetime):
		d1 = datetime(d1.year, d1.month, d1.day)
	if isinstance(d2, date) and not isinstance(d2, datetime):
		d2 = datetime(d2.year, d2.month, d2.day)

	return d1 < d2
	


	


	
	