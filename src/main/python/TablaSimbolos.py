class TablaSimbolos:
    
    _instance = None
    
    def __new__(inst):
        if inst._instance is None:
           inst._instance = super(TablaSimbolos, inst).__new__(inst)
        return inst._instance
    
    ts = [dict()]
    
    # Crear un contexto
    def addContext(self):
        self.ts.append(dict())
    
    # Borrar el ultimo un contexto
    def removeContext(self):
        self.ts.pop()
        
    
    # Mete la variable en el ultimo contexto
    def addId(self, id):
        self.ts[-1][id.name] = id

    
    # Devolver la variable en base a una Key
    def returnKey(self,key):
        print(len(self.ts))
        for context in self.ts:
            print(context.keys())
            if key in context:
                return context[key]
        return False


    # Devuelve el tamaño del arreglo (cuantos contextos hay)
    def returnSize(self):
        return len(self.ts)
    

# Un ID debe tener un nombre y un tipo
# name -> identificador (nombre)
# type -> tipo de ID (int, float para una variable)
class Id:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.is_initialized = False
        self.is_used = False
        self.typeId = ""
        
    def toString(self):
        return f'(name->{self.name},\ntype->{self.type},\nis_initialized->{self.is_initialized},\nis_used->{self.is_used},\ntypeId->{self.typeId})\n'
    

#Variable hereda de id
class Variable(Id):
    pass


#Function hereda de ID pero deben sobreescribirse algunos datos 
class Function(Id):
    def __init__(self, name, type, parameters):
        super().__init__(name, type)
        self.parameters = parameters
        self.typeId = "function"

    def toString(self):
        return f'(name->{self.name},\ntype->{self.type},\nis_initialized->{self.is_initialized},\nis_used->{self.is_used},\nparameters->{self.parameters},\ntypeId->{self.typeId})\n'
        
