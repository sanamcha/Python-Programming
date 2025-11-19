"""  
A function to extract names from e-mail addresses.

Author: SANAM MAHARJAN  
Date: JUN 30, 2025
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.
    
    We assume (see the precondition below) that the e-mail address is in one of
    two forms:
        
        last.first@megacorp.com
        first.last@mompop.net
    
    where first and last correspond to the person's first and last name.  Names
    are not empty, and contain only letters. Everything after the @ is guaranteed 
    to be exactly as shown.
    
    The function preserves the capitalization of the e-mail address.
    
    Examples: 
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'
    
    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the two address formats described above
    """
    # You must use an if-else statement in this function.
    
    idx = introcs.find_str(s, '@')
    username = s[:idx] #everything before '@'

    # inspecting format of email address, everyting after '@'
    email = s[idx + 1:]
    if email == 'megacorp.com':
        # format is last.first 
        # extract after dot
        first = introcs.find_str(username, '.')
        return username[first + 1:]
    else:
        # if email is 'mompop.net, format is first.last
        # extract before dot
        first = introcs.find_str(username, '.')
        return username[:first]
