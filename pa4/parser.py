from tokens import Token, TokenType
from tokenstream import *
from acdcast import *

class ParseError(Exception):
    pass


def expect(ts: TokenStream, expectedtype: TokenType) -> Token:
    tok = ts.peek()
    if tok.tokentype != expectedtype:
        raise ParseError(f"expected {expectedtype} but found {tok.tokentype}")
    return ts.read()


def parse(ts: TokenStream) -> ASTNode:
    t = ts.peek()

    if t.tokentype == TokenType.PRINT:
        ts.read()
        if t.name is None:
            raise ParseError("malformed PRINT token")
        node = PrintNode(t.name)
        expect(ts, TokenType.EOF)
        return node

    if t.tokentype == TokenType.INTDEC:
        ts.read()
        if t.name is None:
            raise ParseError("malformed INTDEC token")
        node = IntDclNode(t.name)
        expect(ts, TokenType.EOF)
        return node

    if t.tokentype == TokenType.VARREF:
        lhs = ts.read()
        expect(ts, TokenType.ASSIGN)
        rhs = parse_expression(ts)
        if lhs.lexeme is None:
            raise ParseError("malformed VARREF token on LHS")
        node = AssignNode(lhs.lexeme, rhs)
        expect(ts, TokenType.EOF)
        return node

    raise ParseError(
        f"expected TokenType.PRINT, TokenType.INTDCL/INTDEC, or TokenType.VARREF; got {t.tokentype}"
    )


def parse_expression(ts: TokenStream) -> ASTNode:
    opstack = []
    valstack = []
    lparen_depths = []

    precedence = {
        TokenType.EXPONENT: 3,
        TokenType.TIMES: 2,
        TokenType.DIVIDE: 2,
        TokenType.PLUS: 1,
        TokenType.MINUS: 1,
    }

    leftassoc = {
        TokenType.EXPONENT: False,
        TokenType.TIMES: True,
        TokenType.DIVIDE: True,
        TokenType.PLUS: True,
        TokenType.MINUS: True,
    }

    operatortypes = {
        TokenType.PLUS,
        TokenType.MINUS,
        TokenType.TIMES,
        TokenType.DIVIDE,
        TokenType.EXPONENT,
    }

    while ts.peek().tokentype != TokenType.EOF:
        tok = ts.peek()

        if tok.tokentype == TokenType.INTLIT:
            tok = ts.read()
            if tok.intvalue is None:
                raise ParseError("malformed INTLIT token")
            next = ts.peek()
            if (next.tokentype in operatortypes) or (next.tokentype == TokenType.RPAREN) or (next.tokentype == TokenType.EOF):
                valstack.append(IntLitNode(tok.intvalue))
                continue
            raise ParseError("expected operator or rparen after int literal")

        if tok.tokentype == TokenType.VARREF:
            tok = ts.read()
            name = tok.lexeme if tok.lexeme else ""
            valstack.append(VarRefNode(name))
            next = ts.peek()
            if (next.tokentype in operatortypes) or (next.tokentype == TokenType.RPAREN) or (next.tokentype == TokenType.EOF):
                continue
            raise ParseError("expected operator or rparen after variable reference")

        if tok.tokentype == TokenType.LPAREN:
            ts.read()
            opstack.append(TokenType.LPAREN)
            lparen_depths.append(len(valstack))
            continue

        if tok.tokentype == TokenType.RPAREN:
            ts.read()
            reduced = False
            while True:
                if len(opstack) == 0:
                    raise ParseError("mismatched parentheses")
                if opstack[-1] == TokenType.LPAREN:
                    opstack.pop()
                    lparen_depths.pop()
                    if not reduced:
                        raise ParseError("expected lparen, intlit, or varref after lparen")
                    break
                reduce(opstack, valstack)
                reduced = True
            continue

        if tok.tokentype in operatortypes:
            incoming = ts.read()
            if len(valstack) == 0:
                raise ParseError(f"expected two operands for operator {incoming.tokentype}")
            if len(opstack) > 0 and opstack[-1] == TokenType.LPAREN:
                if len(lparen_depths) > 0 and len(valstack) == lparen_depths[-1]:
                    raise ParseError("expected lparen, intlit, or varref after lparen")

            while len(opstack) > 0 and opstack[-1] in operatortypes:
                top = opstack[-1]
                top_prec = precedence[top]
                inc_prec = precedence[incoming.tokentype]
                if top_prec > inc_prec:
                    reduce(opstack, valstack)
                elif top_prec == inc_prec and leftassoc[top]:
                    reduce(opstack, valstack)
                else:
                    break

            opstack.append(incoming.tokentype)
            continue

        raise ParseError(f"unexpected token in expression: {tok}")

    while len(opstack) > 0:
        if opstack[-1] == TokenType.LPAREN:
            raise ParseError("mismatched parentheses")
        reduce(opstack, valstack)

    if len(valstack) != 1:
        raise ParseError("expression did not reduce to one AST")

    return valstack.pop()


def reduce(opstack: list, valstack: list) -> None:
    if len(opstack) < 1:
        raise ParseError("mismatched parentheses")
    if len(valstack) < 2:
        if len(valstack) == 0:
            raise ParseError(f"expected two operands for operator {opstack[-1]}")
        raise ParseError("expected operand or lparen after operator")
    op = opstack.pop()
    right = valstack.pop()
    left = valstack.pop()
    valstack.append(BinOpNode(op, left, right))
