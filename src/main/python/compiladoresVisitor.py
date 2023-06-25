# Generated from c:\\Users\\emili\\Downloads\\Martin\\Compilador\\compiladoresDHS\\src\\main\\python\\compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#retorno.
    def visitRetorno(self, ctx:compiladoresParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#valor.
    def visitValor(self, ctx:compiladoresParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipado.
    def visitPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumentosProto.
    def visitArgumentosProto(self, ctx:compiladoresParser.ArgumentosProtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumentoProto.
    def visitArgumentoProto(self, ctx:compiladoresParser.ArgumentoProtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcion.
    def visitFuncion(self, ctx:compiladoresParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumentos.
    def visitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumento.
    def visitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametros.
    def visitParametros(self, ctx:compiladoresParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloquefor.
    def visitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueWhile.
    def visitBloqueWhile(self, ctx:compiladoresParser.BloqueWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueIf.
    def visitBloqueIf(self, ctx:compiladoresParser.BloqueIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueElse.
    def visitBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueElseIf.
    def visitBloqueElseIf(self, ctx:compiladoresParser.BloqueElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueSwitch.
    def visitBloqueSwitch(self, ctx:compiladoresParser.BloqueSwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#casos.
    def visitCasos(self, ctx:compiladoresParser.CasosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#caso.
    def visitCaso(self, ctx:compiladoresParser.CasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#control.
    def visitControl(self, ctx:compiladoresParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cmps.
    def visitCmps(self, ctx:compiladoresParser.CmpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cmp.
    def visitCmp(self, ctx:compiladoresParser.CmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#incrementoUnario.
    def visitIncrementoUnario(self, ctx:compiladoresParser.IncrementoUnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#decrementoUnario.
    def visitDecrementoUnario(self, ctx:compiladoresParser.DecrementoUnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tdato.
    def visitTdato(self, ctx:compiladoresParser.TdatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracionConjunta.
    def visitDeclaracionConjunta(self, ctx:compiladoresParser.DeclaracionConjuntaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#init.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignarFuncion.
    def visitAsignarFuncion(self, ctx:compiladoresParser.AsignarFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oparitmeticas.
    def visitOparitmeticas(self, ctx:compiladoresParser.OparitmeticasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oparitmetica.
    def visitOparitmetica(self, ctx:compiladoresParser.OparitmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expresion.
    def visitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#termino.
    def visitTermino(self, ctx:compiladoresParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#terminos.
    def visitTerminos(self, ctx:compiladoresParser.TerminosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#f.
    def visitF(self, ctx:compiladoresParser.FContext):
        return self.visitChildren(ctx)



del compiladoresParser