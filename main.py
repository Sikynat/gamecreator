#dados do jogo
nome = 'project'
story = 0
gameplay = 0
graficos = 0
audio = 0

#apresentação
print('Dadonas games enterteriment\n')
print('Olá jovem seja bem-vindo ao CreateGames\nnesse jogo você é um pequeno desenvolvedor de jogos independente\n')
print('Qual o nome de seu jogo?\n')
#da nome ao jogo
nome = str(input('Nome: '))
print(f'Gostei desse nome {nome}')

print('Vamos começar que tipo de jogo gostaria de criar?\n')

print('tiro [0]')
print('rpg [1]')
print('terror [2]')

type = str(input('exemplo: [0] [1] [2] '))
if type == '0':
    print('entao voce quer fazer um jogo de tiro')
    print('de 0 a 10 quanto de historia você vai se dedicar a fazer para seu jogo\n')
    while story == 0:
        story += int(input('Digite um numero no valor de 1 a 10: '))
        print(f'seu jogo tera uma historia nivel: {story}')