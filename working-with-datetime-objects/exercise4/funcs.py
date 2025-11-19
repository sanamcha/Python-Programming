"""
Functions for parsing time values from text.  

While these functions are similar to functions found in the assignment, they 
are missing timezone information.  The next exercise will modify these 
functions to make them compatible with the assignment.

Author: SANAM MAHARJAN
Date:   Sep 15, 2025
"""
from dateutil.parser import parse
from datetime import date, datetime

def str_to_time(timestamp):
    """
    Returns the datetime object for the given timestamp (or None if the stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to convert the
    timestamp to a datetime object.  If it is not a valid date (so the parser crashes), 
    this function should return None.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    """
    # Hint: Use a try-except to return None if parsing fails
    try:
        return parse(timestamp)
    except (ValueError, TypeError):
        return None

    


def sunset(date, daycycle):
	"""
	Returns the sunset datetime (day and time) for the given date

	This function looks up the sunset from the given daycycle dictionary. If the
	daycycle dictionary is missing the necessary information, this function 
	returns the value None.

	A daycycle dictionary has keys for several years (as int).  The value for each year
	is also a dictionary, taking strings of the form 'mm-dd'.  The value for that key 
	is a THIRD dictionary, with two keys "sunrise" and "sunset".  The value for each of 
	those two keys is a string in 24-hour time format.

	For example, here is what part of a daycycle dictionary might look like:
		
		"2015": {
			"01-01": {
				"sunrise": "07:35",
				"sunset":  "16:44"
			},
			"01-02": {
				"sunrise": "07:36",
				"sunset":  "16:45"
			},
			...
		}

	Parameter date: The date to check
	Precondition: date is a date object

	Parameter daycycle: The daycycle dictionary
	Precondition: daycycle is a valid daycycle dictiday:02d}"
    mm_dd = f"{mm}-{dd}"
    
    # Try getting year dict
    if yr_int in daycycle:
        ydict = daycycle[yr_int]
    elif yr_str in daycycle:
        ydict = daycycle[yr_str]
    else:
        return None
    
    # Try getting the day dict
    if mm_dd not in ydict:
        return None
    d = ydict[mm_dd]
    
    # Try getting sunset time
    if "sunset" not in d:
        return None
    t = d["sunset"]
    if not isinstance(t, str) or len(t) == 0:
        return None
    
    # Build ISO datetime string
    iso = f"{yr_int:04d}-{mm}-{dd}T{t}"
    return str_to_time(iso)
onary, as described above
	"""
	# HINT: ISO FORMAT IS 'yyyy-mm-ddThh:mm'.  Find the sunset value by constructing a
	# string in ISO format and calling str_to_time.

	try:
		# Extract year and month-day 
		year_int = date.year
		year_str = str(year_int)
		month_day = date.strftime('%m-%d')

		# try interger year and string year
		# ydict = None
		if year_int in daycycle:
			ydict = daycycle[year_int]
		elif year_str in daycycle:
			ydict = daycycle[year_str]
		else:
			return None
		
		# check if month-day exists
		if month_day not in ydict:
			return None

		# Get sunset time string
		sunset_time = ydict[month_day].get('sunset')
		if not isinstance(sunset_time, str) or not sunset_time:
			return None
			
		# ISO format string: 'yyyy-mm-ddThh:mm'
		iso_string = f"{year_int:04d}-{month_day}T{sunset_time}"
		
		# Parse using str_to_time
		result = str_to_time(iso_string)
		return result
		
	except (KeyError, TypeError):
		return None
