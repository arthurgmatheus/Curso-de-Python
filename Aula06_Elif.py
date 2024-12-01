salario = float(input("Digite seu salário: "))

if(salario >=5000):
    print("Você é sênior!")
elif(salario >= 4000):
    print("Você é pleno!")
elif(salario >= 2000 and salario <=3800):
    print("Você é júnior!")
else:
    print("Você é estagiário!")