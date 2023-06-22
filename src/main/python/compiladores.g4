grammar compiladores;

/// Fragment ///
fragment LETRA: [a-zA-Z];
fragment DIGITO: [0-9];


/// Tokens ///
ENTERO: DIGITO+;

/// Palabras reservadas //
// Control
IF: 'if';
// Repeticion
WHILE: 'while';
FOR: 'for';

/// Operadores ///
PYC: ';'; //punto y coma
COMA: ','; 
LA: '{'; //llave abrir
LC: '}'; //llave cerrar
PA: '('; //parentesis abrir
PC: ')'; //parentesis cerrar
// Comparadores //
IGUAL: '=';
MENOR: '<';
MAYOR: '>';
// Operadores aritmeticos //
MAS: '+';
MENOS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
//operadores logicos
TOF: 'true' | 'false';
AND: '&&';
ORR: '||';
NOT: '!';
//operadores unarios
INC: '++'; //incremento
RED: '--'; //reduccion
	
/**** INICIO ****/
programa: lineas;
/** Jerarquia **/
lineas: instruccion lineas | | EOF; //ver comentario...
instruccion:
	bloque
	| declaracion_variables
	| asignacion PYC
	| estructuras
	| funciones
	| funciones bloque;

bloque: LA lineas LC;
estructuras: iwhile | iif | ifor;

/*funciones*/
//declaracion

funciones: funcionesDec | funcionesllam; 

funcionesDecPro: tipo_dato_func ID PA (declaracion_variables_func)* (COMA declaracion_variables_func)* PC PYC; //prototipo
funcionesDec: tipo_dato_func ID PA (declaracion_variables_func)* (COMA declaracion_variables_func)* PC; //declaro funcion por eso no el pyc


//llamado
funcionesllam: ID PA (ID|ENTERO|TOF) (COMA (ID|ENTERO|TOF))* PC
    | ID PA PC;

/*!funciones*/

/*-------------Definición de variables-------------*/
/*Tipo*/
INT: 'int';
DOUBLE: 'double';
CHAR: 'char';
BOOL: 'bool';
VOID: 'void';

tipo_dato: (INT | DOUBLE | CHAR | BOOL);
tipo_dato_func: tipo_dato | VOID;


/*ID*/
ID: (LETRA | '_') ((LETRA | DIGITO | '_'))*;

unarios: INC
	| RED
	| MENOS IGUAL ENTERO
	| MAS IGUAL ENTERO;

asignable: ID | ENTERO | expresion; //Agregar funcion
decl_var: tipo_dato asig PYC;
asig:
	ID IGUAL asignable lista_asignaciones
	| ID lista_asignaciones;
lista_asignaciones: COMA asig | IGUAL asig |;


/*Declaración*/
declaracion_variables: tipo_dato ID la PYC;
declaracion_variables_func: tipo_dato ID | tipo_dato ID la;

/*Asignaciones*/
asignacion: ID IGUAL ID 
    | ID IGUAL ENTERO 
    | ID IGUAL expresion 
    | ID unarios;

la: IGUAL ID la 
	| IGUAL ENTERO 
	| COMA ID la 
	| 
	| IGUAL (TOF) la; 

/*-------------Operadores relacionales-------------*/
/* Declaracion */
operadores_relacionales: (IGUAL IGUAL)
	| MAYOR
	| MENOR
	| (MAYOR IGUAL)
	| (MENOR IGUAL)
	| AND ID
	| ORR ID;

operadores_logicos: AND 
	| ORR
	| NOT IGUAL; //diferente

/* Comparacion */
comparacion:
	ID operadores_relacionales ENTERO
	| ID operadores_relacionales ID
	| ENTERO operadores_relacionales ENTERO
	| ENTERO operadores_relacionales ID
	| 
	|ID operadores_logicos ID
	|ID;


/** Operaciones aritmeticas **/
/* Jerarquia de terminos */
expresion:
	expresion MAS termino
	| expresion MENOS termino
	| termino;
termino:
	termino MUL factor
	| termino DIV factor
	| termino MOD factor
	| factor;
factor: PA expresion PC | ID | ENTERO;

/*-------------Estructuras-------------*/
/* If */
iif:
	IF PA comparacion PC
	| IF PA ENTERO PC
	| IF PA ID PC 
	| IF PA TOF PC
	| IF PA comparacion ((AND|ORR) comparacion)* PC;
/* While */
iwhile: WHILE PA comparacion ((AND|ORR) comparacion)* PC
        | WHILE PA TOF PC;
		//| WHILE PA comparacion (AND comparacion)* (ORR comparacion)* PC;
/* FOR */
ifor:
	FOR PA declaracion_variables comparacion ((AND|ORR) comparacion)*  PYC asignacion PC
	| FOR PA declaracion_variables comparacion ((AND|ORR) comparacion)*  PYC PC
	| FOR PA declaracion_variables PYC asignacion PC
	| FOR PA declaracion_variables PYC PC
	| FOR PA PYC comparacion ((AND|ORR) comparacion)* PYC asignacion PC 
	| FOR PA PYC comparacion ((AND|ORR) comparacion)* PYC asignacion PC 
	| FOR PA PYC comparacion ((AND|ORR) comparacion)* PYC PC
	| FOR PA PYC PYC asignacion PC
	| FOR PA PYC PYC PC; //LISTAS LAS ESTRUCTURAS OJO NO TOCAR.


/*-------------Caracteres ignorados-------------*/
WS: [ \t\n\r] -> skip;