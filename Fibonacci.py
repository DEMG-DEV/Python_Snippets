#!/usr/bin/env python

# Este metodo sirve para hacer la secuencia Fibonacci
def fibonacci(ant, sig, max, tot):
    if ant == sig:
        print(ant)
        print(sig)
    print(ant+sig)
    tot += 1
    if tot < max:
        fibonacci(sig, (ant+sig), max, tot)


max = int(input("Numero de veces que se genere la secuencia Fibonacci:"))
numero = 1
fibonacci(numero, numero, max, 0)
