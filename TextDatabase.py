import nltk
import numpy as np
import re

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
        # Vars for identifying text elements
        wordNum = sentNum = grafNum = chptrNum = 0

        grafs = self.splitGraphs(self.text)

        '''
        Embedded for loop that numbers each chapter, paragraph, sentence, and word
        and adds data to a list

        Eventually I will need to put the grafFragment, sentFragment, and wordFragment into a list with info
        '''
        # Enumberates through a list of text split in paragraphs
        for x, grafFragment in enumerate(grafs):
            #print "g", grafNum, grafFragment
            sents = self.splitSents(grafs[x])
            grafNum += 1
            # Enumerates through a list of text split into sentences. Under construction
            for y, sentFragment in enumerate(sents):
                print "s", sentNum, sentFragment
                words = self.splitWords(sents[y])
                sentNum += 1
                for z, wordFrgament in enumerate(words):
                    print wordFrgament

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

    '''
    Splits a block of text into paragraphs. Returns a list
    I will need to figure out later how to find if paragraphs are split with one line break or two
    '''
    def splitGraphs(self, graphs):
        return graphs.split("\n")

    '''
    Splits a block of text into sentences. Returns a list
    Ends each sentence with a period
    '''
    def splitSents(self, sents):
        # This code is copied from http://stackoverflow.com/questions/4576077/python-split-text-on-sentences
        caps = "([A-Z])"
        prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
        suffixes = "(Inc|Ltd|Jr|Sr|Co)"
        starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
        acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
        websites = "[.](com|net|org|io|gov)"

        text = " " + sents + "  "
        text = text.replace("\n", " ")
        text = re.sub(prefixes, "\\1<prd>", text)
        text = re.sub(websites, "<prd>\\1", text)
        if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")
        if "a.m." in text: text = text.replace("a.m.", "a<prd>m<prd>")
        if "..." in text: text = text.replace("...", "<prd><prd><prd>")
        text = re.sub("\s" + caps + "[.] ", " \\1<prd> ", text)
        text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
        text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
        text = re.sub(caps + "[.]" + caps + "[.]", "\\1<prd>\\2<prd>", text)
        text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
        text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
        text = re.sub(" " + caps + "[.]", " \\1<prd>", text)
        if "\"" in text: text = text.replace(".\"", "\".")
        if "!" in text: text = text.replace("!\"", "\"!")
        if "?" in text: text = text.replace("?\"", "\"?")
        text = text.replace(".", ".<stop>")
        text = text.replace("?", "?<stop>")
        text = text.replace("!", "!<stop>")
        text = text.replace("<prd>", ".")
        sentences = text.split("<stop>")
        sentences = sentences[:-1]
        sentences = [s.strip() for s in sentences]
        return sentences

    # Splits a sentence into parts of speech
    def splitWords(self, words):
        return words.split(" ")