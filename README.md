# AnagramSolver
A Python interface for solving algorithms.

Anagrams are solved through creating a new AnagramSolver object, then using the generateAnagrams method to return a list of all possible
anagrams for a given string. The interface includes:

  AnagramSolver(dictFile) initializes a new AnagramSolver object. If no dictFile is specified, the object will automatically reference
    the dict.txt file within this repository.
  AnagramSolver(): str -> AnagramSolver
  requires: dictFile be the name of a readable text file within the same directory of anagram.py
  
  generateAnagrams(self, s, max) returns a list of anagrams for string s. If max is a positive number, only the first max number of 
    anagrams will be returned. If max is None, all anagrams of s will be returned.
  requires: s be a non-empty string, max be either None or a positive integer
