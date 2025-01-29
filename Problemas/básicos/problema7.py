#Función para convertir la entrada en lista
def Convertir(entrada_usuario):
	cadena_convertida = entrada_usuario.split()
	nueva_lista = [float(dato) for dato in cadena_convertida if dato in entrada_usuario]
	return nueva_lista
	

#Pidiendo números al usuario
while True:
	entrada_usuario = input("Introduza los números: ")
	try:
		nueva_lista = Convertir(entrada_usuario)
		break
	except:
		print("Introduzca números válidoa")
		
#Función para retornar el valor mayor de la lista
def Numero_Mayor(lista):
	for i in range(len(lista)+1):
		if len(lista) > 1:
			valor_min = min(lista)
			lista.remove(valor_min)
	return lista
	
#Mostrando resultado
print(f"El número mayor es : {Numero_Mayor(nueva_lista)[0]}")
		
		
	