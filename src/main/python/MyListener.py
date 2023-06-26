
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
        self.tablaSimbolos.addContext()

    # quito un contexto al entrar a un bloque
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
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
     
     
    #-------------- DECLARACION DE FUNCIONES --------------  

    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        #añado el nuevo contexto de parametros de la funcion
        self.tablaSimbolos.addContext()


    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        #obtengo ID
        nombreFuncion = str(ctx.getChild(1))
        #obtengo tdato
        tipoFuncion = str(ctx.getChild(0).getChild(0))
        #creo la funcion
        function = Function(nombreFuncion, tipoFuncion, self.argumentosFuncion.copy())
        #indico que la funcion fue declarada
        function.is_initialized = True
        #la agrego al ultimo contexto
        self.tablaSimbolos.ts[-2][nombreFuncion] = function
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
        #le pongo el estado de inicializada
        argumento.is_initialized = True
        #la agrego al contexto de parametros de funcion
        self.tablaSimbolos.ts[-1][nombreVariable] = argumento
        #la agrego a la lista de argumentos
        self.argumentosFuncion.append(argumento)


    #-------------- LLAMADA A FUNCIONES -------------- 
    
    def exitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        
        #busco la funcion en la tabla simbolos en base al ID
        function = self.tablaSimbolos.returnKey(str(ctx.getChild(0)))

        if(not function):
            print(f'ERROR: la funcion {str(ctx.getChild(0))} no ha sido prototipada ni declarada previamente')
         
        self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_used = True    
            


    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        tmp = ctx.getText()
        tmp = tmp.split(",")
        
        try:
            if tmp[0].isdigit() or float(tmp[0]):
                return
        except Exception as e:
            pass
        
        try:
            if (str(tmp[0]) == 'true') or (str(tmp[0]) == 'false'):
                return
        except Exception as e:
            pass


        if self.tablaSimbolos.returnKey(str(tmp[0])) is not False:
            self.tablaSimbolos.returnKey(str(tmp[0])).is_used = True   
              
            if not self.tablaSimbolos.returnKey(str(tmp[0])).is_initialized:
                print(f'WARNING: La variable "{str(tmp[0])}" no esta inicializada')
                
        else:
            print(f'ERROR: La variable "{str(tmp[0])}" no existe')






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




    def exitIncrementoUnario(self, ctx:compiladoresParser.IncrementoUnarioContext):
        #verifico si la variable existe
        if self.tablaSimbolos.returnKey(str(ctx.getChild(0))) != False:
            #verifico si fue inicializada
            if self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_initialized == True:
                pass
            else:
                print(f'ERROR: La variable "{str(ctx.getChild(0))}" no fue inicializada')
        else:
            print(f'ERROR: La variable "{str(ctx.getChild(0))}" no existe')



    def exitDecrementoUnario(self, ctx:compiladoresParser.DecrementoUnarioContext):
        #verifico si la variable existe
        if self.tablaSimbolos.returnKey(str(ctx.getChild(0))) != False:
            #verifico si fue inicializada
            if self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_initialized == True:
                pass
            else:
                print(f'ERROR: La variable "{str(ctx.getChild(0))}" no fue inicializada')
        else:
            print(f'ERROR: La variable "{str(ctx.getChild(0))}" no existe')


    #-------------- DECLARACION e INICIALIZACION DE VARIABLES -------------- 

    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        #obtengo ID
        nombreVariable = str(ctx.getChild(1))
        #obtengo tdato
        tipoVariable = str(ctx.getChild(0).getChild(0))

        #genero objeto variable
        variable = Variable(nombreVariable,tipoVariable)

        #verifico si fue inicializada
        if (ctx.getChildCount() == 4):
            #marco la variable como inicializada
            variable.is_initialized = True

        self.tablaSimbolos.ts[-1][nombreVariable] = variable
        
        

    def exitInit(self, ctx:compiladoresParser.InitContext):
        #verifico si la variable existe
        if self.tablaSimbolos.returnKey(str(ctx.getChild(0))) != False:
            #le cambio el estado a usada
            self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_initialized = True
        else:
            print(f'ERROR: La variable "{str(ctx.getChild(0))}" no existe')





    #-------------- OPERACIONES ARITMETICAS -------------- 
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        
        #caso de id o numero
        if(ctx.getChildCount()==1):
            
            #obtengo id o numero
            id = str(ctx.getChild(0))
            
            try:
                id.isdigit() or float(id)
                return
            except:
                #verifico si la variable existe
                if self.tablaSimbolos.returnKey(str(ctx.getChild(0))) != False:
                    #verifico si fue inicializada
                    if self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_initialized == True:
                        #le cambio el estado a usada
                        self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_used = True
                    else:
                        print(f'ERROR: La variable "{str(ctx.getChild(0))}" no fue inicializada')
                else:
                    print(f'ERROR: La variable "{str(ctx.getChild(0))}" no existe')



del compiladoresParser