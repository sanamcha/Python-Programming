"""  
A function to search for the first vowel position

Author: SANAM MAHARJAN
Date: June 29, 2025
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns len(s) if there are no vowels.
    
    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.
    
    Examples: 
        first_vowel('hat') returns 1
        first_vowel('grrm') returns 4
        first_vowel('sky') returns 2
        first_vowel('year') returns 1
    
    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """

    result = len(s)  #   In case there is no 'a'
    
    # First if: check for 'a'
    idx_a = introcs.find_str(s, 'a') 
    if idx_a != -1 and idx_a < result:
        result = idx_a

    # Second if: check for 'e' 
    idx_e = introcs.find_str(s, 'e')
    if idx_e != -1 and idx_e < result:
        result = idx_e

        # Check 'i'
    idx_i = introcs.find_str(s, 'i')
    if idx_i != -1 and idx_i < result:
        result = idx_i

    # Check 'o'
    idx_o = introcs.find_str(s, 'o')
    if idx_o != -1 and idx_o < result:
        result = idx_o

    # Check 'u'
    idx_u = introcs.find_str(s, 'u')
    if idx_u != -1 and idx_u < result:
        result = idx_u

    # Check 'y' not at start 
    idx_y = introcs.find_str(s, 'y', 1)
    if idx_y != -1 and idx_y < result:
        result = idx_y 

    return result
     
