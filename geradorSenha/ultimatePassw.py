import random
import string

senhado = None


def gerarSenha():
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(10))

    count = 0
    for elem in result_str:
        if elem.isupper():
            count += 1

    aux = sum(1 for x in result_str if x.isupper())
    print("Letras maiúsculas: ", aux)

    if aux <= 4:
        if result_str[0:1].isupper() == False:
            print("Requisito atingido")
            result_str[0:1].upper()
            auxLetra = result_str[0:1].upper()
            result_str = result_str[:0] + result_str[0 + 1:]
            result_str = auxLetra + result_str
            print(result_str)


print("Começa agora: \n")
gerarSenha()
