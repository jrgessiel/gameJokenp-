# Gessiel José Januário Júnior

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)

print('')
print('-	Bem vindo, jogador(a)! ')
print('- Este jogo se chama Pedra, Papel, Tesoura. Se divirta!!!')

def menu():
	print('\n- Dentre as opções do menu abaixo, escolha um número.')
	print('###01 | Jogar')
	print('###02 | Regras')
	print('###03 | Créditos\n')
	choice_menu = int(input('- | '))
	if type(choice_menu) is not int or choice_menu < 0 or choice_menu > 3:
		print('- Jogador(a), escolha desconhecida, tente novamente usando um dos valores possiveis.\n')
		menu()
	elif choice_menu == 1:
		m_jogar()
	elif choice_menu == 2:
		m_regras()
	elif choice_menu == 3:
		m_creditos()
	else:
		print('- Erro interno inesperado.\n')
		menu()

def m_jogar():
	print()
	print('###01 | Pedra')
	print('###02 | Papel')
	print('###03 | Tesoura')
	print('\n- Dentre as opções do menu acima, escolha um número.')
	choice_player = int(input('- Qual será a sua jogada, jogador(a)? \n- | '))
        
	if type(choice_player) is not int or choice_player < 0 or choice_player > 3:
		print('- Jogador(a), escolha desconhecida, tente novamente usando um dos valores possiveis.\n')
		m_jogar()
	elif choice_player == 1:
		print('\n- Jo')
		sleep(1)
		print('- Ken')
		sleep(1)
		print('- Pô!\n')
		sleep(2)
		print('-=-=' * 8)
		print(f'- Computador jogou: {itens[computer]}.')
		print(f'- Jogador(a) jogou: Pedra. ')
		print('-=-=' * 8)
		if computer == 0:
			print('\n- O jogo encerrou em empate!\n')
			menu()
		elif computer == 1:
			print('\n- O computador venceu!\n')
			menu()
		elif computer == 2:
			print('\n- O jogador venceu!\n')
			menu()

	elif choice_player == 2:
		print('\n- Jo')
		sleep(1)
		print('- Ken')
		sleep(1)
		print('- Pô!\n')
		sleep(2)
		print('-=-=' * 8)
		print(f'- Computador jogou: {itens[computer]}.')
		print(f'- Jogador(a) jogou: Papel. ')
		print('-=-=' * 8)
		if computer == 0:
			print('\n- O jogador venceu!\n')
			menu()
		elif computer == 1:
			print('\n- O jogo encerrou em empate\n')
			menu()
		elif computer == 2:
			print('\n- O computador venceu!\n')
			menu()

	elif choice_player == 3:
		print('\n- Jo')
		sleep(1)
		print('- Ken')
		sleep(1)
		print('- Pô!\n')
		sleep(2)
		print('-=-=' * 8)
		print(f'- Computador jogou: {itens[computer]}.')
		print(f'- Jogador(a) jogou: Tesoura. ')
		print('-=-=' * 8)
		if computer == 0:
			print('\n- O computador venceu!\n')
			menu()
		elif computer == 1:
			print('\n- O jogador venceu!\n')
			menu()
		elif computer == 2:
			print('\n-  O jogo encerrou em empate!\n')
			menu()


def m_regras():
	print()
	print('\n- Para ter chegado até aqui presumo que você não saiba jogar. Fique tranquilo(a) pois irei te ensinar!')
	print('- Havera uma contagem de 4 segundos, após a contagem chegar ao fim, você deverá escolher pedra, papel ou tesoura.')
	print('- A máquina também irá fazer sua escolha, seguido a isso, será calculado o ganhador.')
	print('- Para vencer é bem simples. Basta não ecolher o lado perdedor.')
	print('- ')
	print('- Tesoura corta papel, papel cobre pedra, pedra esmaga tesoura! Boa sorte!')
	menu()

def m_creditos():
	print()
	print('\n- Olá, jogador(a)! Espero que tenha gostado do que jogou, ou do que ainda irá jogar.\n')
	print('- Me chamo Gessiel Júnior e este projeto faz parte do meu portfólio pessoal.')
	print('- Ficarei feliz se você puder fornecer algum feedback sobre o projeto, código, \nestrutura ou qualquer relato que possa me tornar um desenvolvedor melhor!')
	menu()
computer = randint(0,2)
menu()
