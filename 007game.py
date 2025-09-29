print("""
 _____  _____  ______
|  _  ||  _  ||___  /
| |/' || |/' |   / / 
|  /| ||  /| |  / /  
\ |_/ /\ |_/ /./ /   
 \___/  \___/ \_/    
                     """)
print("""
      BEM VINDO AO JOGO 007
      Sua missão é encontrar o agente 007.
      CUIDADO COM AS DECISÔES!!! 
      """)

escolha1 = input('Você está em um labirinto escuro... Onde você quer ir? Escolha "esquerda" ou "direita"?: ')
if escolha1 == "esquerda":
    print('Você andou por 5 horas seguidas.. e morreu de sede. FIM DE JOGO!')
elif escolha1 == "direita":
    print('Você andou por 1 hora.. caminhou.. e chegou em um lago encantado!!! ')
    print('Esse lago tem um monstro!!!, volte imediatamente para o labirinto ou morra! ')
escolha2 = input('Você deseja voltar para o labirinto ou nadar até o outro lado do lago rapidamente? Escolha "voltar" ou "nadar": ')
if escolha2 == "voltar":
    print('Ufaaa!! Você voltou ao labirinto, ande por mais 2 horas... ')
elif escolha2 == "nadar":
    print('O monstro te pegou e você foi estrangulado!!! FIM DE JOGO! ')
escolha3 = input("""Você andou por 2 horas e chegou em uma mansão enorme, porem precisa descobrir a senha da porta de entrada.
[DICA]: A senha é o nome do agente secreto mais famoso do mundo...
DIGITE A SENHA->  """)
if escolha3 == "007":
    print('''PARABÉNS!!! Você entrou na mansão e encontrou o agente 007 acorrentado em um porão escuro!!!
Você o libertou e correram juntos para fora da mansão.. FIM DE JOGO!!! ''')
else: 
    print('SENHA INCORRETA!!! Você disparou o alarme e o monstro te encontrou!!! FIM DE JOGO! ')
