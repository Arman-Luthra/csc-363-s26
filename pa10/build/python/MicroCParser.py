# Generated from python/MicroC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO



from typing import List

from MicroCCompiler.compiler.SymbolTable import SymbolTable
from MicroCCompiler.compiler.Scope import Scope
from MicroCCompiler.ast.IntLitNode import IntLitNode
from MicroCCompiler.ast.FloatLitNode import FloatLitNode
from MicroCCompiler.ast.AssignNode import AssignNode
from MicroCCompiler.ast.VarNode import VarNode
from MicroCCompiler.ast.WriteNode import WriteNode
from MicroCCompiler.ast.ReadNode import ReadNode
from MicroCCompiler.ast.ReturnNode import ReturnNode
from MicroCCompiler.ast.CondNode import CondNode
from MicroCCompiler.ast.CallNode import CallNode
from MicroCCompiler.ast.IfStatementNode import IfStatementNode
from MicroCCompiler.ast.WhileNode import WhileNode
from MicroCCompiler.ast.StatementListNode import StatementListNode
from MicroCCompiler.ast.ASTNode import ASTNode
from MicroCCompiler.ast.BinaryOpNode import BinaryOpNode
from MicroCCompiler.ast.UnaryOpNode import UnaryOpNode
from MicroCCompiler.ast.FunctionListNode import FunctionListNode
from MicroCCompiler.ast.FunctionNode import FunctionNode

