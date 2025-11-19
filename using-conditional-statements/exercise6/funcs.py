"""  
A collection of functions to support the translation of words into Pig Latin.

This module contains two functions.  The first function searchs for the location of the 
first vowel.  The second function uses this as a helper to perform the conversion.

Author: SANAM MAHARJAN
Date: June 30, 2025
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.
    
    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.
    
    Examples: 
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1
    
    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    result = len(s)
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
		
	# return -1 if no vowel found
    return result if result < len(s) else -1





def pigify(s):
    """
    Returns a copy of s converted to Pig Latin
    
    Pig Latin is childish encoding of English that adheres to the following rules:
    
    1.  The vowels are 'a', 'e', 'i', 'o', 'u', as well as any 'y'
        that is not the first letter of a word. All other letters are consonants.
        
        For example, 'yearly' has three vowels  ('e', 'a', and the last 'y') 
        and three consonants (the first 'y', 'r', and 'l').
    
    2.  If the English word begins with a vowel, append 'hay' to the end of the word 
        to get the Pig Latin equivalent. For example, 'ask 'askhay' and 'use' becomes 
        'usehay'.
    
    3.  If the English word starts with 'q', then it must be followed by'u'; move 
        'qu' to the end of the word, and append 'ay'.  Hence 'quiet' becomes
        'ietquay' and 'quay' becomes 'ayquay'.
    
    4.  If the English word begins with a consonant, move all the consonants up to 
        the first vowel (if any) to the end and add 'ay'.  For example, 'tomato' 
        becomes 'omatotay', 'school' becomes 'oolschay'. 'you' becomes 'ouyay' and 
        'ssssh' becomes 'sssshay'.
    
    Parameter s: the string to change to Pig Latin
    Precondition: s is a nonempty string with only lowercase letters. If s starts with
    'q', then it starts with 'qu'.
    """

	# starts with a vowel
    idx = first_vowel(s)
    if idx == 0:
        return s + 'hay'

	# starts with 'qu'
    if s.startswith('qu'):
        return s[2:] + 'qu' + 'ay'

	# consonant(s) first
    if idx > 0:
        return s[idx:] + s[:idx] + 'ay'
    else:
        return s + 'ay'


    

    