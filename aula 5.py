#texto = "Explorando a diversidade de linguagem de programação python"

#print(f"Tamanho do texto  = {len(texto)}")
#print(f"Python in texto  = {'Python' in texto}")
#print(f"Quantidade de e no texto  = {texto.count('e')}")
#print(f"As 5 primeiras letras são: {texto[:5]}")

#Parte2 listas

#cores = ['vermelho','azul','verde','amarelo','roxo']
#for cor in cores:
   # print(f'Posição = {cores.index(cor)}, cor = {cor}')

#List Comprehensions,map e filter

Linguagens = {"Python","Java","JavaScript","PHP","Kotlin","C#","C"}
print("antes de listcomp =", Linguagens)
Linguagens = {item.lower() for item in Linguagens}
print("\nDepois da Listcomp", Linguagens)