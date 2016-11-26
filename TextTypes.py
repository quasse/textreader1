class paragraph():
    def __init__(self):
        print "paragraph class"

class sentence():
    def __init__(self):
        print "sentence class"

class word():
    def __init__(self, word, id):
        self.word = word[0]
        self.type = word[1]
        self.id = id

    def getType(self):
        return self.type

    def getWord(self):
        return self.word

    def getId(self):
        return self.id