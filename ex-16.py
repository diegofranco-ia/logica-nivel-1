#16) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("quantas maças")
quantidade=int(input())
print("valor da compra foi")
preco1=int(quantidade*1.30)
preco2=int(quantidade*1.00)
if(quantidade>=12):
    print(preco2)
else:
    print(preco1)
