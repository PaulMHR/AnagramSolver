#**********************************************************
# Assignment2:
# UTOR user_name: rudmikpa
# First Name: Paul
# Last Name: Rudmik
# Student #: 1001366087
#
#
# Honour Code: I pledge that this program represents my own
# program code and that I have coded on my own. I received
# help from no one in designing and debugging my program.
# I have also read the plagiarism section in the course info sheet
# of CSC 148 and understand the consequences.
#*********************************************************


from letterManager import *


class NegativeError(Exception):
    pass


class AnagramSolver:
    """Interface for finding anagrams from a given string."""
    def __init__(self, dictFile = 'dict.txt'):
        """(str) -> AnagramSolver
        Creates AnagramSolver object using specified text file as source for available anagram words.
        Object variables include:

            self._list -> list of words, derived from reading dictFile
            self._dictFile -> original input string representing name of dictFile
            self._n -> variable integer used for generateAnagrams program.

        >>> a = AnagramSolver("dict.txt")
        >>> isinstance(a, AnagramSolver)
        True
        >>> a._dictFile
        'dict.txt'
        """
        self._list = self._generate_word_list(dictFile)
        self._dictFile = dictFile
        self._n = 0

    def _generate_word_list(self, dictFile):
        """(str) -> list
        Return list of words given from file specified by dictFile string.

        >>> a = AnagramSolver("dict.txt")
        >>> lst = a._generate_word_list("dict.txt")
        >>> lst[0:5]
        ['aback', 'abacus', 'abalone', 'abandon', 'abase']
        >>> lst[-6:-1]
        ['zoo', 'zoology', 'zoom', 'zounds', 'zucchini']
        """
        word_list = []
        try:
            dict_f = open(str(dictFile))
        except FileNotFoundError:
            raise FileNotFoundError("Text file required in the same directory as anagram.py")
        for entry in dict_f.readlines():
            word_list.append(entry.strip())
        return word_list

    def _does_include(self, s1, s2):
        """(LetterManager, str, str) -> object
        Return inclusion report if s1 contains s2, False otherwise.

            inclusion report -> [contained word, remaining characters]

        >>> a = AnagramSolver("dict.txt")
        >>> a._does_include("cats", "cat")
        ['cat', 's']
        >>> a._does_include("cats", "dogs")
        False
        """
        lm1 = LetterManager(s1)
        lm2 = LetterManager(s2)
        result = lm1.Subtract(lm2)

        if result:
            contained_word = s2
            remaining_chars = str(result)
            return [contained_word, remaining_chars]
        else:
            return False

    def _shorten_list(self, s):
        """(str) -> NoneType
        Alters self._list to list of inclusion reports on words contained by s.

        >>> a = AnagramSolver("dict.txt")
        >>> a._shorten_list("cats")
        >>> a._list
        [['act', 's'], ['cast', ''], ['cat', 's'], ['sac', 't'], ['sat', 'c'], ['scat', '']]
        """

        new_lst = []

        if isinstance(self._list[0], list):
            for inclusion_report in self._list:
                word = inclusion_report[0]
                new_lst.append(word)
            self._list = new_lst
            new_lst = []

        for word in self._list:
            inclusion_report = self._does_include(s, word)
            if inclusion_report:
                new_lst.append(inclusion_report)

        self._list = new_lst

    def _get_anagram_list(self, s, iteration_num = 1, previous_words = []):
        """(str, int, list) -> list of lists of str
        Return a list containing iteration_num number of anagrams for s.
        The final parameter, previous_words, is used for recursive purposes only.

        >>> a = AnagramSolver("dict.txt")
        >>> a._get_anagram_list("office key", 3)
        [['eke', 'icy', 'off'], ['eke', 'off', 'icy'], ['ice', 'key', 'off']]
        """
        master_lst = []                          #represents the list of all generated anagrams.
        old_word_lst = self._list                #copy the _list used in the previous function call.
        self._shorten_list(s)                    #shorten _list to include only "anagram-able" words in
                                                 #respect to input string s.

        for inclusion_report in self._list:                     #loop through the shortened list.

            word = inclusion_report[0]
            remaining_characters = inclusion_report[1]

            if not remaining_characters:                        #BASE CASE: the tested word is an exact match for s.
                test = previous_words + [word] 
                if test not in master_lst:
                    master_lst.append(test)      #Add anagram to the list.
                if self._n == iteration_num:
                    self._list = old_word_lst                   #Restore _lst to its previous version
                    return master_lst
                else:
                    self._n += 1                                #Indicate another anagram has been found.

            elif remaining_characters:                          #RECURSIVE CASE: the tested word has extra characters.
                sub_list_grab = self._get_anagram_list(remaining_characters, iteration_num, previous_words + [word])
                if sub_list_grab:                               #If anything was found...
                    for anagram in sub_list_grab:
                        if anagram not in master_lst:
                            master_lst.append(anagram)
                    if self._n == iteration_num:
                        self._list = old_word_lst               #Restore _lst to its previous version
                        return master_lst

            if inclusion_report == self._list[-1]:              #If the entire list has been looped through...
                self._list = old_word_lst                       #Restore _lst to its previous version
                return master_lst

        #Activated iff self._lst == []
        self._list = old_word_lst                               #Restore _lst to its previous version
        return master_lst

    def generateAnagrams(self, s, max):
        """(str, int) -> list of lists of str
        Return a list containing iteration_num number of anagrams for s.
        Implements "0 max" functionality, and resets object parameters.

        >>> a = AnagramSolver("dict.txt")
        >>> a.generateAnagrams("office key", 0)
        [['eke', 'icy', 'off'], ['eke', 'off', 'icy'], ['ice', 'key', 'off'], ['ice', 'off', 'key'], ['icy', 'eke', 'off'], ['icy', 'off', 'eke'], ['key', 'ice', 'off'], ['key', 'off', 'ice'], ['key', 'office'], ['off', 'eke', 'icy'], ['off', 'ice', 'key'], ['off', 'icy', 'eke'], ['off', 'key', 'ice'], ['office', 'key']]
        """
        if not isinstance(s, str):
            raise TypeError("Non-empty string required for input.")
        elif not isinstance(max, int):
            raise TypeError("Non-negative integer input required for input.")
        elif max < 0:
            raise NegativeError("Non-negative integer input required for input.")
        else:
            if max == 0:
                result = self._get_anagram_list(s, None)
            elif max > 0:
                result = self._get_anagram_list(s, max)
            self._n = 0
            return result
