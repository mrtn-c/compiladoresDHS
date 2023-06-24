import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from MyListener import compiladoresListener

def main(argv):
    archivo = "../../../input/entrada.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    
    miListener = compiladoresListener()
    parser.addParseListener(miListener)
    
    tree = parser.s()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)