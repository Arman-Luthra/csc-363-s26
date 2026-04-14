from .ASTNode import ASTNode
from enum import Enum
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class CondNode(ASTNode):
  class OpType(Enum):
    EQ = 1
    NE = 2
    LT = 3
    LE = 4
    GT = 5
    GE = 6

  def getOpFromString(self, op: str):
    if op == '==':
      return CondNode.OpType.EQ
    elif op == '!=':
      return CondNode.OpType.NE
    elif op == '<':
      return CondNode.OpType.LT
    elif op == '<=':
      return CondNode.OpType.LE
    elif op == '>':
      return CondNode.OpType.GT
    elif op == '>=':
      return CondNode.OpType.GE
    else:
      raise Exception("invalid op in CondNode")

  def __init__(self, left: ASTNode, right: ASTNode, op: str):
    self.setLeft(left)
    self.setRight(right)
    self.setOp(self.getOpFromString(op))

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitCondNode(self)

  def getLeft(self) -> ASTNode:
    return self.left

  def setLeft(self, left: ASTNode):
    self.left = left

  def getRight(self) -> ASTNode:
    return self.right

  def setRight(self, right: ASTNode):
    self.right = right  

  def getOp(self) -> OpType: # just OpType?
    return self.oc

  def setOp(self, op: OpType): # just OpType?
    self.oc = op
 
  def getReversedOp(self, op: 'CondNode.OpType') -> 'CondNode.OpType':
    T = CondNode.OpType
    if op == T.LE:
      return T.GT
    if op == T.LT:
      return T.GE
    if op == T.GE:
      return T.LT
    if op == T.GT:
      return T.LE
    if op == T.EQ:
      return T.NE
    if op == T.NE:
      return T.EQ
    raise Exception("Bad op type")

