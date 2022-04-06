# suma tuturor numerelor de la [0, n]
def suma(n):
    if n == 0:
        return 0

    return n + suma(n - 1)

# suma numerelor pare de la [0, n]
def suma_par(n):
    if n == 1:
        return 0

    if n % 2 != 0 :
        n -= 1

    return n + suma_par(n - 1)



# suma numerelor impare de la [0. n]
def suma_impar(n):
    if n == 0:
        return 0

    if n % 2 == 0:
       n -= 1

    return n + suma_impar(n - 1)





