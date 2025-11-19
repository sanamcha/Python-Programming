"""  
A function to check the validity of a numerical string

Author: SANAM MAHARJAN
Date: June 30, 2025
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.
    
    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.
    
    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).
    
    Examples: 
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False
    
    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """

    # for exactly "0"
    if s == '0':
        return True

    # not start with '0' or with ',' or end with ','
    if introcs.find_str(s, '0') == 0 or introcs.find_str(s, ',') == 0 or introcs.find_str(s, ',') == len(s)-1:
        return False

    # contain only digits or commas
    for char in s:
        if not (char.isdigit() or char == ','):
            return False

    # Split on commas
    parts = s.split(',')
    # If no comma, it must be length 1–3
    if len(parts) == 1:
        return 1 <= len(s) <= 3

    # for groups 1–3 digits
    if not (1 <= len(parts[0]) <= 3):
        return False

    # All other groups exactly 3 digits
    for part in parts[1:]:
        if len(part) != 3:
            return False

    return True

    
