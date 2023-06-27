
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

    #-------------- INICIO Y FIN DEL PROGRAMA -------------- 

    #omitimos crear un contexto al iniciar el programa 
    #porque la TablaSimbolos ya se encuentra inicializada con el mismo
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.file = open('./output/TablaDeSimbolos.txt','w')



    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.file.close()
        #recorro los contextos
        for context in self.tablaSimbolos.ts:
            #obtengo todos los items de los contextos
            for key, value in context.items():
                #si es una funcion
                if value.typeId == "function":
                    #prototipada pero no implementada
                    if value.is_declared and not value.is_initialized:
                        print(f'ERROR: la funcion "{value.name}" fue prototipada pero no creada')
                    #no usada
                    if not value.is_used:
                        if value.name != 'main':
                            print(f'WARNING: la funcion "{value.name}" no fue utilizada')

                    

    #-------------- BLOQUES -------------- 

    # añado un contexto al entrar a un bloque
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.addContext()

    # quito un contexto al entrar a un bloque
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        
        ultimoContexto = TablaSimbolos.ts[-1]
        
        for key, value in ultimoContexto.items():
            if value.typeId == "variable":
                if not value.is_used:
                    print(f'WARNING: la variable "{value.name}" no fue utilizada')
        
        self.file.write(self.tablaSimbolos.ts.__str__() + "\n")
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
        self.tablaSimbolos.addContext()


    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        
        ultimoContexto = TablaSimbolos.ts[-1]
        
        for key, value in ultimoContexto.items():
            if value.typeId == "variable":
                if not value.is_initialized:
                    print(f'WARNING: la variable "{value.name}" no fue inicializada')
                if not value.is_used:
                    print(f'WARNING: la variable "{value.name}" no fue utilizada')
        
        
        self.file.write(self.tablaSimbolos.ts.__str__() + "\n")
        #quito el contexto de parametros de funcion        
        self.tablaSimbolos.removeContext()

        if self.tablaSimbolos.returnSize() != 1:
            print(f'ERROR: Debes declarar la funcion {str(ctx.getChild(1))} en el contexto global')
        else:
            #obtengo ID
            nombreFuncion = str(ctx.getChild(1))
            #obtengo tdato
            tipoFuncion = str(ctx.getChild(0).getChild(0))
            #creo la funcion
            function = Function(nombreFuncion, tipoFuncion, self.argumentosFuncion.copy())
            #indico que la funcion fue declarada
            function.is_initialized = True
            #la agrego al ultimo contexto
            self.tablaSimbolos.ts[-1][nombreFuncion] = function
            #limpio el buffer de argumentos
            self.argumentosFuncion.clear()

 

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
        else:
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






        #-------------- RELACIONADO A BLOQUES LOGICOS -------------- 
    def enterBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        #añado el nuevo contexto de parametros del bloque for
        self.tablaSimbolos.addContext()

    def exitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        ultimoContexto = TablaSimbolos.ts[-1]
        for key, value in ultimoContexto.items():
            if value.typeId == "variable":
                if not value.is_initialized:
                    print(f'WARNING: la variable "{value.name}" no fue inicializada')
                if not value.is_used:
                    print(f'WARNING: la variable "{value.name}" no fue utilizada')
                    
        
        #quito el contexto de parametros del bloque for
        self.file.write(self.tablaSimbolos.ts.__str__() + "\n")
        self.tablaSimbolos.removeContext()


    def exitValor(self, ctx:compiladoresParser.ValorContext):
        #obtengo id, numero o TOF
        id = str(ctx.getChild(0))
        
        try:
            if id.isdigit() or float(id):
                pass
        except:
            #verifico si la variable existe
            if self.tablaSimbolos.returnKey(str(ctx.getChild(0))) != False:
                #le cambio el estado a usada
                self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_used = True
                #verifico si fue inicializada
                if self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_initialized == True:
                    pass  
                else:
                    print(f'WARNING: La variable "{str(ctx.getChild(0))}" no fue inicializada')
            elif id == 'true' or id == 'false':
                pass
            else:
                print(f'ERROR: La variable "{str(ctx.getChild(0))}" no existe')



    def exitCmp(self, ctx:compiladoresParser.CmpContext):
        #obtengo los operandos involucrados
        operando_1 = str(ctx.getChild(0))
        operando_2 = str(ctx.getChild(2))
        
        #operando_1
        try:
            #si es un numero hago un pass 
            if operando_1.isdigit() or float(operando_1):
                pass
        #puede ser id o TOF
        except:
            #verifico si la variable existe
            if self.tablaSimbolos.returnKey(str(operando_1)) != False:
                #le cambio el estado a usada
                self.tablaSimbolos.returnKey(str(operando_1)).is_used = True
                #verifico si fue inicializada
                if self.tablaSimbolos.returnKey(str(operando_1)).is_initialized == True:
                    pass  
                else:
                    print(f'WARNING: La variable "{str(operando_1)}" no fue inicializada')
            elif operando_1 == 'true' or operando_1 == 'false':
                pass
            else:
                print(f'ERROR: La variable "{str(operando_1)}" no existe')


        #operando_2
        try:
            #si es un numero hago un pass 
            if operando_2.isdigit() or float(operando_2):
                pass
        #puede ser id o TOF
        except:
            #verifico si la variable existe
            if self.tablaSimbolos.returnKey(str(operando_2)) != False:
                #le cambio el estado a usada
                self.tablaSimbolos.returnKey(str(operando_2)).is_used = True
                #verifico si fue inicializada
                if self.tablaSimbolos.returnKey(str(operando_2)).is_initialized == True:
                    pass  
                else:
                    print(f'WARNING: La variable "{str(operando_2)}" no fue inicializada')
            elif operando_2 == 'true' or operando_2 == 'false':
                pass
            else:
                print(f'ERROR: La variable "{str(operando_2)}" no existe')
        
        

           
    #-------------- INCREMENTO Y DECREMENTO UNITARIO --------------


    def exitIncrementoUnario(self, ctx:compiladoresParser.IncrementoUnarioContext):
        #verifico si la variable existe
        if self.tablaSimbolos.returnKey(str(ctx.getChild(0))) != False:
            #verifico si fue inicializada
            if self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_initialized == True:
                pass
            else:
                print(f'WARNING: La variable "{str(ctx.getChild(0))}" no fue inicializada')
        else:
            print(f'ERROR: La variable "{str(ctx.getChild(0))}" no existe')



    def exitDecrementoUnario(self, ctx:compiladoresParser.DecrementoUnarioContext):
        #verifico si la variable existe
        if self.tablaSimbolos.returnKey(str(ctx.getChild(0))) != False:
            #verifico si fue inicializada
            if self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_initialized == True:
                pass
            else:
                print(f'WARNING: La variable "{str(ctx.getChild(0))}" no fue inicializada')
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
                    #le cambio el estado a usada
                    self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_used = True
                    #verifico si fue inicializada
                    if self.tablaSimbolos.returnKey(str(ctx.getChild(0))).is_initialized == True:
                        pass  
                    else:
                        print(f'WARNING: La variable "{str(ctx.getChild(0))}" no fue inicializada')
                else:
                    print(f'ERROR: La variable "{str(ctx.getChild(0))}" no existe')



del compiladoresParser