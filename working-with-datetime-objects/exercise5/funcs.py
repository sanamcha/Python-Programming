"""
Functions for parsing time values and determining daylight hours.

Both of these functions will be used in the main project.  You should hold on to them.

Author: SANAM MAHARJAN
Date:   Sep 15, 2025
"""

from datetime import datetime
from dateutil.parser import parse
from pytz import timezone
from dateutil import tz




def str_to_time(timestamp,tzsource=None):
    """
    Returns the datetime object for the given timestamp (or None if timestamp is 
    invalid).
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a time zone, then it should keep that time zone even if
    the value for tzsource is not None.  Otherwise, if timestamp has no time zone 
    and tzsource is not None, then this function will use tzsource to assign 
    a time zone to the new datetime object.
    
    The value for tzsource can be None, a string, or a datetime object.  If it 
    is a string, it will be the name of a time zone, and it should localize the 
    timestamp.  If it is another datetime, then the datetime object created from 
    timestamp should get the same time zone as tzsource.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tzsource: The time zone to use (OPTIONAL)
    Precondition: tzsource is either None, a string naming a valid time zone,
    or a datetime object.
    """
    # HINT: Use the code from the previous exercise and add time zone handling.
    # Use localize if tzsource is a string; otherwise replace the time zone if not None

    try:
        dt = parse(timestamp)
    except ValueError:
        return None
        
    if dt.tzinfo is not None:
        return dt
        
    if tzsource is not None:
        if isinstance(tzsource, str):
            tz = timezone(tzsource)
            return tz.localize(dt)
        elif isinstance(tzsource, datetime):
            return dt.replace(tzinfo=tzsource.tzinfo)
            
    return dt

    


def daytime(time,daycycle):
    """
    Returns True if the time takes place during the day, False otherwise (and 
    returns None if a key does not exist in the dictionary).
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dictionary.
    
    A daycycle dictionary has keys for several years (as strings).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
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
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects using data from the daycycle dictionary.  Also, if the time
    parameter does not have a timezone, we assume that it is in the same timezone 
    as the daycycle dictionary.
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)
    

    tzname = daycycle.get('timezone')
    if tzname is None:
        return None

    tzinfo_cycle = tz.gettz(tzname)
    if tzinfo_cycle is None:
        return None

    if time.tzinfo is None or time.tzinfo.utcoffset(time) is None:
        time = time.replace(tzinfo=tzinfo_cycle)
    else:
        time = time.astimezone(tzinfo_cycle)

    year = time.year
    mm = f"{time.month:02d}"
    dd = f"{time.day:02d}"
    mm_dd = f"{mm}-{dd}"
    year_key = str(year) 
    if year_key not in daycycle:
        return None
    if mm_dd not in daycycle[year_key]:
        return None

    dayinfo = daycycle[year_key][mm_dd]
    sunrise_str = dayinfo.get('sunrise')
    sunset_str  = dayinfo.get('sunset')
    if sunrise_str is None or sunset_str is None:
        return None

    sunrise_dt = str_to_time(f"{year}-{mm}-{dd}T{sunrise_str}", tzname)
    sunset_dt  = str_to_time(f"{year}-{mm}-{dd}T{sunset_str}", tzname)
    if sunrise_dt is None or sunset_dt is None:
        return None

    if sunrise_dt < time < sunset_dt:
        return True
    else:
        return False
    
