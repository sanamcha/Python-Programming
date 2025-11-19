"""  
A completed test script for the Pig Latin module.

Author: SANAM MAHARJAN
Date: June 30, 2025
"""
import funcs
import introcs


def test_first_vowel():
    """
    Test procedure for the function first_vowel()
    """
    print('Testing first_vowel()')
    # No vowels
    result = funcs.first_vowel('grrm')
    introcs.assert_equals(-1,result)
    
    # Letter a
    result = funcs.first_vowel('pat')
    introcs.assert_equals(1,result)
    
    # Letter e
    result = funcs.first_vowel('step')
    introcs.assert_equals(2,result)
    
    # Letter i
    result = funcs.first_vowel('strip')
    introcs.assert_equals(3,result)
    
    # Letter o
    result = funcs.first_vowel('stop')
    introcs.assert_equals(2,result)
    
    # Letter u
    result = funcs.first_vowel('truck')
    introcs.assert_equals(2,result)
    
    # Letter y, not a vowel
    result = funcs.first_vowel('ygglx')
    introcs.assert_equals(-1,result)
    
    # Letter y as vowel
    result = funcs.first_vowel('sky')
    introcs.assert_equals(2,result)
    
    # Various multi-vowel combinations
    result = funcs.first_vowel('apple')
    introcs.assert_equals(0,result)
    
    result = funcs.first_vowel('sleep')
    introcs.assert_equals(2,result)
    
    result = funcs.first_vowel('year')
    introcs.assert_equals(1,result)
    
    # Feel free to add more


def test_pigify():
    """
    Test procedure for the function pigify()
    """
    print('Testing pigify()')
        
	# starts with vowel
    result = funcs.pigify('ask')
    introcs.assert_equals('askhay', result)

	# Add more tests:
    result = funcs.pigify('quiet')
    introcs.assert_equals('ietquay', result)

    result = funcs.pigify('school')
    introcs.assert_equals('oolschay', result)

    result = funcs.pigify('you')
    introcs.assert_equals('ouyay', result)

    result = funcs.pigify('ssssh')
    introcs.assert_equals('sssshay', result)

    result = funcs.pigify('yearly')
    introcs.assert_equals('earlyyay', result)

    result = funcs.pigify('rhythm')
    introcs.assert_equals('ythmrhay', result)

    result = funcs.pigify('x')
    introcs.assert_equals('xay', result)

test_first_vowel()
test_pigify()
print('Module funcs passed all tests.')