alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(''' 
 ██████╗  █████╗ ███████╗  ███████╗  █████╗ ██████╗     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗██╔════╝ ██╔════╝  ██╔══██╗██╔══██╗   ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║      ███████║██████╗  ███████╗  ███████║██████╔╝   ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║      ██╔══██║██╔══╝   ╚════██║  ██╔══██║██╔══██╗   ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗ ██║  ██║███████╗ ███████║  ██║  ██║██║  ██║   ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚══════╝  ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        C     A      E       S        A      R            C   I   P   H   E   R
''')

direction = input("Digite 'encode(encrypt)' para criptografar e 'decode(decrypt)' para descriptografar:\n")
text = input("Digite sua mensagem:\n").lower()
shift = int(input("Digite o número de deslocamentos:\n"))

#TODO1

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shift_position = (alphabet.index(letter) + shift_amount) % 26 #ou seja, 7 -> 9 se os deslocamentos forem 2 e usando %26 para voltar ao início do alfabeto
        cipher_text += alphabet[shift_position]

    print(f"A mensagem criptografada é: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)

def descrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shift_position = (alphabet.index(letter) - shift_amount) % 26 #ou seja, 7 -> 5 se os deslocamentos forem 2 e usando %26 para voltar ao início do alfabeto
        cipher_text += alphabet[shift_position]

    print(f"A mensagem descriptografada é: {cipher_text}")


descrypt(original_text=text, shift_amount=shift)

