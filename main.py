# Processamento de Dados I - Teórica
# Equipe 08h - Professor Emerson
# Integrantes do Grupo:
# - Rafael Almeida Souza
# - Renato Wallace Lordello de Almeida
# - Inacio Pereira da Silva
# - Jorge Henrique Conceição Pinto
# - Arttur Barbosa de Oliveira

# Importa o módulo
import random

# Cria a lista para armanzenamento das dificuldades
dificuldades = ['easy', 'medium', 'hard']

# Função para apresentação do menu
def menu():
	print("=" * 30)
	print("     CONTADOR DE DÍGITO")
	print("=" * 30)
	print('[1] - Fácil')
	print('[2] - Média')
	print('[3] - Difícil')
	print('[0] - Sair do jogo')
	print('\n')
 
# Função para geração de número aleatório para retorná-lo junto com sua quantidade
def gerarQtdAleatoria(dificuldade):
	max = 0
	# Atribuindo o valor máximo de acordo com a dificuldade
	try:
		# Apresentando as possibilidades de acordo com o valor associado
		match dificuldade:
			case 'easy':
				max = 1000
			case 'medium':
				max = 10000
			case 'hard':
				max = 100000
			case _:
				# Erro associado para evitar digitação de strings
				raise ValueError('dificuldade inválida')
	# Erro geral
	except Exception as e:
		print('ERRO:', e)
	# Importação de um valor aleatório
	numero = random.randint(1, max)
	# Contagem da quantidade de caracteres do número transformado em string
	qtdChars = len(str(numero))
	# Retorno os valores, agora tranformados em elementos de uma lista
	return [numero, qtdChars]
# Função para pedir qual dificuldade será escolhida e fazer a contagem de chances do usuário para acertar
def logica():
  # Função já definida é chamada
	menu()
	# Obtém a opção escolhida pelo usuário
	opcao = int(input('Digite uma dificuldade: '))
	# Verifica o sinal do número para assim armazenar o valor
	if opcao <= 0:
		print('Fim do jogo')
		return
	# Obtem a dificuldade
	dificuldade = dificuldades[opcao - 1]

	[numero, quantidade] = gerarQtdAleatoria(dificuldade)
	print(f'Um número foi gerado na dificuldade {dificuldade}!')

	vidas = 3

	# Loop até ter tentivas
	while vidas > 0:
		# Obtem o chute do usuário
		chute = int(input('Qual a quantidade de algarismos no número? '))

		# Verifica se o usuário acertou
		if chute == quantidade:
			print('\nVocê acertou a quantidade!')
			break

		# O usuário não acertou
		print('\nTente novamente')
		vidas -= 1

	print('\nO número era:', numero)

logica()