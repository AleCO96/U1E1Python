lista= list()
lista2=list()
lista3=list()
aux=""
frase= "Hola mi nombre es Alejandro y me apellido Cruz"
archivo= open(r"C:\Users\aleja\Documents\Frase Desordenada.txt")
fraseDesordenada= archivo.read()
lista = fraseDesordenada.split()
lista2 = frase.split()
lista3 = fraseDesordenada.split()
for i in range(0,len(lista)):
    for j in range(0,len(lista)):
        if lista[i] == lista2[j]:
            lista3[j]=lista2[j]

for i in range(0,len(lista2)):
    aux=aux+lista3[i]
    aux=aux+" "
    
print(aux)
