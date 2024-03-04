print("Hello word! My name is Iuri Barreto")

print("Estudando Python")
print("Média de notas de alunos")

quantidadeNotas = int(input("Quantas notas deseja calcular? "))
soma = 0

for x in range(quantidadeNotas):
  nota = float(input("Digite a nota: "))
  soma = soma + nota


media = float(soma / quantidadeNotas)

print("A média é: ", media)

print("A média é: {}".format(media))