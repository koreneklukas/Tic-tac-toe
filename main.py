"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lukas Korenek
email: koreneklukas@seznam.cz
"""

print(f"Welcome to Tic Tac Toe\n"
	  f"{'=' * 45}\n"
	  f"GAME RULES:\n"
	  f"Each player can place one mark (or stone)\n"
	  f"per turn on the 3x3 grid. The WINNER is\n"
	  f"who succeeds in placing three of their\n"
	  f"marks in a:\n"
	  f"* horizontal,\n"
	  f"* vertical or\n"
	  f"* diagonal row\n"
	  f"{'=' * 45}\n"
	  f"Let's start the game\n"
	  f"{'-' * 45}")

# Definování hracího pole
pole = [[" " for _ in range(3)] for _ in range(3)]


def zobraz_pole(pole):
	print("+---+---+---+")
	for radek in pole:
		print("| " + " | ".join(radek) + " | ")
		print("+---+---+---+")


def vyber_hrace(symbol) -> None:
	'''
	Funkce pro vybrání uživatele a násládné odehrání hráčova tahu
	'''
	while True:
		print("=" * 45)
		try:
			player_choice = int(input(f"Player {symbol} | Please enter your move number: "))
			if not 1 <= player_choice <= 9:
				print("Please enter a number between 1 and 9.")
				continue
		except ValueError:
			print("Invalid input. Please enter a number.")
			continue

		index = player_choice - 1
		radek = index // 3
		sloupec = index % 3

		if pole[radek][sloupec] == " ":
			pole[radek][sloupec] = symbol
			break
		else:
			print("This spot is already taken. Try a different one.")

	zobraz_pole(pole)


def kontrola_vyhry():
	kombinace = [
		# řádky
		[(0, 0), (0, 1), (0, 2)],
		[(1, 0), (1, 1), (1, 2)],
		[(2, 0), (2, 1), (2, 2)],

		# sloupce
		[(0, 0), (1, 0), (2, 0)],
		[(0, 1), (1, 1), (2, 1)],
		[(0, 2), (1, 2), (2, 2)],

		# diagonály
		[(0, 0), (1, 1), (2, 2)],
		[(0, 2), (1, 1), (2, 0)],
	]

	for kombinace_v in kombinace:
		znaky = [pole[r][s] for r, s in kombinace_v]
		if znaky == ["X","X","X"]:
			print("Congratulations, the player X WON!")
			return True
		elif znaky == ["O","O","O"]:
			print("Congratulations, the player O WON!")
			return True
	return False

def spusteni_smycky():
	'''Hlavní smyčka
	Spouští obě metody a dává je do smyčky, dokud není vítězný hráč
	'''
	for tah in range(9):
		if tah % 2 == 0:
			symbol = "O"
		else:
			symbol = "X"
		vyber_hrace(symbol)

		if kontrola_vyhry():
			break
	else:
		print("It´s draw!")


if __name__ == "__main__":
	spusteni_smycky()