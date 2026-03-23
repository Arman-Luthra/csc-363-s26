from enum import Enum

class TokenType(Enum):
    PRINT = 0
    INTDEC = 1
    INTLIT = 2
    VARREF = 3
    ASSIGN = 4
    STRDEC = 5
    STRLIT = 6
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIVIDE = '/'
    EXPONENT = '^'
    LPAREN = 10
    RPAREN = 11
    EOF = 12
    EOTS = 13



class Token:

    def __init__(
        self, 
        tokentype: TokenType, 
        lexeme: str,
        *,  
        name: str | None = None,
        intvalue: int | None = None,
        strvalue: str | None = None,
    ):

        self.tokentype = tokentype
        self.lexeme = lexeme
        self.name = name
        self.intvalue = intvalue
        self.strvalue = strvalue

    def __str__(self):
        namepart = f"; name: {self.name}" if self.name is not None else ""
        intvalpart = f"; intval: {str(self.intvalue)}" if self.intvalue is not None else ""
        strvalpart = f"; strval: {self.strvalue!r}" if self.strvalue is not None else ""

        return f"[Token type: {self.tokentype}; lexeme: {self.lexeme}{namepart}{intvalpart}{strvalpart}]"

    def __repr__(self):
        return self.__str__()
    
