# Calculadora de IMC(Ou BMI em inglês

n1 = float(input("Digite seu peso em kg: "))
n2 = float(input("Digite sua altura em metros: "))
imc = n1 / (n2 ** 2)

print("Seu IMC é: ", imc)