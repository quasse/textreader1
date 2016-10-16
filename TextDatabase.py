import nltk
import numpy as np

class Directory():
    def __init__(self, text, taggedText):
        self.text = text
        self.taggedText = taggedText
        self.textList = text.split()
        self.readText()

    # Reads through text and analyzes certain parts
    # This method is in flux right now
    def readText(self):
        self.organize()
        #self.getCharacters()
        #self.getType(0)

    # Defines where a word is in each the sentence, where the sentence is in the paragraph, where the paragraph is
    # in the chapter, where the chapter is in the book

    # I will organize chapters later because that will involve figuring out how to parse chapters
    def organize(self):
        wordNum = sentNum = grafNum = chptrNum = 0

        #graphs = self.text.split("\n")
        grafs = self.splitGraphs(self.text)

        for x, grafFragment in enumerate(grafs):
            print "g", x, grafFragment
            sents = self.splitSents(grafs[x])
            for y, sentFragment in enumerate(sents):
                print "s", y, sentFragment
            grafNum += 1

    # Returns a list of characters from the text
    # This method is under construction
    def getCharacters(self):
        print "******************************"
        print "INSIDE getCharacters"
        for index, word in enumerate(self.textList):
            print "Word is: " + word
            print "Index is: " + self.getType(index) + "\n"
            if self.getType(index) == "NNP":
                print "+++++++++++++++"
                print self.taggedText[index][0]
                print "++++++++++++++++\n"
        print "***************************"

    # Returns the word type
    def getType(self, wordID):
        print "get type"
        print self.taggedText[wordID][1]
        return self.taggedText[wordID][1]

    # Splits a text into chapters

    #Will have to find chapters

    # Will work on later
    def splitChapters(self, chapters):
        print chapters

    # Splits a block of text into paragraphs
    # I will need to figure out later how to find if paragraphs are split with one line break or two
    def splitGraphs(self, graphs):
        return graphs.split("\n")

    # Splits a block of text into sentences
    def splitSents(self, sents):
        return sents.split(".")

    # Splits a sentence into parts of speech
    def splitWords(self, words):
        print words