import sys
import os
from typing import List

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
    self.loopLabel = 0
    self.elseLabel = 0
    self.outLabel = 0
    self.currFunc = None

  def getIntRegCount(self):
    return self.intRegCount

  def getFloatRegCount(self):
    return self.floatRegCount

  def _nextLoopLabel(self) -> str:
    self.loopLabel += 1
    return "loop_" + str(self.loopLabel)

  def _nextElseLabel(self) -> str:
    self.elseLabel += 1
    return "else_" + str(self.elseLabel)

  def _nextOutLabel(self) -> str:
    self.outLabel += 1
    return "out_" + str(self.outLabel)

  def postprocessVarNode(self, node: VarNode) -> CodeObject:
    sym = node.getSymbol()
    co = CodeObject(sym)
    co.lval = True
    co.type = node.getType()
    return co

  def postprocessIntLitNode(self, node: IntLitNode) -> CodeObject:
    co = CodeObject()
    temp = self.generateTemp(Scope.Type.INT)
    co.code.append(Li(temp, node.getVal()))
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
      raise Exception("Non int/float type in unary op")
    co.type = expr.type
    co.temp = temp
    co.lval = False
    return co

  def postprocessAssignNode(self, node: AssignNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()
    assert left.lval
    if right.lval:
      right = self.rvalify(right)
    if left.getSTE().isLocal():
      co.code.extend(right.code)
      offset = left.getSTE().addressToString()
      if left.type == Scope.Type.INT:
        co.code.append(Sw(right.temp, 'fp', offset))
      elif left.type == Scope.Type.FLOAT:
        co.code.append(Fsw(right.temp, 'fp', offset))
      else:
        raise Exception("Bad type in assign")
    else:
      addr_temp = self.generateTemp(Scope.Type.INT)
      co.code.append(La(addr_temp, self.generateAddrFromVariable(left)))
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
    assert var.isVar()
    if var.type is Scope.Type.INT:
      val_temp = self.generateTemp(Scope.Type.INT)
      co.code.append(GetI(val_temp))
      if var.getSTE().isLocal():
        offset = var.getSTE().addressToString()
        co.code.append(Sw(val_temp, 'fp', offset))
      else:
        addr_temp = self.generateTemp(Scope.Type.INT)
        co.code.append(La(addr_temp, self.generateAddrFromVariable(var)))
        co.code.append(Sw(val_temp, addr_temp, '0'))
    elif var.type is Scope.Type.FLOAT:
      val_temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(GetF(val_temp))
      if var.getSTE().isLocal():
        offset = var.getSTE().addressToString()
        co.code.append(Fsw(val_temp, 'fp', offset))
      else:
        addr_temp = self.generateTemp(Scope.Type.INT)
        co.code.append(La(addr_temp, self.generateAddrFromVariable(var)))
        co.code.append(Fsw(val_temp, addr_temp, '0'))
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

  def postprocessCondNode(self, node: CondNode, left: CodeObject, right: CodeObject) -> CodeObject:
    branch_op = node.getReversedOp(node.getOp())
    co = CodeObject()
    if left.lval:
      left = self.rvalify(left)
    if right.lval:
      right = self.rvalify(right)
    co.lval = False
    co.code.extend(left.code)
    co.code.extend(right.code)
    co.cmptype = branch_op
    if left.type != right.type:
      raise Exception("Incompatible types in condition")
    co.temp = left.temp
    co.temp2 = right.temp
    co.cond_is_float = (left.type == Scope.Type.FLOAT)
    if left.type != Scope.Type.INT and left.type != Scope.Type.FLOAT:
      raise Exception("bad cond type")
    return co

  def _appendBranchForCond(self, co: CodeObject, cond: CodeObject, label: str) -> None:
    T = CondNode.OpType
    if cond.cond_is_float:
      it = self.generateTemp(Scope.Type.INT)
      op = cond.cmptype
      nonzero = True
      if op == T.EQ:
        co.code.append(Feq(cond.temp, cond.temp2, it))
      elif op == T.NE:
        co.code.append(Feq(cond.temp, cond.temp2, it))
        nonzero = False
      elif op == T.LT:
        co.code.append(Flt(cond.temp, cond.temp2, it))
      elif op == T.LE:
        co.code.append(Fle(cond.temp, cond.temp2, it))
      elif op == T.GT:
        co.code.append(Flt(cond.temp2, cond.temp, it))
      elif op == T.GE:
        co.code.append(Fle(cond.temp2, cond.temp, it))
      else:
        raise Exception("bad float branch op")
      if nonzero:
        co.code.append(Bne(it, 'x0', label))
      else:
        co.code.append(Beq(it, 'x0', label))
      return
    op = cond.cmptype
    a = cond.temp
    b = cond.temp2
    if op == T.EQ:
      co.code.append(Beq(a, b, label))
    elif op == T.NE:
      co.code.append(Bne(a, b, label))
    elif op == T.LT:
      co.code.append(Blt(a, b, label))
    elif op == T.LE:
      co.code.append(Ble(a, b, label))
    elif op == T.GT:
      co.code.append(Bgt(a, b, label))
    elif op == T.GE:
      co.code.append(Bge(a, b, label))
    else:
      raise Exception("bad int branch op")

  def postprocessIfStatementNode(self, node: IfStatementNode, cond: CodeObject, tlist: CodeObject, elist: CodeObject) -> CodeObject:
    co = CodeObject()
    if elist is None:
      out_l = self._nextOutLabel()
      co.code.extend(cond.code)
      self._appendBranchForCond(co, cond, out_l)
      co.code.extend(tlist.code)
      co.code.append(Label(out_l))
    else:
      else_l = self._nextElseLabel()
      out_l = self._nextOutLabel()
      co.code.extend(cond.code)
      self._appendBranchForCond(co, cond, else_l)
      co.code.extend(tlist.code)
      co.code.append(J(out_l))
      co.code.append(Label(else_l))
      co.code.extend(elist.code)
      co.code.append(Label(out_l))
    return co

  def postprocessWhileNode(self, node: WhileNode, cond: CodeObject, wlist: CodeObject) -> CodeObject:
    co = CodeObject()
    loop_l = self._nextLoopLabel()
    out_l = self._nextOutLabel()
    co.code.append(Label(loop_l))
    co.code.extend(cond.code)
    self._appendBranchForCond(co, cond, out_l)
    co.code.extend(wlist.code)
    co.code.append(J(loop_l))
    co.code.append(Label(out_l))
    return co

  def postprocessReturnNode(self, node: ReturnNode, retExpr: CodeObject) -> CodeObject:
    co = CodeObject()
    if retExpr.lval:
      retExpr = self.rvalify(retExpr)
    co.code.extend(retExpr.code)
    retType = node.getFuncSymbol().getReturnType()
    if retType == Scope.Type.INT:
      co.code.append(Sw(retExpr.temp, 'fp', '8'))
    elif retType == Scope.Type.FLOAT:
      co.code.append(Fsw(retExpr.temp, 'fp', '8'))
    else:
      raise Exception("Bad return type")
    co.code.append(J(self._generateFunctionRetLabel()))
    co.type = None
    return co

  def preprocessFunctionNode(self, node: FunctionNode):
    self.currFunc = node.getFuncName()
    self.intRegCount = 1
    self.floatRegCount = 1

  def postprocessFunctionNode(self, node: FunctionNode, body: CodeObject) -> CodeObject:
    co = CodeObject()

    numLocals = node.getScope().getNumLocals()
    numIntTemps = self.intRegCount - 1
    numFloatTemps = self.floatRegCount - 1

    co.code.append(Label(self._generateFunctionEntryLabel()))
    co.code.append(Sw('fp', 'sp', '0'))
    co.code.append(Mv('sp', 'fp'))
    co.code.append(Addi('sp', '-4', 'sp'))
    co.code.append(Addi('sp', str(-4 * numLocals), 'sp'))

    for i in range(1, numIntTemps + 1):
      co.code.append(Sw(self.intTempPrefix + str(i), 'sp', '0'))
      co.code.append(Addi('sp', '-4', 'sp'))
    for i in range(1, numFloatTemps + 1):
      co.code.append(Fsw(self.floatTempPrefix + str(i), 'sp', '0'))
      co.code.append(Addi('sp', '-4', 'sp'))

    co.code.extend(body.code)

    co.code.append(Label(self._generateFunctionRetLabel()))

    for i in range(numFloatTemps, 0, -1):
      co.code.append(Addi('sp', '4', 'sp'))
      co.code.append(Flw(self.floatTempPrefix + str(i), 'sp', '0'))
    for i in range(numIntTemps, 0, -1):
      co.code.append(Addi('sp', '4', 'sp'))
      co.code.append(Lw(self.intTempPrefix + str(i), 'sp', '0'))

    co.code.append(Mv('fp', 'sp'))
    co.code.append(Lw('fp', 'fp', '0'))
    co.code.append(Ret())

    return co

  def postprocessFunctionListNode(self, node: FunctionListNode, functions: List[CodeObject]) -> CodeObject:
    co = CodeObject()

    co.code.append(Mv("sp", "fp"))
    co.code.append(Jr(self._generateFunctionEntryLabel("main")))
    co.code.append(Halt())
    co.code.append(Blank())

    for c in functions:
      co.code.extend(c.code)
      co.code.append(Blank())

    return co

  def postprocessCallNode(self, node: CallNode, args: List[CodeObject]) -> CodeObject:
    co = CodeObject()
    numArgs = len(args)

    for arg in args:
      if arg.lval:
        arg = self.rvalify(arg)
      co.code.extend(arg.code)
      if arg.type == Scope.Type.INT:
        co.code.append(Sw(arg.temp, 'sp', '0'))
      elif arg.type == Scope.Type.FLOAT:
        co.code.append(Fsw(arg.temp, 'sp', '0'))
      else:
        raise Exception("Bad arg type in call")
      co.code.append(Addi('sp', '-4', 'sp'))

    co.code.append(Addi('sp', '-4', 'sp'))

    co.code.append(Sw('ra', 'sp', '0'))
    co.code.append(Addi('sp', '-4', 'sp'))

    co.code.append(Jr(self._generateFunctionEntryLabel(node.getFuncName())))

    co.code.append(Addi('sp', '4', 'sp'))
    co.code.append(Lw('ra', 'sp', '0'))

    retType = node.ste.getReturnType()
    retTemp = self.generateTemp(retType)
    co.code.append(Addi('sp', '4', 'sp'))
    if retType == Scope.Type.INT:
      co.code.append(Lw(retTemp, 'sp', '0'))
    elif retType == Scope.Type.FLOAT:
      co.code.append(Flw(retTemp, 'sp', '0'))
    else:
      raise Exception("Bad return type in call")

    if numArgs > 0:
      co.code.append(Addi('sp', str(4 * numArgs), 'sp'))

    co.temp = retTemp
    co.lval = False
    co.type = retType
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

  def rvalify(self, lco: CodeObject) -> CodeObject:
    assert lco.lval
    assert lco.isVar()
    co = CodeObject()
    if lco.getSTE().isLocal():
      offset = lco.getSTE().addressToString()
      if lco.type is Scope.Type.INT:
        temp = self.generateTemp(Scope.Type.INT)
        co.code.append(Lw(temp, 'fp', offset))
      elif lco.type is Scope.Type.FLOAT:
        temp = self.generateTemp(Scope.Type.FLOAT)
        co.code.append(Flw(temp, 'fp', offset))
      else:
        raise Exception("Bad type in rvalify")
      co.type = lco.type
      co.lval = False
      co.temp = temp
      return co
    address = self.generateAddrFromVariable(lco)
    addr_temp = self.generateTemp(Scope.Type.INT)
    co.code.append(La(addr_temp, address))
    if lco.type is Scope.Type.INT:
      val_temp = self.generateTemp(Scope.Type.INT)
      co.code.append(Lw(val_temp, addr_temp, '0'))
    elif lco.type is Scope.Type.FLOAT:
      val_temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(Flw(val_temp, addr_temp, '0'))
    else:
      raise Exception("Bad type in rvalify")
    co.type = lco.type
    co.lval = False
    co.temp = val_temp
    return co

  def generateAddrFromVariable(self, lco: CodeObject) -> str:
    assert lco.isVar()
    symbol = lco.getSTE()
    return symbol.addressToString()

  def _generateFunctionEntryLabel(self, func=None) -> str:
    if func is None:
      return "func_" + self.currFunc
    return "func_" + func

  def _generateFunctionRetLabel(self, func=None) -> str:
    if func is None:
      return "func_ret_" + self.currFunc
    return "func_ret_" + func