def serializedATN():
    return [
        4,1,32,326,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,81,8,1,1,
        2,1,2,1,2,1,2,3,2,87,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,107,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,122,8,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,141,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,149,8,11,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,3,13,160,8,13,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,3,14,172,8,14,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,186,8,15,1,16,1,16,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,
        18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,3,20,231,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,3,22,260,8,22,1,23,1,23,1,23,1,23,1,
        24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,3,25,277,8,
        25,1,26,1,26,1,26,1,26,1,26,1,26,3,26,285,8,26,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,5,27,296,8,27,10,27,12,27,299,9,27,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,310,8,28,10,28,12,
        28,313,9,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,
        32,1,32,0,2,54,56,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,3,1,0,18,23,
        1,0,24,25,2,0,17,17,26,26,316,0,66,1,0,0,0,2,80,1,0,0,0,4,86,1,0,
        0,0,6,88,1,0,0,0,8,90,1,0,0,0,10,95,1,0,0,0,12,106,1,0,0,0,14,108,
        1,0,0,0,16,121,1,0,0,0,18,123,1,0,0,0,20,140,1,0,0,0,22,148,1,0,
        0,0,24,150,1,0,0,0,26,159,1,0,0,0,28,171,1,0,0,0,30,185,1,0,0,0,
        32,187,1,0,0,0,34,193,1,0,0,0,36,199,1,0,0,0,38,203,1,0,0,0,40,230,
        1,0,0,0,42,232,1,0,0,0,44,259,1,0,0,0,46,261,1,0,0,0,48,265,1,0,
        0,0,50,276,1,0,0,0,52,284,1,0,0,0,54,286,1,0,0,0,56,300,1,0,0,0,
        58,314,1,0,0,0,60,319,1,0,0,0,62,321,1,0,0,0,64,323,1,0,0,0,66,67,
        3,2,1,0,67,68,3,16,8,0,68,69,6,0,-1,0,69,1,1,0,0,0,70,71,3,8,4,0,
        71,72,3,2,1,0,72,81,1,0,0,0,73,74,3,10,5,0,74,75,3,2,1,0,75,81,1,
        0,0,0,76,77,3,14,7,0,77,78,3,2,1,0,78,81,1,0,0,0,79,81,1,0,0,0,80,
        70,1,0,0,0,80,73,1,0,0,0,80,76,1,0,0,0,80,79,1,0,0,0,81,3,1,0,0,
        0,82,83,3,8,4,0,83,84,3,4,2,0,84,87,1,0,0,0,85,87,1,0,0,0,86,82,
        1,0,0,0,86,85,1,0,0,0,87,5,1,0,0,0,88,89,5,27,0,0,89,7,1,0,0,0,90,
        91,3,12,6,0,91,92,3,6,3,0,92,93,5,1,0,0,93,94,6,4,-1,0,94,9,1,0,
        0,0,95,96,5,2,0,0,96,97,3,6,3,0,97,98,5,3,0,0,98,99,5,30,0,0,99,
        100,5,1,0,0,100,101,6,5,-1,0,101,11,1,0,0,0,102,103,5,4,0,0,103,
        107,6,6,-1,0,104,105,5,5,0,0,105,107,6,6,-1,0,106,102,1,0,0,0,106,
        104,1,0,0,0,107,13,1,0,0,0,108,109,3,12,6,0,109,110,3,6,3,0,110,
        111,5,6,0,0,111,112,3,20,10,0,112,113,5,7,0,0,113,114,5,1,0,0,114,
        115,6,7,-1,0,115,15,1,0,0,0,116,117,3,18,9,0,117,118,3,16,8,0,118,
        119,6,8,-1,0,119,122,1,0,0,0,120,122,6,8,-1,0,121,116,1,0,0,0,121,
        120,1,0,0,0,122,17,1,0,0,0,123,124,3,12,6,0,124,125,3,6,3,0,125,
        126,5,6,0,0,126,127,3,20,10,0,127,128,5,7,0,0,128,129,6,9,-1,0,129,
        130,5,8,0,0,130,131,3,4,2,0,131,132,3,26,13,0,132,133,5,9,0,0,133,
        134,6,9,-1,0,134,19,1,0,0,0,135,136,3,24,12,0,136,137,3,22,11,0,
        137,138,6,10,-1,0,138,141,1,0,0,0,139,141,6,10,-1,0,140,135,1,0,
        0,0,140,139,1,0,0,0,141,21,1,0,0,0,142,143,5,10,0,0,143,144,3,24,
        12,0,144,145,3,22,11,0,145,146,6,11,-1,0,146,149,1,0,0,0,147,149,
        6,11,-1,0,148,142,1,0,0,0,148,147,1,0,0,0,149,23,1,0,0,0,150,151,
        3,12,6,0,151,152,3,6,3,0,152,153,6,12,-1,0,153,25,1,0,0,0,154,155,
        3,28,14,0,155,156,3,26,13,0,156,157,6,13,-1,0,157,160,1,0,0,0,158,
        160,6,13,-1,0,159,154,1,0,0,0,159,158,1,0,0,0,160,27,1,0,0,0,161,
        162,3,30,15,0,162,163,5,1,0,0,163,164,6,14,-1,0,164,172,1,0,0,0,
        165,166,3,40,20,0,166,167,6,14,-1,0,167,172,1,0,0,0,168,169,3,42,
        21,0,169,170,6,14,-1,0,170,172,1,0,0,0,171,161,1,0,0,0,171,165,1,
        0,0,0,171,168,1,0,0,0,172,29,1,0,0,0,173,174,3,38,19,0,174,175,6,
        15,-1,0,175,186,1,0,0,0,176,177,3,32,16,0,177,178,6,15,-1,0,178,
        186,1,0,0,0,179,180,3,34,17,0,180,181,6,15,-1,0,181,186,1,0,0,0,
        182,183,3,36,18,0,183,184,6,15,-1,0,184,186,1,0,0,0,185,173,1,0,
        0,0,185,176,1,0,0,0,185,179,1,0,0,0,185,182,1,0,0,0,186,31,1,0,0,
        0,187,188,5,11,0,0,188,189,5,6,0,0,189,190,3,6,3,0,190,191,5,7,0,
        0,191,192,6,16,-1,0,192,33,1,0,0,0,193,194,5,12,0,0,194,195,5,6,
        0,0,195,196,3,54,27,0,196,197,5,7,0,0,197,198,6,17,-1,0,198,35,1,
        0,0,0,199,200,5,13,0,0,200,201,3,54,27,0,201,202,6,18,-1,0,202,37,
        1,0,0,0,203,204,3,6,3,0,204,205,5,3,0,0,205,206,3,54,27,0,206,207,
        6,19,-1,0,207,39,1,0,0,0,208,209,5,14,0,0,209,210,5,6,0,0,210,211,
        3,58,29,0,211,212,5,7,0,0,212,213,5,8,0,0,213,214,3,26,13,0,214,
        215,5,9,0,0,215,216,6,20,-1,0,216,231,1,0,0,0,217,218,5,14,0,0,218,
        219,5,6,0,0,219,220,3,58,29,0,220,221,5,7,0,0,221,222,5,8,0,0,222,
        223,3,26,13,0,223,224,5,9,0,0,224,225,5,15,0,0,225,226,5,8,0,0,226,
        227,3,26,13,0,227,228,5,9,0,0,228,229,6,20,-1,0,229,231,1,0,0,0,
        230,208,1,0,0,0,230,217,1,0,0,0,231,41,1,0,0,0,232,233,5,16,0,0,
        233,234,5,6,0,0,234,235,3,58,29,0,235,236,5,7,0,0,236,237,5,8,0,
        0,237,238,3,26,13,0,238,239,5,9,0,0,239,240,6,21,-1,0,240,43,1,0,
        0,0,241,242,3,6,3,0,242,243,6,22,-1,0,243,260,1,0,0,0,244,245,5,
        6,0,0,245,246,3,54,27,0,246,247,5,7,0,0,247,248,6,22,-1,0,248,260,
        1,0,0,0,249,250,3,46,23,0,250,251,6,22,-1,0,251,260,1,0,0,0,252,
        253,3,48,24,0,253,254,6,22,-1,0,254,260,1,0,0,0,255,256,5,28,0,0,
        256,260,6,22,-1,0,257,258,5,29,0,0,258,260,6,22,-1,0,259,241,1,0,
        0,0,259,244,1,0,0,0,259,249,1,0,0,0,259,252,1,0,0,0,259,255,1,0,
        0,0,259,257,1,0,0,0,260,45,1,0,0,0,261,262,5,17,0,0,262,263,3,54,
        27,0,263,264,6,23,-1,0,264,47,1,0,0,0,265,266,3,6,3,0,266,267,5,
        6,0,0,267,268,3,50,25,0,268,269,5,7,0,0,269,270,6,24,-1,0,270,49,
        1,0,0,0,271,272,3,54,27,0,272,273,3,52,26,0,273,274,6,25,-1,0,274,
        277,1,0,0,0,275,277,6,25,-1,0,276,271,1,0,0,0,276,275,1,0,0,0,277,
        51,1,0,0,0,278,279,5,10,0,0,279,280,3,54,27,0,280,281,3,52,26,0,
        281,282,6,26,-1,0,282,285,1,0,0,0,283,285,6,26,-1,0,284,278,1,0,
        0,0,284,283,1,0,0,0,285,53,1,0,0,0,286,287,6,27,-1,0,287,288,3,56,
        28,0,288,289,6,27,-1,0,289,297,1,0,0,0,290,291,10,1,0,0,291,292,
        3,64,32,0,292,293,3,56,28,0,293,294,6,27,-1,0,294,296,1,0,0,0,295,
        290,1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,
        55,1,0,0,0,299,297,1,0,0,0,300,301,6,28,-1,0,301,302,3,44,22,0,302,
        303,6,28,-1,0,303,311,1,0,0,0,304,305,10,1,0,0,305,306,3,62,31,0,
        306,307,3,44,22,0,307,308,6,28,-1,0,308,310,1,0,0,0,309,304,1,0,
        0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,57,1,0,0,
        0,313,311,1,0,0,0,314,315,3,54,27,0,315,316,3,60,30,0,316,317,3,
        54,27,0,317,318,6,29,-1,0,318,59,1,0,0,0,319,320,7,0,0,0,320,61,
        1,0,0,0,321,322,7,1,0,0,322,63,1,0,0,0,323,324,7,2,0,0,324,65,1,
        0,0,0,15,80,86,106,121,140,148,159,171,185,230,259,276,284,297,311
    ]

