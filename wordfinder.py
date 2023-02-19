"""Word Finder: finds random words from a dictionary."""


from random import randint


class WordFinder:
    def __init__(self, file):
        self.file = file
        self.words = None
        self.word_lst = None
        self.get_file()

    def get_file(self):
        '''get file and format word data'''

        with open(self.file, 'r') as file:
            self.word_lst = file.readlines()
            self.words = list(map(lambda x: ''.join(
                list(filter(lambda y: y != "\n", x))), self.word_lst))
            return self.words

    def random_word(self):
        """pick a random word from the word list"""

        index = randint(0, len(self.words)-1)
        return self.words[index]


class SpecialWordFinder(WordFinder):
    """ word finder that searches past blank lines and comments """

    def __init__(self, file):
        super().__init__(file)
        self.remove_nonwords()

    def remove_nonwords(self):
        """search through file and append anything
        that is not a comment or empty space
        """
        actual = []

        for word in self.words:
            if "#" not in word and word:
                actual.append(word)

        self.words = actual
        return self.words


words1 = WordFinder('words.txt')
print(words1.random_word())
worda = SpecialWordFinder('otherwords.txt')
print(worda.random_word())
