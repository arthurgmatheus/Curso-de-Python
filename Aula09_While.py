notas = []
contador = 1

while(contador <= 2):
    rm_aluno = int(input("RM: "))
    nota_aluno = float(input("Nota: "))
    resultado = [rm_aluno, nota_aluno]
    notas.append(resultado)

    contador +1


for n in notas:
        rm_aluno = n[0]
        nota_aluno = n[1]
        print("O RM ", rm_aluno, " tirou: ", nota_aluno)


