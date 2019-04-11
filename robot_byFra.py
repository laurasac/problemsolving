import os

directions = ['N', 'E', 'S', 'W']
arrows = ['^', '>', 'v', '<']

os.system('cls')
print('ROBOT\n')
x = int(input('x iniziale: '))
y = int(input('y iniziale: '))

while True:
	dir_iniz = input('direzione iniziale (N S W E): ').upper()
	if dir_iniz in directions:
		break

pos = [x,y]
pos_iniz = [x, y, dir_iniz]

print('\ncomando per comando (1)')
print('lista di comandi es. F,A,F,O,F...(2)')
mode = int(input())

'''
N = 1
E = 2
S = 3
W = 4
'''

direc = 0
if dir_iniz == 'N':
	direc = 1
elif dir_iniz == 'E':
	direc = 2
elif dir_iniz == 'S':
	direc = 3
elif dir_iniz == 'W':
	direc = 4

os.system('cls')
d = ''

all_pos = []

if mode == 1:
	while True:
		print('pos = {}, dir = {} ({})'.format(pos, arrows[direc-1], directions[direc-1]))
		mov = input('O A F QUIT: ').upper()

		if mov == "QUIT":
			print('\nSENZA POSIZIONE INIZIALE')
			print(all_pos)
			print('\nCON POSIZIONE INIZIALE')
			print([pos_iniz]+all_pos)
			print()
			break

		if mov == 'O':
			direc += 1
			if direc == 5:
				direc = 1
			all_pos.append(pos+[directions[direc-1]])

		elif mov == 'A':
			direc -= 1
			if direc == 0:
				direc = 4
			all_pos.append(pos+[directions[direc-1]])

		elif mov == 'F':
			if direc == 1:
				y += 1
				pos = [x,y]
				all_pos.append(pos+[directions[direc-1]])
			elif direc == 2:
				x += 1
				pos = [x,y]
				all_pos.append(pos+[directions[direc-1]])

			elif direc == 3:
				y -= 1
				pos = [x,y]
				all_pos.append(pos+[directions[direc-1]])

			elif direc == 4:
				x -= 1
				pos = [x,y]
				all_pos.append(pos+[directions[direc-1]])

		os.system('cls')


if mode == 2:
	print('SCRIVI !!!MAIUSCOLO!!!')
	lista_mov = input('inserisci i movimenti es A,O,F,F,A,O: ').upper()
	lista_mov.split(',')

	for mov in lista_mov:
			
		if direc == 1:
			d = 'N'
		elif direc == 2:
			d = 'E'
		elif direc == 3:
			d = 'S'
		elif direc == 4:
			d = 'W'

		if mov == 'O':
			direc += 1
			if direc == 5:
				direc = 1
			all_pos.append(pos+[directions[direc-1]])

		elif mov == 'A':
			direc -= 1
			if direc == 0:
				direc = 4
			all_pos.append(pos+[directions[direc-1]])

		elif mov == 'F':
			if direc == 1:
				y += 1
				pos = [x,y]
				all_pos.append(pos+[directions[direc-1]])

			elif direc == 2:
				x += 1
				pos = [x,y]
				all_pos.append(pos+[directions[direc-1]])

			elif direc == 3:
				y -= 1
				pos = [x,y]
				all_pos.append(pos+[directions[direc-1]])

			elif direc == 4:
				x -= 1
				pos = [x,y]
				all_pos.append(pos+[directions[direc-1]])

	print('\nSENZA POSIZIONE INIZIALE')
	print(all_pos)
	print('\nCON POSIZIONE INIZIALE')
	print([pos_iniz]+all_pos)
