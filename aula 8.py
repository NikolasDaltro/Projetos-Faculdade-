import matplotlib.pyplot as plt

#Dados

x = ['Janeiro','Março', 'Julho','Fervereiro']
y = [150,50,250,100]

#Criando grafico de linha

plt.bar(x,y)

#Adicionando rótulos aos eixos
plt.xlabel('Eixo x')
plt.ylabel('Eixo Y')

#Adicionando titulo ao grafico
plt.title('Exemplo de Grafico de Linha')

#Mostrar o Grafico
plt.show()


