#Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze
# suma parametrilor care reprezintă numere întregi sau reale.
def your_function(*args, **kwargs):
    sum = 0

    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
         sum += arg

    return sum

print(your_function(1,5,-3,'abc',[12,56,'cad']))
print(your_function())
print(your_function(2,4,'abc', param_1=2))

#Să se scrie o funcție care citește de la tastatură și returnează valoarea
# dacă aceasta este un număr întreg, altfel returnează valoarea 0.

def function():
    try:
     i = int(input('Scrie un numar: '))
    except ValueError:
        return 0
    else:
        return i

print(function())

# Să se scrie un modul care contine 3 funcții recursive
# care primesc ca parametru un număr întreg și returnează:
# -> modul.py

import modul

print(f'suma tuturor numerelor: {modul.suma(4)}')
print(f'suma numerelor pare: {modul.suma_par(4)}')
print(f'suma numerelor impare: {modul.suma_impar(4)}')
