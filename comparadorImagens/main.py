import numpy as np
import cv2


def mostrarImgs():
    cv2.imshow("Original", original)
    cv2.imshow("Duplicate", duplicate)
    cv2.waitKey(0)


# === Definindo imagens === #
original = cv2.imread("imgs/original.jpg")
duplicate = cv2.imread("imgs/triplicate.jpg")

# === Fazendo checagem se as duas imagens são iguais === #
if original.shape == duplicate.shape:
    print("As imagens possuem mesmo tamanho e canais")
    difference = cv2.subtract(original, duplicate)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("As imagens são completamente iguais")

else:
    print("As imagens não são iguais")

# === Monstrando imagens === #
print("\nDeseja visualizar as imagems?\n1. Sim\n2.Não\n")
switcher = {
    1: mostrarImgs(),
    2: print("Programa encerrado")
}
