def encontrar_primo(limite_superior):
    for i in range(2,limite_superior):
        es_primo = True
        for ii in range(2,i-1):
            if i%ii == 0:
                es_primo = False
                break
        if es_primo == True:
            print(i)

encontrar_primo(int(input("dame el limite superior: ")))