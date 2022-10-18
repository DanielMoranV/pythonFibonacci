# Forma Iterativa
def fbc(n):
    a = -1
    b = 1
    for k in range(n+1):
        c = a + b
        a = b
        b = c
    return b


# Forma Recursiva
# fn = fn-1 + fn-2
def fbc_r(n):
    if n < 2:
        return n
    return fbc_r(n - 1) + fbc_r(n - 2)


# Imprimir
n_fbc = int(input("Ingrese el total de series de Sucesión de Fibonacci: \n"))
print("\033[36m Forma Iterativa: \033[39m")
for x in range(n_fbc):
    print(fbc(x))

print("\033[36m Forma Recursiva: \033[39m")
for x in range(n_fbc):
    print(fbc_r(x))
