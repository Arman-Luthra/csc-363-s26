import sys
import os

from .CodeObject import CodeObject
from .InstructionList import InstructionList
from .instructions import *
from ..compiler import *
from ..ast import *
from ..ast.visitor.AbstractASTVisitor import AbstractASTVisitor

class CodeGenerator(AbstractASTVisitor):

  def __init__(self):
    self.intRegCount = 1
    self.floatRegCount = 1
    self.intTempPrefix = 't'
    self.floatTempPrefix = 'f'

  def getIntRegCount(self):
    return self.intRegCount

  def getFloatRegCount(self):
    return self.floatRegCount




  def postprocessVarNode(self, node: VarNode) -> CodeObject:
    sym = node.getSymbol()

    co = CodeObject(sym)
    co.lval = True
    co.type = node.getType()

    return co


  
  def postprocessIntLitNode(self, node: IntLitNode) -> CodeObject:

    co = CodeObject()

    temp = self.generateTemp(Scope.Type.INT)
    val = node.getVal()
    # LI t2, 5
    co.code.append(Li(temp, val))
    co.temp = temp
    co.lval = False
    co.type = node.getType()


    return co


  def postprocessFloatLitNode(self, node: FloatLitNode) -> CodeObject:
    co = CodeObject()
    temp = self.generateTemp(Scope.Type.FLOAT)
    co.code.append(FImm(temp, node.getVal()))
    co.temp = temp
    co.lval = False
    co.type = node.getType()
    return co



  def postprocessBinaryOpNode(self, node: BinaryOpNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()
    if left.lval:
      left = self.rvalify(left)
    co.code.extend(left.code)
    if right.lval:
      right = self.rvalify(right)
    co.code.extend(right.code)
    dest = self.generateTemp(node.getType())
    op = node.getOp()
    if node.getType() == Scope.Type.INT:
      if op == BinaryOpNode.OpType.ADD:
        co.code.append(Add(left.temp, right.temp, dest))
      elif op == BinaryOpNode.OpType.SUB:
        co.code.append(Sub(left.temp, right.temp, dest))
      elif op == BinaryOpNode.OpType.MUL:
        co.code.append(Mul(left.temp, right.temp, dest))
      elif op == BinaryOpNode.OpType.DIV:
        co.code.append(Div(left.temp, right.temp, dest))
      else:
        raise Exception("Invalid int binary op")
    elif node.getType() == Scope.Type.FLOAT:
      if op == BinaryOpNode.OpType.ADD:
        co.code.append(FAdd(left.temp, right.temp, dest))
      elif op == BinaryOpNode.OpType.SUB:
        co.code.append(FSub(left.temp, right.temp, dest))
      elif op == BinaryOpNode.OpType.MUL:
        co.code.append(FMul(left.temp, right.temp, dest))
      elif op == BinaryOpNode.OpType.DIV:
        co.code.append(FDiv(left.temp, right.temp, dest))
      else:
        raise Exception("Invalid float binary op")
    else:
      raise Exception("Invalid type for binary op")
    co.temp = dest
    co.lval = False
    co.type = node.getType()
    return co



  def postprocessUnaryOpNode(self, node: UnaryOpNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    if expr.lval:
      expr = self.rvalify(expr)

    co.code.extend(expr.code)

    if expr.type == Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(Neg(src=expr.temp, dest=temp))
      

    elif expr.type == Scope.Type.FLOAT:
      temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(FNeg(src=expr.temp, dest=temp))

    else:
      raise Exception("Non int/float type in unary op!")

    co.type = expr.type
    co.temp = temp
    co.lval = False 

    return co
  






  def postprocessAssignNode(self, node: AssignNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()
    assert left.lval
    addr_temp = self.generateTemp(Scope.Type.INT)
    co.code.append(La(addr_temp, self.generateAddrFromVariable(left)))
    if right.lval:
      right = self.rvalify(right)
    co.code.extend(right.code)
    if left.type == Scope.Type.INT:
      co.code.append(Sw(right.temp, addr_temp, '0'))
    elif left.type == Scope.Type.FLOAT:
      co.code.append(Fsw(right.temp, addr_temp, '0'))
    else:
      raise Exception("Bad type in assign")
    return co



  def postprocessStatementListNode(self, node: StatementListNode, statements: list) -> CodeObject:
    co = CodeObject()

    for subcode in statements:
      co.code.extend(subcode.code)

    co.type = None
    return co


	
  def postprocessReadNode(self, node: ReadNode, var: CodeObject) -> CodeObject:

    co = CodeObject()

    assert(var.isVar())

    if var.type is Scope.Type.INT:
      address = self.generateAddrFromVariable(var)
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp2, address))
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(GetI(temp))
      co.code.append(Sw(temp, temp2, '0'))

    elif var.type is Scope.Type.FLOAT:
      address = self.generateAddrFromVariable(var)
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp2, address))
      temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(GetF(temp))
      co.code.append(Fsw(temp, temp2, '0'))

    else:
      raise Exception("Bad type in read node")


    return co


  def postprocessWriteNode(self, node: WriteNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    if expr.type == Scope.Type.STRING:
      assert expr.lval
      addr_temp = self.generateTemp(Scope.Type.INT)
      co.code.append(La(addr_temp, self.generateAddrFromVariable(expr)))
      co.code.append(PutS(addr_temp))
      return co
    if expr.lval:
      expr = self.rvalify(expr)
    co.code.extend(expr.code)
    if expr.type == Scope.Type.INT:
      co.code.append(PutI(expr.temp))
    elif expr.type == Scope.Type.FLOAT:
      co.code.append(PutF(expr.temp))
    else:
      raise Exception("Bad type in write")
    return co

  
  def postprocessReturnNode(self, node: ReturnNode, retExpr: CodeObject) -> CodeObject:

    co = CodeObject()

    if retExpr.lval is True:
      retExpr = self.rvalify(retExpr)

    co.code.extend(retExpr.code)
    co.code.append(Halt())
    co.type = None
    return co


  
  def generateTemp(self, t: Scope.Type) -> str:

    if t == Scope.Type.INT:
      s = self.intTempPrefix + str(self.intRegCount)
      self.intRegCount += 1
      return s
    elif t == Scope.Type.FLOAT:
      s = self.floatTempPrefix + str(self.floatRegCount)
      self.floatRegCount += 1
      return s
    else:
      raise Exception("Generating temp for bad type")



  def rvalify(self, lco : CodeObject) -> CodeObject:

    assert(lco.lval is True)
    assert(lco.isVar() is True)
    
    co = CodeObject()

    address = self.generateAddrFromVariable(lco)
    temp1 = self.generateTemp(Scope.Type.INT) # Addresses are always ints
    co.code.append(La(temp1, address)) # Load address (global only)

    if lco.type is Scope.Type.INT:
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(Lw(temp2, temp1, '0'))

    elif lco.type is Scope.Type.FLOAT:
      temp2 = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(Flw(temp2, temp1, '0'))

    else:
      raise Exception("Bad type in rvalify!")

    co.type = lco.type
    co.lval = False
    co.temp = temp2


    return co






  def generateAddrFromVariable(self, lco: CodeObject) -> str:
    assert(lco.isVar() is True)

    symbol = lco.getSTE()   # Get symbol from symbol table
    address = str(symbol.getAddress()) # Get address of variable

    return address
    