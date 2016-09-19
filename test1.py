class test1():
    def __init__(self):
        print "test init"
        self.testvar = [[]]

    def test(self):
        print "test"
        y = 1
        print y
        print self.testvar
        self.testvar[0] = [1,2]
        print self.testvar[0]