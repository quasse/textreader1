class Directory():
    def __init__(self, text):
        self.text = text
        self.textList = text.split()
        print "def __init__ in TextDatabase, Directory"
        self.readText()

    def readText(self):
        print "readText"
        print self.textList[0]