Algoritmo MayorDeTres
	
	Definir num1, num2, num3, mayor como Entero
	
	Escribir "Ingrese el primer n�mero: "
	Leer num1
	
	Escribir "Ingrese el segundo n�mero: "
	Leer num2
	
	Escribir "Ingrese el tercer n�mero: "
	Leer num3
	
	mayor <- num1
	
	Si num2 > mayor Entonces
		mayor <- num2
	FinSi
	
	Si num3 > mayor Entonces
		mayor <- num3
	FinSi
	
	Escribir "El n�mero mayor es: ", mayor
	
FinAlgoritmo
