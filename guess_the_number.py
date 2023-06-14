import random

numero_secreto = random.randint(1, 10)
adivinhacao = None

while adivinhacao != numero_secreto:
    adivinhacao = int(input("Adivinhe um número entre 1 e 10: "))
    if adivinhacao != numero_secreto:
        print("Errado! Tente novamente.")
    else:
        print("Parabéns! Você acertou!")

print("Fim do jogo.")
