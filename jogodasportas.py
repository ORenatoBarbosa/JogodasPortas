# O jogo das portas

def jogo():
	print("Você está em um salão.")
	print("Existem duas portas, a da esquerda e a da direita.")
	escolha = input("Em qual delas você quer entrar? Digite 'e', 'esquerda', 'd' ou 'direita': ").lower()

	if escolha == "e" or escolha == "esquerda":
		print("Você entrou na sala à esquerda, parece que não tem nada por aqui. Acho melhor você voltar correndo!")
	elif escolha == "d" or escolha == "direita":
		print("Excelente escolha! A sala à direita estava te esperando esse tempo todo! Que maravilhoso isso. Pena que não tem nada aqui para você. :(")
	else:
		print("Você não escolheu nenhuma das portas. Tente novamente.")
		jogo()

jogo()
# Renato Barbosa
