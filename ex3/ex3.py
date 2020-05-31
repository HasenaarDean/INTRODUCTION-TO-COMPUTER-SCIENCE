#!/usr/bin/env python3

#############################################################
# FILE : ex3.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex3 2016 - 2017
# DESCRIPTION: this file contains 8 functions which are
# described on the README file and below each function.
#############################################################

import math


def create_list():

    """
    This function gets string inputs from the user by using loops
    and returns a list of all those strings. The function stops
    when it gets an empty string, and do not add the empty string
    as another value of the returned list.
    """

    strings_list = []
    string_input = input()
    while string_input != "":
        strings_list.append(string_input)
        string_input = input()
    return strings_list


def concat_list(str_list):

    """
    This function returns the concatenation of items in an input list.
    """

    concatenation = ""
    for stringg in str_list:
        concatenation += stringg
    return concatenation


def average(num_list):

    """
    This function returns the average of float numbers.
    """

    num_sum = 0
    if num_list:
        for num in num_list:
            num_sum += num
        return float(num_sum) / len(num_list)
    else:
        return None


def cyclic(lst1,lst2):

    """
    This function checks whether or not one input list is a cyclic
    permutation of another input list.
    """

    if len(lst1) != len(lst2):
        return False
    cyclic_lst = []
    for i in range(1, len(lst1)+1):
        for j in range(len(lst1)):
            # now we use the formula of cyclic indentation
            cyclic_lst.append(lst1[(j+i) % len(lst1)])
            if cyclic_lst == lst2:
                return True
        cyclic_lst = []
    return False


def histogram(n,num_list):

    """
    This function returns the histogram of int numbers in an input list,
    and its maximum number plus one is given too as an input (called n).
    """

    histogram_list = []
    for k in range(n):
        histogram_list.append(0)

    for i in range(len(num_list)):
        for j in range(n):
            if j == num_list[i]:
                histogram_list[j] += 1
    return histogram_list


def prime_factors(n):

    """
    This function gets an int positive number and returns its products
    of factorization.
    """

    fact_list = []

    for j in range(2, int(math.sqrt(n)+1)):
        while n % j == 0:
            fact_list.append(j)
            n = n / j
        if n / j == 1:
            break
    if n > 1:
        fact_list.append(int(n))
    return fact_list


def cartesian(lst1, lst2):

    """
    This function returns the cartesian product of two input lists.
    """

    cartesian_product_lst = []
    if lst1 == [] or lst2 == []:
        return []
    else:
        for i in range(len(lst1)):
            for j in range(len(lst2)):
                cartesian_product_lst.append([lst1[i], lst2[j]])
    return cartesian_product_lst


def pairs(n,num_list):

    """
    This function gets an input list of int numbers and another int
    number called n, and returns all the pairs of two different numbers
    in the list which their sum is n.
    """

    pairs_list = []
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == n:
                pairs_list.append([num_list[i], num_list[j]])
    return pairs_list
