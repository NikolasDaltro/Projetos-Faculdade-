meu_conjunto  = set()

meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

print("Conjunto após adicionar elementos", meu_conjunto)

#Verificando se o 20 está dentro do conjunto

elemento = 20
if elemento in meu_conjunto:
    print(f"Está no conjunto")
else:
    print(f"{elemento} não está no conjunto")
#removendo Elemento no conjunto

meu_conjunto.remove(20)
print("Conjunto após remover o elemento 20",meu_conjunto)

#Criando um dicionario vazio seguido de atribução de chaves e valores
dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['Idade'] = 23
print(dici_1)

#Exemplo 2 criação de dicionario com pares chave: valor
dici_2 = {'nome': 'Maria', 'idade': 25}
#Exemplo 3- Criação de um dicionario com uma lista de tuplas representantes para chave:valor
dici_3 = dici_3 = dict([("nome", "Maria"), ("Idade", 25)])
#Exemplo 4 Criação de um dicionario usando a função bufit in zip() eduas listas, uma para chaves e outra para valores
dici_4 = dict(zip(['nome','idade'],['Maria',25]))
#teste se todas as construção resultam em obtos iguais
print(dici_1 == dici_2 == dici_3 == dici_4) #"Imprimirtrue"
#print(dici_1)



