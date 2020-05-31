#############################################################
# FILE : ex7.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex6 2016 - 2017
# DESCRIPTION: In this file we exercised recursion functions.
#############################################################


# Magic Numbers:

ZERO_STRING = "0"
ONE_STRING = "1"


def print_to_n(n):

    """
    this function gets an n int number and prints the int numbers from
    1 to n count up.
    """

    if n <= 0:
        return
    print_to_n(n-1)
    print(n)


def print_reversed(n):

    """
    this function gets an n int number and prints the int numbers from
    n to 1 count down.
    """

    if n == 1:
        print(n)
    elif n > 1:
        print(n)
        return print_reversed(n - 1)


def has_divisor_smaller_than(n, i):

    """
    this function checks if n has a divisor which is not 1 and is
    smaller than i.
    """

    if i == 1:
        return False
    elif n % i == 0:
        return True
    else:
        return has_divisor_smaller_than(n, i - 1)


def is_prime(n):

    """
    this function gets an n int number and returns True while n is a
    prime number, and returns False if not.
    """

    if n < 2:
        return False
    return not has_divisor_smaller_than(n, n - 1)


def divisors_helper(n, i=1, divisor_list=[]):

    """
    this function checks which int positive numbers are the divisors of
    an n int number and returns them count up in a list. this function helps
    us to implement the divisors function.
    """

    if n == 0:
        return []
    if n < 0:
        n *= -1
    if i == n:
        divisor_list.append(i)
        return divisor_list
    elif n % i == 0:
        divisor_list.append(i)
        return divisors_helper(n, i + 1, divisor_list)
    else:
        return divisors_helper(n, i + 1, divisor_list)


def divisors(n):

    """
    this function uses the function divisors_helper, gets an int
    number and returns a list of all its int positive number divisors
    count up.
    """

    return divisors_helper(n)


def factorial(n):

    """
    this function calculates the factorial number of an n input int
    number which is not negative.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def exp_n_x_helper(n, x, i=0):

    """
    this function gets an n input int number and a real x number and
    returns the function of exponential sum by using the given formula.
    this function helps us to implement the exp_n_x function.
    """

    if i == n:
        return (x ** i) / factorial(i)
    else:
        return (x ** i) / factorial(i) + exp_n_x_helper(n, x, 1 + i)


def exp_n_x(n, x):

    """
    this function uses the exp_n_x_helper function and gets an n input
    int number and an x real number and returns the function of exponential
    sum.
    """

    return exp_n_x_helper(n, x)


def play_hanoi(hanoi, n, src, dest, temp):

    """
    this function solves the game of The Towers of Hanoi.
    """

    if n <= 0:
        return
    # This way we ensure the function will cope with any int value.
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)


def print_binary_sequences_with_prefix(prefix, n):

    """
    this function prints all the combinations of 0 and 1 in length n
    which starts with the prefix. this function helps us to implement the
    print_binary_sequences function.
    """

    if n == 0:
        print(prefix)
    else:
        prefix1 = prefix + ONE_STRING
        prefix0 = prefix + ZERO_STRING
        print_binary_sequences_with_prefix(prefix0, n - 1)
        print_binary_sequences_with_prefix(prefix1, n - 1)


def print_binary_sequences(n):

    """
    this function uses the print_binary_sequences_with_prefix function
    and prints all the possible combinations of 0 and 1 in length n.
    """

    if n == 0:
        print("")
    else:
        print_binary_sequences_with_prefix("", n)


def print_sequences_with_prefix(prefix, char_list, n):

    """
    this function prints all the combinations of chars in a list by the
    length of n which starts with the prefix, while the same char may appear
    more than one time. this function helps us to implement the
    print_sequences function.
    """

    if n == 0:
        print(prefix)
    else:
        for i in range(len(char_list)):
            prefix += char_list[i]
            print_sequences_with_prefix(prefix, char_list, n - 1)
            prefix = prefix[:-1]


def print_sequences(char_list, n):

    """
    this function uses the print_sequences_with_prefix function and
    gets a list of chars, then prints all the possible combinations in
    length n of chars from the list, while the same char may appear more
    than one time.
    """

    if n == 0:
        print("")
    else:
        print_sequences_with_prefix("", char_list, n)


def print_no_repetition_sequences_with_prefix(prefix, char_list, n):

    """
    this function prints all the combinations of chars in a list by the
    length of n which starts with the prefix, while the same char mustn't
    appear more than one time. this function helps us to implement the
    print_no_repetition_sequences function.
    """

    if n == 0:
        print(prefix)
    else:
        for i in range(len(char_list)):
            if char_list[i] in prefix:
                continue
            prefix += char_list[i]
            print_no_repetition_sequences_with_prefix(prefix, char_list, n - 1)
            prefix = prefix[:-1]


def print_no_repetition_sequences(char_list, n):

    """
    this function uses the print_no_repetition_sequences_with_prefix
    function and gets an input list of chars, then prints all the possible
    combinations in length n of chars from the list, while the same char
    mustn't appear more than one time.
    """

    if n == 0:
        print('')
        return
    else:
        print_no_repetition_sequences_with_prefix("", char_list, n)


def no_repetition_sequences_list_with_prefix(prefix, char_list, n, listt):

    """
    this function returns a list of strings of all the combinations of
    chars in a list by the length of n which starts with the prefix, while
    the same char mustn't appear more than one time. this function helps us
    to implement the no_repetition_sequences_list function.
    """

    if n == 0:
        return prefix
    else:
        for i in range(len(char_list)):
            if char_list[i] in prefix:
                continue
            prefix += char_list[i]
            if n == 1:
                listt.append(
                    no_repetition_sequences_list_with_prefix(prefix, char_list,
                                                             n - 1, listt))
            else:
                no_repetition_sequences_list_with_prefix(prefix, char_list,
                                                         n - 1, listt)
            prefix = prefix[:-1]


def no_repetition_sequences_list(char_list, n):

    """
    this function uses the no_repetition_sequences_list_with_prefix
    function and gets an input list of chars, then returns a list of strings
    of all the possible combinations in length n of chars from the list,
    while the same char mustn't appear more than one time.
    """

    if n == 0:
        return [""]
    listt = []
    no_repetition_sequences_list_with_prefix("", char_list, n, listt)
    return listt
