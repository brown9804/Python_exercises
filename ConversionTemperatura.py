#Python3 

#### 			DEFINICIONES 			####

#Definicion para convertir de grado Fahrenheit a Celsius
def celsius(f):
	cgrade = (f-32)*(5/9)
	return cgrade

#Definicion para convertir de grado Celsius a Fahrenheit 
def fahren(c):
	fgrade = ((9/5)*c) +32
	return fgrade

#### 			IMPLEMENTACION 			####

fahgrado = float(input("Digite un valor en grados fahrenheit para convertirlo a celsius "))
c = celsius(fahgrado)
print (fahgrado, "equivale a ", c, " grados celsius")

celgrado = float(input("Digite grados celsius para pasarlos a fahrenheit "))
f = fahren(celgrado)
print(celgrado, "equivalen a ", f, "grados fahrenheit ")
