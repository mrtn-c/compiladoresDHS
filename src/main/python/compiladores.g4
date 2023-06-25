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
FLOAT: 'float';
BOOL: 'bool';
TOF: 'true' | 'false';
 

//Estructuras de Control
IIF: 'if';
IELSE: 'else';
IELSEIF: 'else if';

//Definiciones para Switch
ISWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';
BREAK: 'break';
DP: ':';
//Estructuras de Repeticion
IWHILE: 'while';
IFOR: 'for';
/// INICIO DE FUNCION Y CONTEXTOS ///
programa: instrucciones EOF;

instrucciones: instruccion instrucciones |;

instruccion:
	bloque | declaracion PYC | asignacion PYC | incrementoUnario PYC | decrementoUnario PYC
	| bloqueIf | bloqueWhile | bloquefor | bloqueSwitch | prototipado PYC | funcion
	| llamadaFuncion PYC | asignarFuncion PYC;

bloque:
	LA instrucciones retorno PYC LC | LA instrucciones LC ;

retorno: RETORNO | RETORNO ID | RETORNO NUMERO | RETORNO oparitmetica;





NUMERO:
	DIGITO+ | '-' DIGITO+ | DIGITO+ PUNTO DIGITO+ | '-' DIGITO+ PUNTO DIGITO+;

RETORNO: 'return';

ID: (LETRA | '_') ((LETRA | DIGITO | '_'))*; 

WS: [ \t\n\r] -> skip;

valor: NUMERO | TOF | ID;


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
	IFOR PA (declaracion | asignacion | ) PYC (cmp | ) PYC (asignacion | incrementoUnario | decrementoUnario | ) PC bloque; //completo


bloqueWhile: IWHILE control bloque ;




// bloques de control
bloqueIf: IIF control bloque | IIF control bloque bloqueElse | IIF control bloque bloqueElseIf;

bloqueElse: IELSE bloque;

bloqueElseIf: IELSEIF control bloque (bloqueElse | bloqueElseIf|);



bloqueSwitch: ISWITCH PA (valor | expresion) PC LA casos LC;

casos: caso casos |;

caso: CASE valor DP instrucciones BREAK PYC
| CASE valor DP instrucciones
| DEFAULT DP instrucciones;

      


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
	tdato ID | tdato init | tdato init declaracionConjunta | tdato ID declaracionConjunta | tdato ID ASSIG valor;

tdato: INT | FLOAT | BOOL;

declaracionConjunta:
	COMA ID | COMA ID declaracionConjunta | COMA init declaracionConjunta |;

init: ID ASSIG NUMERO | ID ASSIG oparitmeticas | ID ASSIG llamadaFuncion;

asignacion: ID ASSIG NUMERO | ID ASSIG oparitmeticas;

asignarFuncion: ID ASSIG llamadaFuncion;



/// OPERACION ARITMETICA ///
oparitmeticas: oparitmetica oparitmeticas |;

oparitmetica: expresion;

expresion: termino terminos;

termino: factor f;

terminos: SUMA termino terminos | REST termino terminos |;

factor: ID | NUMERO | PA expresion PC;

f: MULT factor f | DIV factor f |;