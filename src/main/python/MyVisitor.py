# Generated from /home/valen/dhs-2023/compiladoresDHS/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class MyVisitor(ParseTreeVisitor):

    jump_from_function_call = ""
    hay_return = False
    asignacion = False
    tmp = 0
    rollback = False


    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.file = open("./output/CodigoIntermedio.txt", "w")
        #Apenas empieza se dirije directo al main.
        self.file.write("goto MAIN \n")
        #Tengo arbol completo, visito hijos...
        self.visitChildren(ctx)
        print("salio del programa.")
        #cierro archivo.
        self.file.close()


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
        #Return solo.
        if ctx.getChildCount == 1:
            self.file.write("return\n") 
        #Operacion aritmetica
        elif(ctx.getChild(1).getChildCount() > 0):
            self.visitChildren(ctx)
            self.file.write("return t"  + str(self.tmp) + "\n" + "\n")
            self.tmp=0 
        #ID / NUMERO
        elif(ctx.getChild(1).getChildCount() == 0):
            if(self.tmp != 0):
                self.file.write("return t"  + str(self.tmp) + "\n" + "\n")
                self.tmp=0
            else:
                self.file.write("return "  + str(ctx.getChild(1)) + "\n" + "\n")
        



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
        nombreFuncion = str(ctx.getChild(1)).upper()
        self.file.write(f'\nLBL {nombreFuncion} \n')
        return self.visitChildren(ctx)



    # Visit a parse tree produced by compiladoresParser#argumento.
    def visitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        self.file.write(f'POP {str(ctx.getChild(1))} \n')
        return self.visitChildren(ctx)
    


    # Visit a parse tree produced by compiladoresParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        self.file.write("CALL " +str(ctx.getChild(0)))
        self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametros.
    def visitParametros(self, ctx:compiladoresParser.ParametrosContext):
        self.file.write(", " + str(ctx.getChild(0))) #siempre termina en un numero, ToF o ID.
        self.visitChildren(ctx)
        self.file.write("\n")
    


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




    #-------------- DECLARACION e INICIALIZACION DE VARIABLES --------------

    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        
        # si hay mas de 2 hijos es porque hay valor, oparitmetica o llamada a funcion
        if(ctx.getChildCount() > 2):
            self.asignacion = True
            self.rollback = False
                 
            # llamada a funcion
            if(ctx.getChild(3).getChildCount() > 2):
                self.file.write(str(ctx.getChild(1))+" = ")
                self.visitChildren(ctx)
            # Operacion aritmetica    
            elif(ctx.getChild(3).getChildCount() == 2):
                self.visitChildren(ctx)
                self.file.write(str(ctx.getChild(1))+" = "+ "t"+str(self.tmp)+"\n")
                self.tmp = 0
            #Valor
            elif(ctx.getChild(3).getChildCount() == 1):
                self.file.write(str(ctx.getChild(1))+" = "+str(ctx.getChild(3).getChild(0))+"\n")
        


    # Visit a parse tree produced by compiladoresParser#tdato.
    def visitTdato(self, ctx:compiladoresParser.TdatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#init.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        
        self.asignacion = True
              
        self.rollback = False
        
        #Operacion aritmetica o llamada a funcion
        
         # llamada a funcion
        if(ctx.getChild(2).getChildCount() > 2):
            self.file.write(str(ctx.getChild(0))+" = ")
            self.visitChildren(ctx)
        # Operacion aritmetica    
        elif(ctx.getChild(2).getChildCount() == 2):
            self.visitChildren(ctx)
            self.file.write(str(ctx.getChild(0))+" = "+ "t"+str(self.tmp)+"\n")
            self.tmp = 0
        elif(ctx.getChild(2).getChildCount() == 1):
            self.file.write(str(ctx.getChild(0))+" = "+str(ctx.getChild(2).getChild(0))+"\n")

        


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)





    #-------------- OPERACIONES ARITMETICAS --------------

    # Visit a parse tree produced by compiladoresParser#oparitmeticas.
    def visitOparitmeticas(self, ctx:compiladoresParser.OparitmeticasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oparitmetica.
    def visitOparitmetica(self, ctx:compiladoresParser.OparitmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expresion.
    def visitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        self.visitChildren(ctx)
        
        if(ctx.getChildCount()):
            self.file.write("t" + str(self.tmp) + "=" + ctx.getChild(0).getText() + "\n")
        self.rollback = True
        self.tmp = 0
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#termino.
    def visitTermino(self, ctx:compiladoresParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#terminos.
    def visitTerminos(self, ctx:compiladoresParser.TerminosContext):
        self.visitChildren(ctx)
        
        if ctx.getChildCount() and not self.rollback:
            self.file.write("t" + str(self.tmp) + "=" + ctx.getChild(1).getText() + "\n")
            self.tmp = self.tmp + 1
            
        elif self.rollback and ctx.getChildCount():
            self.file.write("t" + str(self.tmp + 1) + "=" + "t" + str(self.tmp + 1))
            self.file.write(ctx.getChild(0).getText() + "t" + str(self.tmp) + "\n")
            self.tmp = self.tmp + 1


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#f.
    def visitF(self, ctx:compiladoresParser.FContext):
        return self.visitChildren(ctx)



del compiladoresParser