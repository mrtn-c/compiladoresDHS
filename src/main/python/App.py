import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from MyListener import MyListener
from MyVisitor import MyVisitor

def main(argv):
    archivo = "./input/entrada.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    
    miListener = MyListener()
    parser.addParseListener(miListener)
    
    tree = parser.programa()
    print(tree.toStringTree(recog=parser))
    myVisitor = MyVisitor()
    myVisitor.visitPrograma(tree)

if __name__ == '__main__':
    main(sys.argv)