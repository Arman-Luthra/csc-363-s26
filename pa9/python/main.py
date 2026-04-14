import os
import sys

_v = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor")
if os.path.isdir(_v):
    sys.path.insert(0, _v)

import MicroCCompiler.compiler.Compiler

MicroCCompiler.compiler.Compiler.main(sys.argv[1])
