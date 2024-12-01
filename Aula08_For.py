notas = []

for x in range (2):
    codigo_aluno = int(input("RM: "))
    nota_aluno = float(input("Nota: "))
    resultado = [codigo_aluno, nota_aluno]
    notas.append(resultado)

print("Quantidade de notas: ", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota_aluno = n[1]
    print("O aluno com RM ", codigo_aluno, "tirou ", nota_aluno, ".")