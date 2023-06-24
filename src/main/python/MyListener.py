
from antlr4 import *
from TablaSimbolos import TablaSimbolos
from TablaSimbolos import Funcion 
from TablaSimbolos import Variable

if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser


class MyListener(ParseTreeListener):
    
    tablaSimbolos = TablaSimbolos()

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#retorno.
    def enterRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#retorno.
    def exitRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#valor.
    def enterValor(self, ctx:compiladoresParser.ValorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#valor.
    def exitValor(self, ctx:compiladoresParser.ValorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#prototipado.
    def enterPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipado.
    def exitPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumentosProto.
    def enterArgumentosProto(self, ctx:compiladoresParser.ArgumentosProtoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumentosProto.
    def exitArgumentosProto(self, ctx:compiladoresParser.ArgumentosProtoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumentoProto.
    def enterArgumentoProto(self, ctx:compiladoresParser.ArgumentoProtoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumentoProto.
    def exitArgumentoProto(self, ctx:compiladoresParser.ArgumentoProtoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#funcion.
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#funcion.
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumentos.
    def enterArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumentos.
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumento.
    def enterArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumento.
    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#parametros.
    def enterParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parametros.
    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloquefor.
    def enterBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloquefor.
    def exitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloqueWhile.
    def enterBloqueWhile(self, ctx:compiladoresParser.BloqueWhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueWhile.
    def exitBloqueWhile(self, ctx:compiladoresParser.BloqueWhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloqueIf.
    def enterBloqueIf(self, ctx:compiladoresParser.BloqueIfContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueIf.
    def exitBloqueIf(self, ctx:compiladoresParser.BloqueIfContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloqueElse.
    def enterBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueElse.
    def exitBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloqueElseIf.
    def enterBloqueElseIf(self, ctx:compiladoresParser.BloqueElseIfContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueElseIf.
    def exitBloqueElseIf(self, ctx:compiladoresParser.BloqueElseIfContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloqueSwitch.
    def enterBloqueSwitch(self, ctx:compiladoresParser.BloqueSwitchContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueSwitch.
    def exitBloqueSwitch(self, ctx:compiladoresParser.BloqueSwitchContext):
        pass


    # Enter a parse tree produced by compiladoresParser#casos.
    def enterCasos(self, ctx:compiladoresParser.CasosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#casos.
    def exitCasos(self, ctx:compiladoresParser.CasosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#caso.
    def enterCaso(self, ctx:compiladoresParser.CasoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#caso.
    def exitCaso(self, ctx:compiladoresParser.CasoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#control.
    def enterControl(self, ctx:compiladoresParser.ControlContext):
        pass

    # Exit a parse tree produced by compiladoresParser#control.
    def exitControl(self, ctx:compiladoresParser.ControlContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cmps.
    def enterCmps(self, ctx:compiladoresParser.CmpsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cmps.
    def exitCmps(self, ctx:compiladoresParser.CmpsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cmp.
    def enterCmp(self, ctx:compiladoresParser.CmpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cmp.
    def exitCmp(self, ctx:compiladoresParser.CmpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#incrementoUnario.
    def enterIncrementoUnario(self, ctx:compiladoresParser.IncrementoUnarioContext):
        pass

    # Exit a parse tree produced by compiladoresParser#incrementoUnario.
    def exitIncrementoUnario(self, ctx:compiladoresParser.IncrementoUnarioContext):
        pass


    # Enter a parse tree produced by compiladoresParser#decrementoUnario.
    def enterDecrementoUnario(self, ctx:compiladoresParser.DecrementoUnarioContext):
        pass

    # Exit a parse tree produced by compiladoresParser#decrementoUnario.
    def exitDecrementoUnario(self, ctx:compiladoresParser.DecrementoUnarioContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tdato.
    def enterTdato(self, ctx:compiladoresParser.TdatoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tdato.
    def exitTdato(self, ctx:compiladoresParser.TdatoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracionConjunta.
    def enterDeclaracionConjunta(self, ctx:compiladoresParser.DeclaracionConjuntaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracionConjunta.
    def exitDeclaracionConjunta(self, ctx:compiladoresParser.DeclaracionConjuntaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignarFuncion.
    def enterAsignarFuncion(self, ctx:compiladoresParser.AsignarFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignarFuncion.
    def exitAsignarFuncion(self, ctx:compiladoresParser.AsignarFuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#oparitmeticas.
    def enterOparitmeticas(self, ctx:compiladoresParser.OparitmeticasContext):
        pass

    # Exit a parse tree produced by compiladoresParser#oparitmeticas.
    def exitOparitmeticas(self, ctx:compiladoresParser.OparitmeticasContext):
        pass


    # Enter a parse tree produced by compiladoresParser#oparitmetica.
    def enterOparitmetica(self, ctx:compiladoresParser.OparitmeticaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#oparitmetica.
    def exitOparitmetica(self, ctx:compiladoresParser.OparitmeticaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expresion.
    def enterExpresion(self, ctx:compiladoresParser.ExpresionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expresion.
    def exitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#termino.
    def enterTermino(self, ctx:compiladoresParser.TerminoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#termino.
    def exitTermino(self, ctx:compiladoresParser.TerminoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#terminos.
    def enterTerminos(self, ctx:compiladoresParser.TerminosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#terminos.
    def exitTerminos(self, ctx:compiladoresParser.TerminosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#f.
    def enterF(self, ctx:compiladoresParser.FContext):
        pass

    # Exit a parse tree produced by compiladoresParser#f.
    def exitF(self, ctx:compiladoresParser.FContext):
        pass



del compiladoresParser