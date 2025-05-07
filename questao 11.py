Nome = (input("Digite seu nome completo:"))
nota1 = float(input("Digite sua nota da primiera prova:"))
nota2 = float(input("Digite sua nota da segunda prova:"))
nota3 = float(input("Digite sua nota da terceira prova:"))
nota4 = float(input("Digite sua nota da quarta prova:"))

soma = nota1 + nota2 + nota3 + nota4
media = soma/4

if media >= 7:
    print(f"O aluno{Nome} foi aporvao por Média.")
else:
    print(f"O aluno{Nome} esta reprovado.")
