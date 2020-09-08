import random

memoria = [' '] * 20
opcao = 0
tamanho = 0
char = ''
maior = 0
menor = 9999
menorpos = 0

for i in range(20):
	if(random.randint(0,9) >= 5):
		memoria[i] = 'x'
	else:
		memoria[i] = ' '

for i in range(0,20):
		print(memoria[i], end="|")
print()

while(opcao != 4):
	print("1 - First-fit")
	print("2 - Best-fit")
	print("3 - Worst-fit")
	print("4 - Sair")
	print("Escolha o algoritmo pelo numero")
	opcao = int(input())
	print("Digite o tamanho da informacao")
	tamanho = int(input())
	print("Digite a letra a ser utiliada")
	char = input()

	if(opcao == 1):
		ini = 0
		while(ini < 20):
			if memoria[ini] == ' ':
				end = ini + 1
				while(end < 20):
					if memoria[end] != ' ':
						break
					end = end + 1
				print("Espaço[",ini,'-',end,"]")
				fit = end-ini 
				if fit >= tamanho:
					for i in range (tamanho):
						memoria[ini]=char
						ini+=1
					break
				ini = end
			ini = ini + 1
		pass
		
	else:
		if (opcao == 2):
			ini = 0
			menor = 9999
			while(ini < 20):
				if memoria[ini] == ' ':
					end = ini + 1
					while(end < 20):
						if memoria[end] != ' ':
							break
						end = end + 1
					print("Espaço[",ini,'-',end,"]")
					fit = end-ini
					if fit >= tamanho:
						if menor > fit:
							menor = fit
							menorpos = ini
					ini = end
				ini = ini + 1
			for i in range (tamanho):
					memoria[menorpos]=char
					menorpos+=1
			pass

		else:
			if(opcao == 3):
				ini = 0
				while(ini < 20):
					if memoria[ini] == ' ':
						end = ini + 1
						while(end < 20):
							if memoria[end] != ' ':
								break
							end = end + 1
						print("Espaço[",ini,'-',end,"]")
						fit = end-ini
						if fit > maior:
							maior = fit
							maiorpos = ini
						ini = end
					ini = ini + 1
				for i in range (tamanho):
					memoria[maiorpos]=char
					maiorpos+=1
				pass
	
	if(opcao==4):
		print("ENCERRADO")

	for i in range(0,20):
		print(memoria[i], end="|")
	print()
