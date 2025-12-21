'''
class Lang
We need a unique index per word to use as the inputs and targets of the networks later. 
To keep track of this we will use a helper class called Lang.
This has:
word → index (word2index) dictionary
index → word (index2word) dictionary 
A count of each word word2count (will be used to replace rare words later)
'''
class Lang:
    def __init__(self, name: str):
        self.name = name
        # print("Lang type of name: ", type(name))
        self.word2index = {}
        self.word2count = {}
        self.index2word = {0: "SOS", 1: "EOS"}
        self.n_words = 2  # Count SOS and EOS

    def addSentence(self, sentence: str):
        # print("Lang type of sentence: ", type(sentence))
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word: str):
        # print("Lang type of word: ", type(word))
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1