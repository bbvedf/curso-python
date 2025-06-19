###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

print("Hola, me llamo pepe\ny vivo en Madrid")
print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"a = {a} -> {type(a)}")
print(f"b = {b} -> {type(b)}")
print(f"c = {c} -> {type(c)}")
print(f"d = {d} -> {type(d)}")
print(f"e = {e} -> {type(e)}")


print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

print("Cadena a entero:", int("12345"))
print("Cadena a float:", float("12345"))
print("Float a entero:", int(3.99))  # Esto truncará el decimal, no redondeará
print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

nombre = "pepe"
edad = 39
altura = 1.70
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")
print("--------------")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

import math
pi = math.pi
print(f"El número PI es: {pi}")
pi_redondeado = round(pi)
print(f"El número PI redondeado es: {pi_redondeado}")
division_entera = pi_redondeado // 2
print(f"La división entera de {pi_redondeado} entre 2 es: {division_entera}")
print("--------------")


resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)