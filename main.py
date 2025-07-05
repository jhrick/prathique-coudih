import random

dificuldades = ['easy', 'medium', 'hard']

def menu():
	print("=" * 30)
	print("     CONTADOR DE DÍGITO")
	print("=" * 30)
	print('[1] - Fácil')
	print('[2] - Média')
	print('[3] - Difícil')
	print('[0] - Sair do jogo')
	print('\n')

def gerarQtdAleatoria(dificuldade):
	max = 0
  
	match dificuldade:
		case 'easy':
			max = 1000
		case 'medium':
			max = 10000
		case 'hard':
			max = 100000
		case _:
			raise ValueError('dificuldade inválida')
  
	numero = random.randint(1, max)

	qtdChars = len(str(numero))

	return [numero, qtdChars]

def logica():
	menu()

	opcao = int(input('Digite uma dificuldade: '))

	if opcao == 0:
		print('Fim do jogo')
		return

	dificuldade = dificuldades[opcao - 1]

	[numero, quantidade] = gerarQtdAleatoria(dificuldade)
	print(f'Um número foi gerado na dificuldade {dificuldade}!')

	vidas = 3

	while vidas > 0:
		chute = int(input('Qual a quantidade de algarismos no número? '))

		if chute == quantidade:
			print('\nVocê acertou a quantidade!')
			break

		print('\nTente novamente')
		vidas -= 1

	print('\nO número era:', numero)

logica()