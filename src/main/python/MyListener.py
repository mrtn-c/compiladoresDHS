
from antlr4 import *
from TablaSimbolos import TablaSimbolos
from TablaSimbolos import Function 
from TablaSimbolos import Variable

if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser


class MyListener(ParseTreeListener):
    
    tablaSimbolos = TablaSimbolos()

    argumentosFuncion = []
    
    parametrosFuncion = []

    #omitimos crear un contexto al iniciar el programa 
    #porque la TablaSimbolos ya se encuentra inicializada con el mismo


    #-------------- BLOQUES -------------- 

    # añado un contexto al entrar a un bloque
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        print("entro desde bloque")
        self.tablaSimbolos.addContext()

    # quito un contexto al entrar a un bloque
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        print("salida desde bloque")
        self.tablaSimbolos.removeContext()


    #-------------- PROTITIPADO DE FUNCIONES -------------- 

    def exitPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        #obtengo ID
        nombreFuncion = str(ctx.getChild(1))
        #obtengo tdato
        tipoFuncion = str(ctx.getChild(0).getChild(0))
        #creo la funcion
        function = Function(nombreFuncion, tipoFuncion, self.argumentosFuncion.copy())
        #la agrego al ultimo contexto
        self.tablaSimbolos.ts[-1][nombreFuncion] = function
        #limpio el buffer de argumentos
        self.argumentosFuncion.clear()
        

    def exitArgumentoProto(self, ctx:compiladoresParser.ArgumentoProtoContext):
        #obtengo ID
        nombreVariable = str(ctx.getChild(1))
        #obtengo tdato
        tipoVariable = str(ctx.getChild(0).getChild(0))
        #creo la variable argumento
        argumento = Variable(nombreVariable,tipoVariable)
        #la agrego a la lista de argumentos
        self.argumentosFuncion.append(argumento)
     
     
    #-------------- CREACION DE FUNCIONES --------------  
        
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        #añado el nuevo contexto de parametros de la funcion
        print("desde que entro a funcion")
        self.tablaSimbolos.addContext()


    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        #obtengo ID
        nombreFuncion = str(ctx.getChild(1))
        #obtengo tdato
        tipoFuncion = str(ctx.getChild(0).getChild(0))
        #creo la funcion
        function = Function(nombreFuncion, tipoFuncion, self.argumentosFuncion.copy())
        #la agrego al ultimo contexto
        self.tablaSimbolos.ts[-1][nombreFuncion] = function
        #limpio el buffer de argumentos
        self.argumentosFuncion.clear()
        #quito el contexto de parametros de funcion        
        self.tablaSimbolos.removeContext()
        # verifico que la funcion fue declarada en el contexto global
        if self.tablaSimbolos.returnSize() != 1:
            print(f'ERROR: Debes declarar la funcion {str(ctx.getChild(1))} en el contexto global')

    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        #obtengo ID
        nombreVariable = str(ctx.getChild(1))
        #obtengo tdato
        tipoVariable = str(ctx.getChild(0).getChild(0))
        #creo la variable argumento
        argumento = Variable(nombreVariable,tipoVariable)
        #la agrego a la lista de argumentos
        self.argumentosFuncion.append(argumento)


    #-------------- LLAMADA A FUNCIONES -------------- 
    
    def exitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        #busco la funcion en la tabla simbolos en base al ID
        function = self.tablaSimbolos.returnKey(str(ctx.getChild(0)))

        if(not function):
            print(f'ERROR: la funcion {str(ctx.getChild(0))} no ha sido prototipada ni declarada previamente')
            


    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass
        #tmp = ctx.getText()
        #tmp = tmp.split(",")
        #print(tmp)
        #
        #try:
        #    if tmp[0].isdigit() or float(tmp[0]) or (tmp[0] == 'true') or (tmp[0] == 'false'):
        #        return
        #except:
        #    pass
        #
        #if self.tablaSimbolos.returnKey(str(tmp[0])) is not False:
        #    self.tablaSimbolos.returnKey(str(tmp[0])).used = True   
        #      
        #    if not self.tablaSimbolos.returnKey(str(tmp[0])).initialized:
        #        print(f'WARNING: La variable "{str(tmp[0])}" no esta inicializada')
        #        
        #else:
        #    print(f'ERROR: La variable "{str(tmp[0])}" no existe')






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


    #-------------- DECLARACION DE VARIABLES -------------- 

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass
        # #obtengo ID
        # nombreVariable = str(ctx.getChild(1))
        # #obtengo tdato
        # tipoVariable = str(ctx.getChild(0).getChild(0))
        
        # if(ctx.getChildCount() == 2):
        #     #creo la variable
        #     variable = Variable(nombreVariable,tipoVariable)
            
        # elif (ctx.getChildCount() == 4):
        #     valor = str(ctx.getChild(3))
        #     print(valor)
        
        

    
    
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