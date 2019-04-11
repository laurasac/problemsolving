#by farfra
import os

x = int(input("x iniziale: "))
y = int(input("y iniziale: "))
dir_iniz = input("direzione iniziale (N S W E): ")
pos = [x,y]

print()
print("comando per comando (1)")
print("lista di comandi es. F,A,F,O,F...(2)")
mode = int(input())

'''
N = 1
E = 2
S = 3
W = 4
'''

direc = 0
if dir_iniz == "N":
	direc = 1
elif dir_iniz == "E":
	direc = 2
elif dir_iniz == "S":
	direc = 3
elif dir_iniz == "W":
	direc = 4

os.system("cls")
d = ""


if mode == 1:

	while True:
		mov = input("O A F: ")
		if mov == "O":
			direc += 1
			if direc == 5:
				direc = 1

		elif mov == "A":
			direc -= 1
			if direc == 0:
				direc = 4

		elif mov == "F":
			if direc == 1:
				y += 1
				pos = [x,y]

			elif direc == 2:
				x += 1
				pos = [x,y]

			elif direc == 3:
				y -= 1
				pos = [x,y]

			elif direc == 4:
				x -= 1
				pos = [x,y]

		os.system("cls")

		if direc == 1:
			d = "^"
		elif direc == 2:
			d = ">"
		elif direc == 3:
			d = "v"
		elif direc == 4:
			d = "<"
		print("pos =", pos, "dir =", d)

if mode == 2:
	lista_mov = input("inserisci i movimenti es A,O,F,F,A,O: ")
	lista_mov.split(",")
	for mov in lista_mov:

		if mov == "O":
			direc += 1
			if direc == 5:
				direc = 1

		elif mov == "A":
			direc -= 1
			if direc == 0:
				direc = 4

		elif mov == "F":
			if direc == 1:
				y += 1
				pos = [x,y]

			elif direc == 2:
				x += 1
				pos = [x,y]

			elif direc == 3:
				y -= 1
				pos = [x,y]

			elif direc == 4:
				x -= 1
				pos = [x,y]

	if direc == 1:
			d = "^"
	elif direc == 2:
		d = ">"
	elif direc == 3:
		d = "v"
	elif direc == 4:
		d = "<"
			
	print("pos =", pos, "dir =", d)