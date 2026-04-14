from .CodeObject import CodeObject
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
    assert var.isVar()
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

  def _emitFloatPredicate(self, co: CodeObject, fa: str, fb: str, branch_op: CondNode.OpType) -> None:
    it = self.generateTemp(Scope.Type.INT)
    T = CondNode.OpType
    if branch_op == T.EQ:
      co.code.append(Feq(fa, fb, it))
      co.float_branch_nonzero = True
    elif branch_op == T.NE:
      co.code.append(Feq(fa, fb, it))
      co.float_branch_nonzero = False
    elif branch_op == T.LT:
      co.code.append(Flt(fa, fb, it))
      co.float_branch_nonzero = True
    elif branch_op == T.LE:
      co.code.append(Fle(fa, fb, it))
      co.float_branch_nonzero = True
    elif branch_op == T.GT:
      co.code.append(Flt(fb, fa, it))
      co.float_branch_nonzero = True
    elif branch_op == T.GE:
      co.code.append(Fle(fb, fa, it))
      co.float_branch_nonzero = True
    else:
      raise Exception("bad float branch op")
    co.temp = it
    co.temp2 = None

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
    if left.type == Scope.Type.INT:
      co.cond_is_float = False
      co.temp = left.temp
      co.temp2 = right.temp
    elif left.type == Scope.Type.FLOAT:
      co.cond_is_float = True
      self._emitFloatPredicate(co, left.temp, right.temp, branch_op)
    else:
      raise Exception("bad cond type")
    return co

  def _appendBranchForCond(self, co: CodeObject, cond: CodeObject, label: str) -> None:
    if cond.cond_is_float:
      if cond.float_branch_nonzero:
        co.code.append(Bne(cond.temp, 'x0', label))
      else:
        co.code.append(Beq(cond.temp, 'x0', label))
      return
    op = cond.cmptype
    a = cond.temp
    b = cond.temp2
    T = CondNode.OpType
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
    co.code.append(Halt())
    co.type = None
    return co

  def generateTemp(self, t: Scope.Type) -> str:
    if t == Scope.Type.INT:
      s = self.intTempPrefix + str(self.intRegCount)
      self.intRegCount += 1
      return s
    if t == Scope.Type.FLOAT:
      s = self.floatTempPrefix + str(self.floatRegCount)
      self.floatRegCount += 1
      return s
    raise Exception("Generating temp for bad type")

  def rvalify(self, lco: CodeObject) -> CodeObject:
    assert lco.lval
    assert lco.isVar()
    co = CodeObject()
    address = self.generateAddrFromVariable(lco)
    temp1 = self.generateTemp(Scope.Type.INT)
    co.code.append(La(temp1, address))
    if lco.type is Scope.Type.INT:
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(Lw(temp2, temp1, '0'))
    elif lco.type is Scope.Type.FLOAT:
      temp2 = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(Flw(temp2, temp1, '0'))
    else:
      raise Exception("Bad type in rvalify")
    co.type = lco.type
    co.lval = False
    co.temp = temp2
    return co

  def generateAddrFromVariable(self, lco: CodeObject) -> str:
    assert lco.isVar()
    symbol = lco.getSTE()
    return str(symbol.getAddress())
