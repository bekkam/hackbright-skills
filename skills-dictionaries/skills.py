"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    return set(words)


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    """

    return set(list1) & set(list2)


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    # get unique words in string
    # for each unique word, count number of times it occurs in string
    # add to dictionary, where key = unique words, value = number times it occured

    uniq_dict = {}
    input_list = input_string.split(" ")

    uniq_words = set(input_list)

    for word in uniq_words:
        uniq_dict[word] = input_list.count(word)
    return uniq_dict


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    # create a dictionary with English as key, and Pirate as value

    string = """    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey"""

    pirate_dict = {}
    for line in string.split("\n"):
        words = line.split(None)
        if len(words) > 2:
            # If there are three arguments after splitting the line, concat the 2nd and 3rd args -
            # This is pretty gross, but I couldn't get a regex to capture the pirate words.
            words[1] += " " + words[2]
        pirate_dict[words[0]] = words[1]

    result_list = []

    # For each word in the argument, return the original word unless the term is in the
    # pirate dictionary. If the word is in the pirate dictionary, return the
    # pirate translation. Store the words to be returned in result_list.  Return result_list
    # as a string, joined with a whitespace
    for word in phrase.split():
        if word in pirate_dict.keys():
            result_word = pirate_dict.get(word)
        else:
            result_word = word
        result_list.append(result_word)

    return " ".join(result_list)


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    # create an empty dictionary, word_dict.
    # for each word in words, if word length is already a key, add word to the key's list of values
    # else, create new key in form of (word length, [word])
    # return word_dict.items() to return the key value pairs as a tuple
    word_dict = {}

    for word in words:
        key = len(word)
        if key in word_dict.keys():
            value = word_dict.get(key)
            word_dict[key] = value + [word]
        else:
            word_dict[key] = [word]

    return word_dict.items()


def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    # SOLUTION 1: Using set and comprehension
    uniq_nums = set(input_list)

    result = []

    pairs = [[-(num), num] for num in uniq_nums if num * -1 in uniq_nums]

    for item in pairs:
        if item[0] <= item[1]:
            result.append((item[0], item[1]))

    result.sort()
    return result

    # SOLUTION 2: Using filter and set
    # filter input_list include only numbers that have their negative value also in input_list
    # and bind the list to sums_to_zero
    # bind the unique set of sums_to_zero to pairs
    # for each number in set of pairs, append the number and its negative to the result list once
    # sort the result list and return the result

    """sums_to_zero = filter(lambda x: x * -1 in input_list, input_list)

    pairs = set(sums_to_zero)

    result = []

    for num in pairs:
        if [num, -(num)] not in result:
            result.append([-(num), num])

    result.sort()
    return result
    """

##############################################################################
# You can ignore everything below this.


def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