class MicroCParser ( Parser ):

    grammarFileName = "MicroC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'string'", "'='", "'int'", "'float'", 
                     "'('", "')'", "'{'", "'}'", "','", "'read'", "'print'", 
                     "'return'", "'if'", "'else'", "'while'", "'-'", "'<'", 
                     "'<='", "'>='", "'=='", "'!='", "'>'", "'*'", "'/'", 
                     "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_var_decls = 2
    RULE_ident = 3
    RULE_var_decl = 4
    RULE_str_decl = 5
    RULE_base_type = 6
    RULE_func_decl = 7
    RULE_functions = 8
    RULE_function = 9
    RULE_params = 10
    RULE_params_rest = 11
    RULE_param = 12
    RULE_statements = 13
    RULE_statement = 14
    RULE_base_stmt = 15
    RULE_read_stmt = 16
    RULE_print_stmt = 17
    RULE_return_stmt = 18
    RULE_assign_stmt = 19
    RULE_if_stmt = 20
    RULE_while_stmt = 21
    RULE_primary = 22
    RULE_unaryminus_expr = 23
    RULE_call_expr = 24
    RULE_arg_list = 25
    RULE_args_rest = 26
    RULE_expr = 27
    RULE_term = 28
    RULE_cond = 29
    RULE_cmpop = 30
    RULE_mulop = 31
    RULE_addop = 32

    ruleNames =  [ "program", "decls", "var_decls", "ident", "var_decl", 
                   "str_decl", "base_type", "func_decl", "functions", "function", 
                   "params", "params_rest", "param", "statements", "statement", 
                   "base_stmt", "read_stmt", "print_stmt", "return_stmt", 
                   "assign_stmt", "if_stmt", "while_stmt", "primary", "unaryminus_expr", 
                   "call_expr", "arg_list", "args_rest", "expr", "term", 
                   "cond", "cmpop", "mulop", "addop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    IDENTIFIER=27
    INT_LITERAL=28
    FLOAT_LITERAL=29
    STR_LITERAL=30
    COMMENT=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    def setSymbolTable(self, st: SymbolTable):
      self.st = st

    def getSymbolTable(self) -> SymbolTable:
      return self.st

    def setAST(self, node: ASTNode):
      self.ast = node

    def getAST(self) -> ASTNode:
      return self.ast

    def addParams(self, types: List[Scope.Type], names: List[str]):
      for i in reversed(range(len(types))):
        self.st.addArgument(types[i], names[i])




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._functions = None # FunctionsContext

        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def functions(self):
            return self.getTypedRuleContext(MicroCParser.FunctionsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MicroCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.decls()
            self.state = 67
            localctx._functions = self.functions()
            self.setAST(localctx._functions.node);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def str_decl(self):
            return self.getTypedRuleContext(MicroCParser.Str_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MicroCParser.Func_declContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = MicroCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.var_decl()
                self.state = 71
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.str_decl()
                self.state = 74
                self.decls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.func_decl()
                self.state = 77
                self.decls()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def var_decls(self):
            return self.getTypedRuleContext(MicroCParser.Var_declsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decls" ):
                listener.enterVar_decls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decls" ):
                listener.exitVar_decls(self)




    def var_decls(self):

        localctx = MicroCParser.Var_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decls)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.var_decl()
                self.state = 83
                self.var_decls()
                pass
            elif token in [9, 11, 12, 13, 14, 16, 27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MicroCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = MicroCParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(MicroCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = MicroCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            localctx._base_type = self.base_type()
            self.state = 91
            localctx._ident = self.ident()
            self.state = 92
            self.match(MicroCParser.T__0)
            self.st.addVariable(localctx._base_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ident = None # IdentContext
            self.val = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def STR_LITERAL(self):
            return self.getToken(MicroCParser.STR_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_str_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_decl" ):
                listener.enterStr_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_decl" ):
                listener.exitStr_decl(self)




    def str_decl(self):

        localctx = MicroCParser.Str_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_str_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(MicroCParser.T__1)
            self.state = 96
            localctx._ident = self.ident()
            self.state = 97
            self.match(MicroCParser.T__2)
            self.state = 98
            localctx.val = self.match(MicroCParser.STR_LITERAL)
            self.state = 99
            self.match(MicroCParser.T__0)
            self.st.addVariable(Scope.Type.STRING, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), (None if localctx.val is None else localctx.val.text));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None


        def getRuleIndex(self):
            return MicroCParser.RULE_base_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_type" ):
                listener.enterBase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_type" ):
                listener.exitBase_type(self)




    def base_type(self):

        localctx = MicroCParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_base_type)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(MicroCParser.T__3)
                localctx.t =  Scope.Type.INT
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(MicroCParser.T__4)
                localctx.t =  Scope.Type.FLOAT
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext
            self._params = None # ParamsContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def params(self):
            return self.getTypedRuleContext(MicroCParser.ParamsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)




    def func_decl(self):

        localctx = MicroCParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            localctx._base_type = self.base_type()
            self.state = 109
            localctx._ident = self.ident()
            self.state = 110
            self.match(MicroCParser.T__5)
            self.state = 111
            localctx._params = self.params()
            self.state = 112
            self.match(MicroCParser.T__6)
            self.state = 113
            self.match(MicroCParser.T__0)
            self.st.addFunction(localctx._base_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._params.types);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._function = None # FunctionContext
            self._functions = None # FunctionsContext

        def function(self):
            return self.getTypedRuleContext(MicroCParser.FunctionContext,0)


        def functions(self):
            return self.getTypedRuleContext(MicroCParser.FunctionsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = MicroCParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functions)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                localctx._function = self.function()
                self.state = 117
                localctx._functions = self.functions()
                localctx.node =  FunctionListNode(localctx._function.node, localctx._functions.node)
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                localctx.node =  FunctionListNode()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext
            self._params = None # ParamsContext
            self._statements = None # StatementsContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def params(self):
            return self.getTypedRuleContext(MicroCParser.ParamsContext,0)


        def var_decls(self):
            return self.getTypedRuleContext(MicroCParser.Var_declsContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MicroCParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            localctx._base_type = self.base_type()
            self.state = 124
            localctx._ident = self.ident()
            self.state = 125
            self.match(MicroCParser.T__5)
            self.state = 126
            localctx._params = self.params()
            self.state = 127
            self.match(MicroCParser.T__6)

            # Add FunctionSymbolTable entry to global scope
            ste = self.st.getSymbolTableEntry((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
            if ste is None or not ste.isDefined():
              self.st.addFunction(localctx._base_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._params.types);          
              ste = self.st.getSymbolTableEntry((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
              ste.setDefined(True);
            else:
              raise Exception("Function already defined");
            self.st.pushScope((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
            self.addParams(localctx._params.types, localctx._params.names);

            self.state = 129
            self.match(MicroCParser.T__7)
            self.state = 130
            self.var_decls()
            self.state = 131
            localctx._statements = self.statements()
            self.state = 132
            self.match(MicroCParser.T__8)

            # Create FunctionNode
            funcScope = self.st.currentScope();
            localctx.node =  FunctionNode(localctx._statements.node, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), funcScope)

            # Done with this scope, so pop the scope
            self.st.popScope();

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.names = None
            self.types = None
            self._param = None # ParamContext
            self._params_rest = None # Params_restContext

        def param(self):
            return self.getTypedRuleContext(MicroCParser.ParamContext,0)


        def params_rest(self):
            return self.getTypedRuleContext(MicroCParser.Params_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = MicroCParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_params)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                localctx._param = self.param()
                self.state = 136
                localctx._params_rest = self.params_rest()

                localctx.names =  []
                localctx.types =  []
                localctx.names.append(localctx._param.name);
                localctx.names.extend(localctx._params_rest.names);
                localctx.types.append(localctx._param.type_);
                localctx.types.extend(localctx._params_rest.types);

                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)

                localctx.names =  []
                localctx.types =  []

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.names = None
            self.types = None
            self._param = None # ParamContext
            self._params_rest = None # Params_restContext

        def param(self):
            return self.getTypedRuleContext(MicroCParser.ParamContext,0)


        def params_rest(self):
            return self.getTypedRuleContext(MicroCParser.Params_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_params_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_rest" ):
                listener.enterParams_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_rest" ):
                listener.exitParams_rest(self)




    def params_rest(self):

        localctx = MicroCParser.Params_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_params_rest)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(MicroCParser.T__9)
                self.state = 143
                localctx._param = self.param()
                self.state = 144
                localctx._params_rest = self.params_rest()

                localctx.names =  []
                localctx.types =  []
                localctx.names.append(localctx._param.name);
                localctx.names.extend(localctx._params_rest.names);
                localctx.types.append(localctx._param.type_);
                localctx.types.extend(localctx._params_rest.types);

                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)

                localctx.names =  []
                localctx.types =  []

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self.type_ = None
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = MicroCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            localctx._base_type = self.base_type()
            self.state = 151
            localctx._ident = self.ident()

            localctx.name =  (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))
            localctx.type_ =  localctx._base_type.t

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._statement = None # StatementContext
            self.s = None # StatementsContext

        def statement(self):
            return self.getTypedRuleContext(MicroCParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = MicroCParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statements)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 16, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                localctx._statement = self.statement()
                self.state = 155
                localctx.s = self.statements()
                localctx.node =  StatementListNode(localctx._statement.node, localctx.s.node.getStatements())
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                localctx.node =  StatementListNode()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._base_stmt = None # Base_stmtContext
            self._if_stmt = None # If_stmtContext
            self._while_stmt = None # While_stmtContext

        def base_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Base_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MicroCParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MicroCParser.While_stmtContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MicroCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                localctx._base_stmt = self.base_stmt()
                self.state = 162
                self.match(MicroCParser.T__0)
                localctx.node =  localctx._base_stmt.node
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                localctx._if_stmt = self.if_stmt()
                localctx.node =  localctx._if_stmt.node
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                localctx._while_stmt = self.while_stmt()
                localctx.node =  localctx._while_stmt.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._assign_stmt = None # Assign_stmtContext
            self._read_stmt = None # Read_stmtContext
            self._print_stmt = None # Print_stmtContext
            self._return_stmt = None # Return_stmtContext

        def assign_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Assign_stmtContext,0)


        def read_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Read_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_base_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_stmt" ):
                listener.enterBase_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_stmt" ):
                listener.exitBase_stmt(self)




    def base_stmt(self):

        localctx = MicroCParser.Base_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_base_stmt)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                localctx._assign_stmt = self.assign_stmt()
                localctx.node =  localctx._assign_stmt.node
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                localctx._read_stmt = self.read_stmt()
                localctx.node =  localctx._read_stmt.node
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                localctx._print_stmt = self.print_stmt()
                localctx.node =  localctx._print_stmt.node
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                localctx._return_stmt = self.return_stmt()
                localctx.node =  localctx._return_stmt.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_read_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_stmt" ):
                listener.enterRead_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_stmt" ):
                listener.exitRead_stmt(self)




    def read_stmt(self):

        localctx = MicroCParser.Read_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_read_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MicroCParser.T__10)
            self.state = 188
            self.match(MicroCParser.T__5)
            self.state = 189
            localctx._ident = self.ident()
            self.state = 190
            self.match(MicroCParser.T__6)
            localctx.node =  ReadNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = MicroCParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MicroCParser.T__11)
            self.state = 194
            self.match(MicroCParser.T__5)
            self.state = 195
            localctx._expr = self.expr(0)
            self.state = 196
            self.match(MicroCParser.T__6)
            localctx.node =  WriteNode(localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = MicroCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MicroCParser.T__12)
            self.state = 200
            localctx._expr = self.expr(0)
            localctx.node =  ReturnNode(localctx._expr.node, self.st.getFunctionSymbol(self.st.currentScope().getName()))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._expr = None # ExprContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = MicroCParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            localctx._ident = self.ident()
            self.state = 204
            self.match(MicroCParser.T__2)
            self.state = 205
            localctx._expr = self.expr(0)
            localctx.node =  AssignNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))), localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext
            self.ts = None # StatementsContext
            self.es = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MicroCParser.StatementsContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = MicroCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_stmt)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(MicroCParser.T__13)
                self.state = 209
                self.match(MicroCParser.T__5)
                self.state = 210
                localctx._cond = self.cond()
                self.state = 211
                self.match(MicroCParser.T__6)
                self.state = 212
                self.match(MicroCParser.T__7)
                self.state = 213
                localctx._statements = self.statements()
                self.state = 214
                self.match(MicroCParser.T__8)
                localctx.node =  IfStatementNode(localctx._cond.node, StatementListNode(None, localctx._statements.node.getStatements()), None)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(MicroCParser.T__13)
                self.state = 218
                self.match(MicroCParser.T__5)
                self.state = 219
                localctx._cond = self.cond()
                self.state = 220
                self.match(MicroCParser.T__6)
                self.state = 221
                self.match(MicroCParser.T__7)
                self.state = 222
                localctx.ts = self.statements()
                self.state = 223
                self.match(MicroCParser.T__8)
                self.state = 224
                self.match(MicroCParser.T__14)
                self.state = 225
                self.match(MicroCParser.T__7)
                self.state = 226
                localctx.es = self.statements()
                self.state = 227
                self.match(MicroCParser.T__8)
                localctx.node =  IfStatementNode(localctx._cond.node, StatementListNode(None, localctx.ts.node.getStatements()), StatementListNode(None, localctx.es.node.getStatements()))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = MicroCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MicroCParser.T__15)
            self.state = 233
            self.match(MicroCParser.T__5)
            self.state = 234
            localctx._cond = self.cond()
            self.state = 235
            self.match(MicroCParser.T__6)
            self.state = 236
            self.match(MicroCParser.T__7)
            self.state = 237
            localctx._statements = self.statements()
            self.state = 238
            self.match(MicroCParser.T__8)
            localctx.node =  WhileNode(localctx._cond.node, StatementListNode(localctx._statements.node))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._expr = None # ExprContext
            self._unaryminus_expr = None # Unaryminus_exprContext
            self._call_expr = None # Call_exprContext
            self.il = None # Token
            self.fl = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def unaryminus_expr(self):
            return self.getTypedRuleContext(MicroCParser.Unaryminus_exprContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MicroCParser.Call_exprContext,0)


        def INT_LITERAL(self):
            return self.getToken(MicroCParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MicroCParser.FLOAT_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = MicroCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primary)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                localctx._ident = self.ident()
                localctx.node =  VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(MicroCParser.T__5)
                self.state = 245
                localctx._expr = self.expr(0)
                self.state = 246
                self.match(MicroCParser.T__6)
                localctx.node =  localctx._expr.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                localctx._unaryminus_expr = self.unaryminus_expr()
                localctx.node =  localctx._unaryminus_expr.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                localctx._call_expr = self.call_expr()
                localctx.node =  localctx._call_expr.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
                localctx.il = self.match(MicroCParser.INT_LITERAL)
                localctx.node =  IntLitNode((None if localctx.il is None else localctx.il.text))
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 257
                localctx.fl = self.match(MicroCParser.FLOAT_LITERAL)
                localctx.node =  FloatLitNode((None if localctx.fl is None else localctx.fl.text))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unaryminus_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_unaryminus_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryminus_expr" ):
                listener.enterUnaryminus_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryminus_expr" ):
                listener.exitUnaryminus_expr(self)




    def unaryminus_expr(self):

        localctx = MicroCParser.Unaryminus_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryminus_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MicroCParser.T__16)
            self.state = 262
            localctx._expr = self.expr(0)
            localctx.node =  UnaryOpNode(localctx._expr.node, '-')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._arg_list = None # Arg_listContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def arg_list(self):
            return self.getTypedRuleContext(MicroCParser.Arg_listContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_call_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_expr" ):
                listener.enterCall_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_expr" ):
                listener.exitCall_expr(self)




    def call_expr(self):

        localctx = MicroCParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            localctx._ident = self.ident()
            self.state = 266
            self.match(MicroCParser.T__5)
            self.state = 267
            localctx._arg_list = self.arg_list()
            self.state = 268
            self.match(MicroCParser.T__6)
            localctx.node =  CallNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._arg_list.args)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.args = None
            self._expr = None # ExprContext
            self._args_rest = None # Args_restContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def args_rest(self):
            return self.getTypedRuleContext(MicroCParser.Args_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)




    def arg_list(self):

        localctx = MicroCParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arg_list)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 17, 27, 28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                localctx._expr = self.expr(0)
                self.state = 272
                localctx._args_rest = self.args_rest()

                localctx.args =  []
                localctx.args.append(localctx._expr.node);
                localctx.args.extend(localctx._args_rest.args);

                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                localctx.args =  []
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Args_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.args = None
            self._expr = None # ExprContext
            self._args_rest = None # Args_restContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def args_rest(self):
            return self.getTypedRuleContext(MicroCParser.Args_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_args_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs_rest" ):
                listener.enterArgs_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs_rest" ):
                listener.exitArgs_rest(self)




    def args_rest(self):

        localctx = MicroCParser.Args_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_args_rest)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(MicroCParser.T__9)
                self.state = 279
                localctx._expr = self.expr(0)
                self.state = 280
                localctx._args_rest = self.args_rest()

                localctx.args =  []
                localctx.args.append(localctx._expr.node);
                localctx.args.extend(localctx._args_rest.args);

                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                localctx.args =  []
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self._term = None # TermContext
            self._addop = None # AddopContext

        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def addop(self):
            return self.getTypedRuleContext(MicroCParser.AddopContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            localctx._term = self.term(0)
            localctx.node =  localctx._term.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 290
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 291
                    localctx._addop = self.addop()
                    self.state = 292
                    localctx._term = self.term(0)
                    localctx.node =  BinaryOpNode(localctx.e1.node, localctx._term.node, (None if localctx._addop is None else self._input.getText(localctx._addop.start,localctx._addop.stop))) 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.t1 = None # TermContext
            self._primary = None # PrimaryContext
            self._mulop = None # MulopContext

        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def mulop(self):
            return self.getTypedRuleContext(MicroCParser.MulopContext,0)


        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            localctx._primary = self.primary()
            localctx.node =  localctx._primary.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                    localctx.t1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 304
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 305
                    localctx._mulop = self.mulop()
                    self.state = 306
                    localctx._primary = self.primary()
                    localctx.node =  BinaryOpNode(localctx.t1.node, localctx._primary.node, (None if localctx._mulop is None else self._input.getText(localctx._mulop.start,localctx._mulop.stop))) 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self._cmpop = None # CmpopContext
            self.e2 = None # ExprContext

        def cmpop(self):
            return self.getTypedRuleContext(MicroCParser.CmpopContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MicroCParser.ExprContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = MicroCParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            localctx.e1 = self.expr(0)
            self.state = 315
            localctx._cmpop = self.cmpop()
            self.state = 316
            localctx.e2 = self.expr(0)
            localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, (None if localctx._cmpop is None else self._input.getText(localctx._cmpop.start,localctx._cmpop.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_cmpop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmpop" ):
                listener.enterCmpop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmpop" ):
                listener.exitCmpop(self)




    def cmpop(self):

        localctx = MicroCParser.CmpopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_cmpop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)




    def mulop(self):

        localctx = MicroCParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)




    def addop(self):

        localctx = MicroCParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            _la = self._input.LA(1)
            if not(_la==17 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.expr_sempred
        self._predicates[28] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




