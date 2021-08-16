import Core

class Id:
    name = None
    value = None
    isDecl = None
    isInit = None

    def __init__(self,n,v,d,i):
        self.name = n
        self.value =v
        self.isInit = i
        self.isDecl = d

    def checkDecl(self):
        return self.isDecl

    def checkInit(self):
        return self.isInit

    def printName(self):
        return self.name

    def printValue(self):
        return self.value