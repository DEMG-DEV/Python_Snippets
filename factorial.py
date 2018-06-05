#!/usr/bin/env python

# Calculo del Factorial de un numero
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# Se pide al usuario que introduzca el numero a calcular
number = int(input("Enter a number:"))
print(fact(number))
