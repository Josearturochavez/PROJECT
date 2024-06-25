def fib_hasta(num_terminos):
    terminos = []
    for i in range(num_terminos):
        if i == 0:
            terminos.append(0)
        elif i == 1:
            terminos.append(1)
        else:
            terminos.append(terminos[-1]+terminos[-2])
    if num_terminos > 2:
        raz_aur = terminos[-1] / terminos[-2]
    else:
        raz_aur = "insuficientes datos"
    return terminos,raz_aur

terminos,razon = fib_hasta(int(input("cuantos terminos de la suseccion de fib deseas?: ")))

print(f"los terminos son: {terminos} y la razon aurea encontrada es de: {razon}")
