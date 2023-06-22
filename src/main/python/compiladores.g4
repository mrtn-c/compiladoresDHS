grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];

// Operadores //
PA: '(';
PC: ')';
LA: '{';
LC: '}';
PYC: ';';
COMA: ',';
ASSIG: '=';

PUNTO: '.';

//operadores aritmeticos
SUMA: '+';
MULT: '*';
REST: '-';
DIV: '/';


//operadores de asignacion unitarios
INCREMENTO: '++';
DECREMENTO: '--';



//operadores de comparacion
MENOR: '<';
MAYOR: '>';
IGUALDAD: '==';
DISTINTO: '!=';
MAYORIGUAL: '>=';
MENORIGUAL: '<=';

//operadores logicos
AND: '&&';
OR: '||';

//tipos datos
INT: 'int';
DOUBLE: 'double';
FLOAT: 'float';
BOOL: 'bool';
TOF: 'true' | 'false';


//Estructuras de Control
IIF: 'if';
IELSE: 'else';
//Estructuras de Repeticion
IWHILE: 'while';
IFOR: 'for';




/// INICIO DE FUNCION Y CONTEXTOS ///
programa: instrucciones EOF;

instrucciones: instruccion instrucciones |;

instruccion:
	bloque | declaracion PYC | asignacion PYC | incrementoUnario PYC | decrementoUnario PYC
	| bloqueif | bloquewhile | bloquefor | prototipado PYC | funcion
	| llamadaFuncion PYC | asignarFuncion PYC;

bloque:
	LA instrucciones LC | LA instrucciones retorno PYC LC;

retorno: RETORNO | RETORNO ID | RETORNO NUMERO | RETORNO oparitmetica;





NUMERO:
	DIGITO+ | '-' DIGITO+ | DIGITO+ PUNTO DIGITO+ | '-' DIGITO+ PUNTO DIGITO+;

RETORNO: 'return';

ID: (LETRA | '_') ((LETRA | DIGITO | '_'))*; 

WS: [ \t\n\r] -> skip;




/// FUNCIONES ///

//prototipado de funciones
prototipado: tdato ID PA (argumentosProto |) PC;

argumentosProto:
	argumentoProto
	| argumentoProto COMA argumentosProto
	|;

argumentoProto: tdato ID;


//declaracion de funciones
funcion: tdato ID PA (argumentos |) PC bloque;

argumentos: argumento | argumento COMA argumentos |;

argumento: tdato ID;



// llamada a funcion
llamadaFuncion: ID PA (parametros |) PC | ID PA PC;

parametros:
	ID | ID COMA parametros | NUMERO COMA parametros | NUMERO | TOF | TOF COMA parametros;



/// BLOQUES ///
// bloques de repeticion
bloquefor:
	IFOR PA (declaracion | asignacion) PYC cmp PYC (asignacion | incrementoUnario | decrementoUnario) PC bloque //completo
	| IFOR PA PYC PYC PYC PC //infinito
	| IFOR PA (declaracion | asignacion) PYC PYC (asignacion | incrementoUnario | decrementoUnario) PC bloque //for(x;;x++)
	| IFOR PA (declaracion | asignacion) PYC cmp PYC PC bloque //for(x;x=5;)
	| IFOR PA (declaracion | asignacion) PYC PYC PC bloque //for(x;;)
	| IFOR PA PYC cmp PYC (asignacion | incrementoUnario | decrementoUnario) PC bloque //sin asignacion/declaracion
	| IFOR PA PYC PYC (asignacion | incrementoUnario | decrementoUnario) PC bloque; //for(;;x++)

bloquewhile: IWHILE control bloque  ;


// bloques de control
bloqueif: IIF control bloque | IIF control bloque bloqueElse;

bloqueElse: IELSE bloque;



//COMPARACIONES
control: PA cmps PC;

cmps: cmp | cmp AND cmps | cmp OR cmps;

cmp:
	//ID cmp NUMERO
	ID MAYOR NUMERO | ID MENOR NUMERO | ID IGUALDAD NUMERO 
	| ID DISTINTO NUMERO | ID MAYORIGUAL NUMERO | ID MENORIGUAL NUMERO 
	//ID cmp ID
	| ID MAYOR ID | ID MENOR ID | ID IGUALDAD ID 
	| ID DISTINTO ID | ID MAYORIGUAL ID | ID MENORIGUAL ID 
	//NUMERO cmp ID
	| NUMERO MAYOR ID | NUMERO MENOR ID | NUMERO IGUALDAD ID 
	| NUMERO DISTINTO ID | NUMERO MAYORIGUAL ID | NUMERO MENORIGUAL ID 
	//NUMERO cmp NUMERO
	| NUMERO MAYOR NUMERO | NUMERO MENOR NUMERO | NUMERO IGUALDAD NUMERO 
	| NUMERO DISTINTO NUMERO | NUMERO MAYORIGUAL NUMERO | NUMERO MENORIGUAL NUMERO
	//bool
	| ID IGUALDAD TOF | ID DISTINTO TOF | TOF DISTINTO ID | TOF IGUALDAD ID 
	| TOF IGUALDAD TOF | TOF DISTINTO TOF ;

incrementoUnario: ID INCREMENTO;

decrementoUnario: ID DECREMENTO;



//VARIABLES
declaracion:
	tdato ID | tdato init | tdato init declaracionConjunta | tdato ID declaracionConjunta;

tdato: INT | FLOAT | DOUBLE | BOOL;

declaracionConjunta:
	COMA ID | COMA ID declaracionConjunta | COMA init declaracionConjunta |;

init: ID ASSIG NUMERO | ID ASSIG oparitmeticas | ID ASSIG llamadaFuncion;

asignacion: ID ASSIG NUMERO | ID ASSIG oparitmeticas;

asignarFuncion: ID ASSIG llamadaFuncion;



/// OPERACION ARITMETICA ///
oparitmeticas: oparitmetica oparitmeticas |; //potencialmente infinita

oparitmetica: expresion;

expresion: termino terminos;

termino: factor f;

terminos: SUMA termino terminos | REST termino terminos |;

factor: ID | NUMERO | PA expresion PC;

f: MULT factor f | DIV factor f |;