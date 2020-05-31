#############################################################
# FILE : hangman.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex4 2016 - 2017
# DESCRIPTION: In this file we implemented the game Hangman.
# This file contains 5 functions which are described on the
# README file and below each function.
#############################################################


from hangman_helper import *


def update_word_pattern(word, pattern, letter):

    """
    This function gets as inputs word, current pattern and a letter and
    returns an updated pattern which includes the same letter.
    """

    new_pattern = ""

    for i in range((len(word))):
        if word[i] == letter:
            new_pattern += word[i]
        else:
            new_pattern += pattern[i]
    return new_pattern


def run_single_game(words_list):

    """
    This function gets the words list and implements the hangman game
    itself.
    """

    chosen_word = get_random_word(words_list)
    wrong_guess_lst = []
    pattern = "_" * len(chosen_word)
    msg = DEFAULT_MSG
    error_count = len(wrong_guess_lst)
    while len(wrong_guess_lst) < MAX_ERRORS and pattern != chosen_word:
        display_state(pattern, error_count, wrong_guess_lst, msg)
        user_input = get_input()
        if user_input[0] == LETTER:
            chosen_letter = user_input[1]
            if (len(chosen_letter) > 1) or (chosen_letter.islower() is False):
                msg = NON_VALID_MSG
            elif (chosen_letter in pattern) or \
                    (chosen_letter in wrong_guess_lst):
                msg = ALREADY_CHOSEN_MSG + chosen_letter
            elif chosen_letter in chosen_word:
                pattern = update_word_pattern(chosen_word, pattern,
                                              chosen_letter)
                msg = DEFAULT_MSG
            elif chosen_letter not in chosen_word:
                wrong_guess_lst.append(chosen_letter)
                error_count += 1
                msg = DEFAULT_MSG
        elif user_input[0] == HINT:
            filtered_words = filter_words_list(words_list, pattern,
                                               wrong_guess_lst)
            letter = choose_letter(filtered_words, pattern)
            msg = HINT_MSG + letter
    if error_count == MAX_ERRORS:
        msg = LOSS_MSG + chosen_word
    else:
        msg = WIN_MSG
    display_state(pattern, error_count, wrong_guess_lst, msg, True)


def filter_words_list(words, pattern, wrong_guess_lst):

    """
    This function gets as an input the words list, the current pattern and
    the list of wrong guesses and returns a new list which includes only the
    words from the input list which may fit the previous pattern and
    guesses.
    """

    filtered_words = []
    for word in words:
        if len(word) == len(pattern):
            filtered_words.append(word)

    filtered_words2 = []
    i = 0
    for word in filtered_words:
        temp_word = ""
        for char in pattern:

            if char == word[i] or char == "_":
                temp_word += char
            i += 1

        if temp_word == pattern:
            filtered_words2.append(word)
        i = 0
    final_list = filtered_words2[:]
    for word in filtered_words2:
        for wrong_guess in wrong_guess_lst:
            if (wrong_guess in word) and (word in final_list):
                final_list.remove(word)

    return final_list


def choose_letter(words, pattern):

    """
    This function gets an input words list (which is fitting to the current
    pattern) and also gets the current pattern, and returns the most frequent
    letter in the list.
    """

    words_string = ''.join(words)
    dicta = {}
    for letter in words_string:
        if letter in dicta:
            dicta[letter] += 1
        else:
            if letter not in pattern:
                dicta[letter] = 1

    return max(dicta, key=lambda x: dicta[x])[0]


def main():

    """
     This function does not get and does not return any values, but
     implements three operations: 1. loads words.txt file into a list by
     using the load_words function. 2. runs the game by using the
     run_single_game function. 3. at the end of each game asks the user if
     he wants to play again, by using the function get_input.
    """

    list_of_words = load_words()
    run_single_game(list_of_words)
    user_input = get_input()

    while user_input[1]:
        run_single_game(list_of_words)
        user_input = get_input()


if __name__ == "__main__":
    start_gui_and_call_main(main)
    close_gui()
