class test1():
    def __init__(self):
        self.testvar = [[]]

    def test(self):
        y = 1
        print y
        print self.testvar
        self.testvar[0] = [1,2]
        print self.testvar[0]