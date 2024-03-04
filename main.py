print("Hello word! My name is Iuri Barreto")

print("Estudando Python")
print("Média de notas de alunos")
print("Pensamento Computacional com Python")
print("pilares:")
print("1. Abstração")
print("2. Pensamento Algoritmo")
print("3. Decomposição")
print("4. Reconhecimento de padrões")

quantidadeNotas = int(input("Quantas notas deseja calcular? "))
soma = 0

for x in range(quantidadeNotas):
  nota = float(input("Digite a nota: "))
  soma = soma + nota


media = float(soma / quantidadeNotas)

print("A média é: ", media)

print("A média é: {}".format(media))
print("now, this code is running in gitHub")