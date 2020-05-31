
#############################################################
# FILE : bmi.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A program that calculates the BMI of a 
# magician. 
#############################################################

import math

# Magic Numbers:

BMI_MINIMUM_PROPER_VALUE = 18.5
BMI_MAXIMUM_PROPER_VALUE = 24.9


def is_normal_bmi(spells_per_hour, wand):
    """This function returns the boolean value whether or not
    someone is an intelligent magician"""

    formula = spells_per_hour/wand**2
    return bool((formula >= BMI_MINIMUM_PROPER_VALUE) and
                (formula <= BMI_MAXIMUM_PROPER_VALUE))
