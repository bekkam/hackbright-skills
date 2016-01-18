"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # Initialize empty dictionary to identifier 'result_dict'.
    # Remove spaces from input_string and bind result to identifier 'chars_only'.

    # For each unique letter in 'chars_only': get the number of times the character occurs in the
    # input string, and bind the value to identifier 'count'.
    # Save count and character as a key, value pair in result_dict.
    # If count is already a key in result_dict, append character to the list of
    # values for count.

    result_dict = {}

    chars_only = input_string.replace(" ", "").lower()

    for char in set(chars_only):
        count = chars_only.count(char)
        if count not in result_dict.keys():
            result_dict[count] = [char]
        else:
            value = result_dict.get(count) + [char]
            result_dict[count] = value

    # Get the highest key stored in result_dicts, and return its list of value(s), sorted
    # alphabetically
    most_repeats_count = max(result_dict.keys())
    return sorted(result_dict.get(most_repeats_count))

# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.


def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    # Create a dictionary with unique word lengths as keys, and bind each key's value to
    # the list of words of that length:
    # 1. Initialize empty dictionary 'result_dict'
    # 2. For each word in words, if the length of the word has not been stored as
    # a key in the dictionary, store <word length, [word]> as a key value pair
    # 3. If the word has been stored as a key in result_dict, append word to the list
    # of values, and sort the list.

    result_dict = {}
    for word in words:
        if len(word) not in result_dict:
            result_dict[len(word)] = [word]
        else:
            result_dict[len(word)] += [word]
            result_dict[len(word)].sort()

    return result_dict.items()

##############################################################################
# You can ignore everything below this.
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
