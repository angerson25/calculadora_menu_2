# Calculadora con menu

from math import log

print("----------------------")
print("---CALCULADORA-MENU---")
print("----------------------")

#INPUT
bandera = False
x = float(input("Digite el valor de x: "))
y = float(input("Digite el valor de y: "))

print("\n Dame la opcion que deseas realizar: \n")
# Se despliega el menu que desea realizar
print("1. Sumar (El primero mas el segundo)")
print("2. Restar (El primero menos el segundo)")
print("3. Multiplicar (El primero por el segundo)")
print("4. Dividir (El primero sobre el segundo)")
print("5. Potencia (El primero a la potencia del segundo)")
print("6. Logaritmo (El logaritmo del primero)")

opcion = int(input("\nDame la opción: "))