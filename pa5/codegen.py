from acdcast import *
from tokens import TokenType

class InstructionList:

    def __init__(self):
        self.instructions = []

    def append(self, instruction: str):
        self.instructions.append(instruction)

    def extend(self, newinstructions: "InstructionList"):
        self.instructions.extend(newinstructions.instructions)

    def __iter__(self):
        return iter(self.instructions)


def codegenerator(program: list[ASTNode]) -> InstructionList:
    code = InstructionList()
    for statement in program:
        newcode = stmtcodegen(statement)
        code.extend(newcode)
    return code


def stmtcodegen(statement: ASTNode) -> InstructionList:
    code = InstructionList()
    if isinstance(statement, IntDclNode):
        return code
    if isinstance(statement, PrintNode):
        code.append(f"l{statement.varname}")
        code.append("p")
        return code
    if isinstance(statement, AssignNode):
        code.extend(exprcodegen(statement.expr))
        code.append(f"s{statement.varname}")
        return code
    return code


def exprcodegen(expr: ASTNode) -> InstructionList:
    code = InstructionList()
    if isinstance(expr, IntLitNode):
        code.append(str(expr.value))
        return code
    if isinstance(expr, VarRefNode):
        code.append(f"l{expr.varname}")
        return code
    if isinstance(expr, BinOpNode):
        if expr.optype == TokenType.EXPONENT and isinstance(expr.right, IntLitNode):
            n = expr.right.value
            if n < 0:
                code.extend(exprcodegen(expr.left))
                code.extend(exprcodegen(expr.right))
                code.append("^")
                return code
            if n == 0:
                code.extend(exprcodegen(expr.left))
                code.append("1")
                code.append("r")
                code.append("0")
                code.append("*")
                code.append("-")
                return code
            if n == 1:
                code.extend(exprcodegen(expr.left))
                return code
            code.extend(exprcodegen(expr.left))
            for _ in range(n - 1):
                code.append("d")
            for _ in range(n - 1):
                code.append("*")
            return code
        code.extend(exprcodegen(expr.left))
        code.extend(exprcodegen(expr.right))
        op = str(expr.optype.value)
        code.append(op)
        return code
    return code
