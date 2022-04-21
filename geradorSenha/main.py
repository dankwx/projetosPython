"""import random
import string

# ============= gerador de senhas fortes mas codado de um jeito mais trabalhoso ============= #


# import random
# import string
#
# def get_random_string(length):
# With combination of lower and upper case
#   result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
# print random string
#   print(result_str)

# string of length 8
# get_random_string(8)
# get_random_string(8)

nome = None
stringT = "A"

# Com letras maiúsculas e minúsculas
result_str = ''.join(random.choice(string.ascii_letters) for i in range(10))
# printar a random
print(result_str)

count = 0
for elem in result_str:
    if elem.isupper():
        count += 1

# quantidade de letras maiúsuclas na senha
# print(count)
# print("\nA palavra é maiúscula?", stringT.isupper())

# print("*******\nInício do programa")
# if result_str[0:1] != "A":
#    print("tete")

# Calcular letras maiúsculas na senha
# print("Capital Letters: ", sum(1 for x in result_str if x.isupper()))

aux = sum(1 for x in result_str if x.isupper())
print("Letras maiúsculas: ", aux)

# começando verificações de substituição de letras maiúsculas


if aux <= 4:
    if result_str[0:1].isupper() == False:
        print("Requisito atingido")
        result_str[0:1].upper()
        auxLetra = result_str[0:1].upper()
        result_str = result_str[:0] + result_str[0 + 1:]
        result_str = auxLetra + result_str
        print(result_str)"""
