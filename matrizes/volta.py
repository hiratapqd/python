import math
import numpy as np
A=[[ 8, -3],[-5,2]]
ainv = np.linalg.inv(A)
#blocos=input("quantos blocos foram recebidos? ")
C=[]
B=[]
#for i in range(int(blocos)):
blur=input("digite o primeiro bloco da matrix recebida: ")
plunkt = list(map(int, blur.split()))
B.append(plunkt)
blur=input("digite o segundo bloco da matrix recebida: ")
plunkt = list(map(int, blur.split()))
B.append(plunkt)
origem=np.matmul(ainv,B)
linha, colunas=len(origem),len(origem[0])

for linha in range(linha):
    for coluna in range (colunas):
        C.append(origem[linha][coluna])

crip=[]
for i in range(len(C)):
        genders = {
            1:"a",
            2:"b",
            3:"c",
            4:"d",
            5:"e",
            6:"f",
            7:"g",
            8:"h",
            9:"i",
            10:"j",
            11:"k",
            12:"l",
            13:"m",
            14:"n",
            15:"o",
            16:"p",
            17:"q",
            18:"r",
            19:"s",
            20:"t",
            21:"u",
            22:"v",
            23:"w",
            24:"x",
            25:"y",
            26:"z",
            27:".",
            28:",",
            29:"_",
            30:" "
        }
        crip.append(genders.get(C[i]))
        i+=1
str1 = ''.join(crip)
print (str1)
