from acdcast import *

class SemanticError(Exception):
    pass


def semanticanalysis(program: list[ASTNode]) -> None:
    declared: dict[str, str] = {}
    initialized: set[str] = set()

    for linenumber, statement in enumerate(program, start=1):
        _semantic_check_stmt(statement, declared, initialized, linenumber)

    return


def _semantic_check_stmt(statement: ASTNode, declared: dict[str, str], initialized: set[str], linenumber: int) -> None:

    if isinstance(statement, IntDclNode):
        varname = statement.varname
        if varname in declared:
            raise SemanticError(f"Variable {varname!r} redeclared at line {linenumber}")
        declared[varname] = "int"
        return

    if isinstance(statement, StrDclNode):
        varname = statement.varname
        if varname in declared:
            raise SemanticError(f"Variable {varname!r} redeclared at line {linenumber}")
        declared[varname] = "string"
        return

    if isinstance(statement, PrintNode):
        varname = statement.varname
        if varname not in declared:
            raise SemanticError(f"Trying to print undeclared variable {varname!r} at line {linenumber}")
        if varname not in initialized:
            raise SemanticError(f"Trying to print uninitialized variable {varname!r} at line {linenumber}")
        return

    if isinstance(statement, AssignNode):
        varname = statement.varname
        if varname not in declared:
            raise SemanticError(f"Assignment to undeclared variable {varname!r} at line {linenumber}")
        rhs_type = _semantic_check_expr(statement.expr, declared, initialized, linenumber)
        if rhs_type != declared[varname]:
            raise SemanticError(
                f"Type mismatch in assignment to {varname!r} at line {linenumber}: "
                f"expected {declared[varname]}, got {rhs_type}"
            )
        initialized.add(varname)
        return

    raise SemanticError(f"Unknown statement type at line {linenumber}")


def _semantic_check_expr(expr: ASTNode, declared: dict[str, str], initialized: set[str], linenumber: int) -> str:
    if isinstance(expr, IntLitNode):
        return "int"

    if isinstance(expr, StrLitNode):
        return "string"

    if isinstance(expr, VarRefNode):
        varname = expr.varname
        if varname not in declared:
            raise SemanticError(f"Use of undeclared variable {varname!r} at line {linenumber}")
        if varname not in initialized:
            raise SemanticError(f"Use of unitialized variable {varname!r} at line {linenumber}")
        return declared[varname]

    if isinstance(expr, BinOpNode):
        left_type = _semantic_check_expr(expr.left, declared, initialized, linenumber)
        right_type = _semantic_check_expr(expr.right, declared, initialized, linenumber)
        if left_type != "int" or right_type != "int":
            raise SemanticError(f"Operator {expr.optype} requires int operands at line {linenumber}")
        return "int"

    raise SemanticError(f"Unknown expression type at line {linenumber}")
