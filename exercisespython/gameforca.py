import random

word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)

print(chosen_word)  
stages = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """
]

lives = 6

display = "_" * len(chosen_word)
letras_certas = []
letras_erradas = []

fim = False

while not fim:
    print(stages[6 - lives])
    print(display)
    print("Letras erradas:", letras_erradas)

    guess = input("Adivinhe uma letra: ").lower()

    if guess in letras_certas or guess in letras_erradas:
        print("Você já tentou essa letra.")
        continue

    if guess in chosen_word:
        letras_certas.append(guess)
    else:
        letras_erradas.append(guess)
        lives -= 1
        print("Letra errada!")

    nova_display = ""
    for letter in chosen_word:
        if letter in letras_certas:
            nova_display += letter
        else:
            nova_display += "_"
    display = nova_display

    if "_" not in display:
        fim = True
        print("VOCÊ GANHOU!")
    elif lives == 0:
        fim = True
        print(stages[-1])
        print("VOCÊ PERDEU!")
        print("A palavra era:", chosen_word)

    





