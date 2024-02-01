'''
-este o insusire de elemente ordonate
-pot avea valori diferite
-este mutabila(se pot adauga,sterge si in locui elemte
-putem accesa orice index
-valorile se pot repeta
'''
lista_diversa=[2,3.14,False,'Elefant',12345]
print(lista_diversa)
element_2=lista_diversa[1]
print(element_2)
#accesarea ultimul element
ultimul_element=lista_diversa[-1]
lungime_lista=len(lista_diversa)
print(lungime_lista)
element=lista_diversa[1]
print(element)
#adaugam un nou element in lista
#la sfarsitul listei se face cu append
lista_diversa.append('carte')
print(lista_diversa)
#adaugam in interiorul listei
lista_diversa.insert(3,10*10)
print(lista_diversa)

#inlocuim un element din lista
lista_diversa[2]=True
print(lista_diversa)
#sterge ultimul element din lista
lista_diversa.pop()
print(lista_diversa)
#stergem din lista prin index

lista_diversa.pop(3)
print(lista_diversa)
#list slicing
lista_inversa=lista_diversa[::-1]
print(lista_inversa)
lst1=lista_diversa[:3]# de la primul index (0)pana la index 3 dar index 3 nu este inclus
print(lst1)
lst2=lista_diversa[3:] # de la primul index (3)
print(lst2)
#inversarea ultimelor 3 elemente
ultimele_3_elemente=lista_inversa[-3:]

print(ultimele_3_elemente)

