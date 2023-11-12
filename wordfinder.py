"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine for finding random words from dictionary """

    def __init__(self, path):
        """Read dictionary and reports number items read."""

        dict_file = open(path)

        self.words = self.list_of_words(dict_file)

        print(f"{len(self.words)} words read")

    def list_of_words(self, dict_file):
        """list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

t= WordFinder("words.txt")

class SpecialWordFinder(WordFinder):
    """list of words excludes blank lines/comments."""

    def list_of_words(self, dict_file):
        """list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    
c= SpecialWordFinder("words.txt")