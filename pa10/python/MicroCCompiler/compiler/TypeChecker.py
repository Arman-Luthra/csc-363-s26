from .Scope import Scope
from ..ast import *
from ..ast.visitor.AbstractASTVisitor import AbstractASTVisitor


class TypeCheckError(Exception):
  pass


class TypeChecker(AbstractASTVisitor):

  def postprocessVarNode(self, node: VarNode):
    return node.getType()

  def postprocessIntLitNode(self, node: IntLitNode):
    return Scope.Type.INT

  def postprocessFloatLitNode(self, node: FloatLitNode):
    return Scope.Type.FLOAT

  def postprocessBinaryOpNode(self, node: BinaryOpNode, left, right):
    if left != right:
      raise TypeCheckError("binary op operand types differ")
    return left

  def postprocessUnaryOpNode(self, node: UnaryOpNode, expr):
    return expr

  def postprocessAssignNode(self, node: AssignNode, left, right):
    if left != right:
      raise TypeCheckError("assignment LHS/RHS type mismatch")
    return None

  def postprocessStatementListNode(self, node: StatementListNode, statements):
    return None

  def postprocessReadNode(self, node: ReadNode, var):
    return None

  def postprocessWriteNode(self, node: WriteNode, writeExpr):
    return None

  def postprocessIfStatementNode(self, node: IfStatementNode, cond, tlist, elist):
    return None

  def postprocessWhileNode(self, node: WhileNode, cond, slist):
    return None

  def postprocessReturnNode(self, node: ReturnNode, retExpr):
    expected = node.getFuncSymbol().getReturnType()
    if retExpr != expected:
      raise TypeCheckError("return expression type does not match function return type")
    return None

  def postprocessCondNode(self, node: CondNode, left, right):
    if left != right:
      raise TypeCheckError("condition operand types differ")
    return None

  def postprocessFunctionNode(self, node: FunctionNode, body):
    return None

  def postprocessFunctionListNode(self, node: FunctionListNode, functions):
    return None

  def postprocessCallNode(self, node: CallNode, args):
    expected = node.ste.getArgTypes()
    if len(args) != len(expected):
      raise TypeCheckError(f"call to {node.getFuncName()} has wrong arg count")
    for i, (got, want) in enumerate(zip(args, expected)):
      if got != want:
        raise TypeCheckError(f"call to {node.getFuncName()} arg {i} type mismatch")
    return node.ste.getReturnType()
