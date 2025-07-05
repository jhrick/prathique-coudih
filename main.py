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
from datetime import datetime 

datetimeFormat = '%Y-%m-%d %H:%M:%S'

historico = []

# Cria a lista para armanzenamento das dificuldades
dificuldades = ['fácil', 'média', 'difícil']

# Menu principal
def menuPrincipal():
	print("=" * 30)
	print("     CONTADOR DE DÍGITO")
	print("=" * 30)
	print("[1] Jogar")
	print("[2] Histórico")
	print("[0] Sair")
	print()

# Menu de dificuldades
def menuDificuldade():
	print("=" * 30)
	print("     ESCOLHA A DIFICULDADE")
	print("=" * 30)
	print("[1] - Fácil")
	print("[2] - Média")
	print("[3] - Difícil")
	print("[0] - Voltar ao menu principal")
	print()

def gerarHistorico():
	print('=' * 30)
	print('	  HISTÓRICO')
	print('=' * 30)
 
	if not historico:
		print("Não há histórico ainda.\n")
		return

	ultimos = historico[-5:]
	for item in ultimos:
		print(item)
	print()

def gravarHistorico():
	if not historico:
		return

	with open('historico.txt', 'a') as f:
		now = datetime.now()
  
		f.write(f'[{now.strftime(datetimeFormat)}]')
		f.writelines(historico)
		f.write('\n')

	print('Histórico registrado!')
 
# Função para geração de número aleatório para retorná-lo junto com sua quantidade
def gerarQtdAleatoria(dificuldade):
	max = 0
	# Atribuindo o valor máximo de acordo com a dificuldade
	try:
		# Apresentando as possibilidades de acordo com o valor associado
		match dificuldade:
			case 'fácil':
				max = 1000
			case 'média':
				max = 10000
			case 'difícil':
				max = 100000
			case _:
				# Erro associado para evitar digitação de strings
				raise ValueError('dificuldade inválida')
	except Exception as e:
		print('ERRO:', e)

	# Gera um número aleatório em um intervalo definido
	numero = random.randint(1, max)

	# Contagem da quantidade de caracteres do número transformado em string
	qtdChars = len(str(numero))

	# Retorno os valores, agora tranformados em elementos de uma lista
	return [numero, qtdChars]

# Lógica do jogo
def jogar():
	while True:
		menuDificuldade()

		# Obtém a opção escolhida pelo usuário
		opcao = int(input('Digite uma dificuldade: '))
 
		if opcao == 0:
			return

		if 1 <= opcao <= 3:
			# Obtem a dificuldade
			dificuldade = dificuldades[opcao - 1]

			[numero, quantidade] = gerarQtdAleatoria(dificuldade)
			print(f'Um número foi gerado na dificuldade {dificuldade}!')

			vidas = 3

			# Loop até ter tentivas
			while vidas > 0:
				chute = int(input('Qual a quantidade de algarismos no número? '))

				# Verifica se o usuário acertou
				if chute == quantidade:
					print('\nVocê acertou a quantidade!')
					historico.append(f'\nDificuldade {dificuldade}, Resultado: ACERTOU, Número: {numero}')
					break
				else:
					vidas -= 1
					print('\nTente novamente. Vidas restantes:', vidas)

			if vidas == 0:
				print(f'\nAcabaram as tentivas. O número era: {numero}')
				historico.append(f'\nDificuldade {dificuldade}, Resultado: ERROU, Número: {numero}')

		else:
			print('Opção de dificuldade inválida')

def main():
	while True:
		menuPrincipal()
		try:
			opcao = int(input("Escolha uma opção: "))
		except ValueError:
			print("Entrada inválida. Digite um número.")
			continue

		if opcao == 1:
			jogar()
		elif opcao == 2:
			gerarHistorico()
		elif opcao == 0:
			gravarHistorico()
			print("Saindo do jogo.")
			break
		else:
			print("Opção inválida.")

main()