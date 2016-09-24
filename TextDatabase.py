import nltk

class Directory():
    def __init__(self, text, taggedText):
        self.text = text
        self.taggedText = taggedText
        self.textList = text.split()
        self.readText()

    # Reads through text and analyzes certain parts
    # This method is in flux right now
    def readText(self):
        self.getCharacters()
        self.getType(0)

    # Returns a list of characters from the text
    # This method is under construction
    def getCharacters(self):
        for index, word in enumerate(self.textList):
            if self.getType(index) == "NNP":
                print self.taggedText[index][0]

    # Returns the word type
    def getType(self, wordID):
        return self.taggedText[wordID][1]