from os import system, name
palavrasecreta = str(input('Digite a palavra secreta desejada para o jogo da velha e peça para o seu amigo tapar os olhos: ')).upper()
while True:
    try:
        vidas = int(input('Quantas vezes a pessoa pode errar antes de perder? '))
    except (ValueError, TypeError):
        print('\033[31mEsperava-se um número inteiro\033[m')
    except Exception as erro:
        print(f'\033[31mErro: {erro}\033[m')
    else:
        if vidas <= 0:
            print('\033[31mEsperava-se um número inteiro positivo e diferente de zero.\033[m')
        else:
            break
system('cls') if name == 'nt' else system('clear')
cont = 1
tot = 0
escondida = []
for elemento in palavrasecreta:
    escondida.append('-')
while True:
    print(str(f'{cont}° RODADA: {"".join(escondida)}'))
    escolha = str(input('Digite uma letra: ')).upper()[0]
    x = 0
    conseguiu = False
    for caracter in palavrasecreta:
        if escolha == caracter:
            if escondida[x] != '-':
                print(f'Letra {escolha} já foi digitada')
            else:
                escondida[x] = escolha
            conseguiu = True
        x += 1
    if not conseguiu:
        vidas -= 1
        print(f'{escolha} não está na palavra. Total de chances = {vidas}')
    if vidas == 0:
        print('\033[1;31mVocê Perdeu!\033[m')
        break
    elif palavrasecreta == ''.join(escondida):
        print('\033[1;35mVocê Venceu!\033[m')
        break
