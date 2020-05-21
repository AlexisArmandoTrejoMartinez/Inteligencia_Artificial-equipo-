# Integrantes:
# Hidalgo Hernandez Juan Daniel
# Trejo Martinez Alexis Armando

/*Persona A = comparar B = EGO*/
hermanos(A,B) :- A\==B,
	padres(A,X),
	padres(B,X).
/*Tios Sanguineos*/
tios(A,B) :- A\==B,
	padres(A,X),
	hermanos(X,B).
/*Para tios politicos*/
tios(A,B) :- A\==B,
	padres(A,X),
	hermanos(X,Y),
	padres(Z,Y),
	padres(Z,B).
/*Abuelos*/
abuelos(PA,PB):- padres(PA,X),padres(X,PB).
/*Bisabuelos*/
bisabu(A,B) :- A\==B,
	padres(A,X),
	padres(X,Y),
	padres(Y,B).
/*Tios Abuelos*/
tioabu(A,B) :- A\==B,
	padres(A,X),
	tios(X,B).
/*Tios Segundos*/
tioseg(A,B) :- A\==B,
	padres(A,X),
	tioabu(X,B).
/*Nietos*/
nietos(A,B) :- A\==B,
	padres(A,X),
	padres(X,B).
/*Bisnietos*/
bisnie(A,B) :- A\==B,
	bisabu(B,A).
/*Primos*/
primos(A,B) :- A\==B,
	padres(A,X),
	padres(B,Y),
	hermanos(X,Y).
/*Sobrinos Segundos*/
sobriseg(A,B) :- A\==B,
	nietos(A,X),
	tios(X,B).
