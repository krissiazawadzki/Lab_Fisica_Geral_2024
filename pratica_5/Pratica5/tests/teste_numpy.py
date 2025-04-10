import LabIFSC as lab
import numpy as np

lista_normal = [0,1,2,3,4]
lista_numpy = np.array(lista_normal)
incerteza_padrao = 0.1

#print("Running Medida() with lista_normal")
#n1 = lab.Medida(lista_normal, incerteza=incerteza_padrao, unidade="m")
print("Running M() with lista_normal")
n2 = lab.M(lista_normal, incerteza=incerteza_padrao, unidade="m")
#print("Printing n1 elements")
#for i in n1:
#    print("{latex:ifsc}", i)
print("Printing n2 elements")
for j in n2:
    print("{:latex,ifsc}".format(j))
print(type(n2))
print(type(n2[0]))
#print("Running Medida() with lista_normal")
#n1 = lab.Medida(lista_numpy, incerteza=incerteza_padrao, unidade="m")
print("Running M() with lista_numpy")
n2 = lab.M(lista_numpy, incerteza=incerteza_padrao, unidade="m")
#print("Printing n1 elements")
#for i in n1:
#    print("{latex:ifsc}", i)
print("Printing n2 elements")
for j in n2:
    print("{:latex,ifsc}".format(j))
print(type(n2))
print(type(n2[0]))

print("Teste de multiplicação numpy: n2*n2")

n3 = n2*n2
for i in n3:
    print("{:latex,ifsc}".format(i))
