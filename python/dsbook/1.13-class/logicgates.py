'''logic gates pedigogical class inheritance example'''

class LogicGate(object):
    '''general gate definition'''
    def __init__(self, name):
        self.label = name
        self.output = None

    def getlabel(self):
        '''get gate label'''
        return self.label

    def getoutput(self):
        '''get gate logical output'''
        self.output = self.dogatelogic()
        return self.output

class BinaryGate(LogicGate):
    '''gate with two input pins'''
    def __init__(self, name):
        LogicGate.__init__(self, name)
        self.pin1 = None
        self.pin2 = None

    def getpin1(self):
        '''get value on pin1'''
        return self.pin1

    def getpin2(self):
        '''get value on pin2'''
        return self.pin2

class ANDGate(BinaryGate):
    '''ANDing logical gate'''
    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def dogatelogic(self):
        '''AND gate logic implementation'''
        if self.pin1 == 1 and self.pin2 == 1:
            return 1
        else:
            return 0

def main():
    '''main area'''
    gate1 = ANDGate("G1")
    print gate1.getoutput()

main()
