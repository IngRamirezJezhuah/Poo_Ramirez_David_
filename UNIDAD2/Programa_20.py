#crea un programa que una 3 conjuntos luego recorrer ese conjunto 
#y hacer uno nuevo con unicamente los valores pares
#imprimir el resultado commit Programa 20- conjunto numeros pares

conjuntito1= {1,3,5,7,9}
conjuntito2= {2,4,6,11}
conjuntito3= {8,10,12}

unionsita = conjuntito1 | conjuntito2 | conjuntito3
print("-------------------------------------")
print("tus valores son;  ◟( ˃̶͈◡ ˂̶͈ )◞")
print (unionsita)
print("-------------------------------------")
print("y los numeros pares del conjunto son:(｡- .•)")
for unionsita in unionsita:
    if unionsita % 2 == 0:
        print("(੭ ˊ^ˋ)੭ ",unionsita)
print("-------------------------------------")