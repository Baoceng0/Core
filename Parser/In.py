from Core import Core


class In:
    scanner = None
    token = None

    def parse(self):
        if (self.scanner.currentToken() == Core.INPUT):
            self.scanner.nextToken()
            if (self.scanner.currentToken() == Core.ID):
                self.token = self.scanner.getID()
                self.scanner.nextToken()
                if (self.scanner.currentToken() == Core.SEMICOLON):
                    self.scanner.nextToken()

                else:
                    print("Expect ';' in <IN>, but ", self.scanner.currentToken())
                    self.scanner.isErrorParse = True
            else:
                print("Expect 'ID' in <IN>, but ", self.scanner.currentToken())
                self.scanner.isErrorParse = True
        else:
            print("Expect 'INPUT' in <IN>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True

    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}input {self.token};")