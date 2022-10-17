class Term():
    def __init__(self, ttype, targs, tname):
        self.ttype = ttype
        self.targs = targs
        self.tname = tname

    def __str__(self)->str:
        if self.ttype == 'variable':
            return f'{self.tname}'
        elif self.ttype == 'constructor':
            targs = ""
            for i in self.targs:
                targs += str(i) + ","
            
            return f"{self.tname}({targs[:-1]})"
        return ""
    
    def __eq__(self, __o: object) -> bool:
        return str(self) == str(0)

    def __ne__(self, __o: object) -> bool:
        return str(self) != str(0)

    def __hash__(self) -> int:
        return len(str(self))