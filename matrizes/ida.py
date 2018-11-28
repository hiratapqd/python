import math
import numpy as np
crip=[]
text = input("Frase a ser criptografada   ")


for i in range (len(text)):
#relacao entre letras e valores
    genders = {
        "a": 1,
        "b": 2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "o":15,
        "p":16,
        "q":17,
        "r":18,
        "s":19,
        "t":20,
        "u":21,
        "v":22,
        "w":23,
        "x":24,
        "y":25,
        "z":26,
        ".":27,
        ",":28,
        "_":29,
        " ":30
    }

    crip.append(genders.get(text[i]))
    i+=1
#como estamos trabalhando com multiplicacao de matrizes, nao podemos ter quantidade de caracteres impares
if len(crip)%2==0:
    print ("numero de caracteres pares")
else: print("numero de caracteres impares, favor incluir um espaco ou _ ao fim da frase")

pic=len(crip)/2
c=pic-1
pic1=crip[0:int(pic)]
pic2=crip[int(pic):len(crip)]
B=[pic1,pic2]

A=[[ 8, -3],[-5,2]]
print(np.matmul(A,B))
