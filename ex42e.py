"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""

import re


class TriangleWordsCounter():
    def __init__(self, words_file):
        file_words = ListOfWords(words_file)
        self.words = file_words.get_words()
        self.triangle_numbers = TriangleNumbers(file_words.get_max_theorethical_word_value())

    def count_is(self):
        self.set_triangle_words()
        self.set_count()
        return self.count

    def set_triangle_words(self):
        self.triangle_words = []
        for word in self.words:
            if self.triangle_numbers.check(word.get_value()):
                self.triangle_words.append(word)

    def set_count(self):
        self.count = len(self.triangle_words)


class Word():
    valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, word):
        self.word = word
        self.make_character_points_dict()

    def make_character_points_dict(self):
        self.valid_characters_points = {}
        for points, character in enumerate(self.valid_characters, 1):
            self.valid_characters_points[character] = points

    def get_max_theorethical_value(self):
        return len(self.word) * max(self.valid_characters_points.values())

    def get_value(self):
        value = 0
        for char in self.word:
            value += self.valid_characters_points[char]
        return value


class ListOfWords():
    def __init__(self, words_file):
        self.open_word_list(words_file)

    def open_word_list(self, words_file):
        with open(words_file) as f:
            words_string = f.read()
            take_quotes = re.compile('"')
            words_string = take_quotes.sub("", words_string)
            self.words = [Word(word) for word in words_string.split(",")]

    def get_max_theorethical_word_value(self):
        max_values = [word.get_max_theorethical_value() for word in self.words]
        return max(max_values)

    def get_words(self):
        return self.words


class TriangleNumbers():
    def __init__(self, limit=300):
        self.limit = limit
        self.get_valid_triangle_numbers()

    def get_valid_triangle_numbers(self):
        self.valid_triangle_numbers = []
        n = 1
        tn = 1
        while tn < self.limit:
            self.valid_triangle_numbers.append(tn)
            n += 1
            tn = n * (n + 1) / 2

    def check(self, number):
        return number in self.valid_triangle_numbers


# CPU times: user 7.23 ms, sys: 357 µs, total: 7.59 ms
# Wall time: 8.38 ms
# 162
