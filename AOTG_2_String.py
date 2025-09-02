"""
ACTIVIDAD 2 (TPO) PROGRAMACION ORIENTADA A OBJETOS
"""


#1 Pedir la Frase

print("Ingresa una frase: ")
frase = input()


#2 Usar Split para lista

lista = frase.split()
print("Lista de palabras: ", lista)


#3 Convertir a mayúsculas

lista_mayusculas = frase.upper()
print("Lista de palabras en mayúsculas: ", lista_mayusculas)


#4 Contar Cuantas veces se menciona cierta palabra

palabra_seleccionada = input("\n\nIngresa la palabra que deseas contar en la frase: ")
contador = lista_mayusculas.count(palabra_seleccionada)
print("La palabra",palabra_seleccionada," se menciona", contador,"veces en la frase.")


#5 Remplazar la palabra con otra

palabra_reemplazo = input("\n\nIngresa la palabra que deseas reemplazar: ")
nueva_palabra = input("Ingresa la nueva palabra: ")

Lista_Remplazo = lista_mayusculas.replace(palabra_reemplazo, nueva_palabra)
print("Lista de palabras después del reemplazo: ", Lista_Remplazo)


