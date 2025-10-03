import random

print("Escolha pedra[0], papel[1] ou tesoura[2]: ")
usuario = int(input("Qual é a sua escolha? "))


escolhas = random.randint(0, 2)


if escolhas == 0:
    print("pedra")
elif escolhas == 1:
    print("papel")
else:
    print("tesoura")

print(f"Você escolheu {usuario} e o computador escolheu {escolhas}.")

