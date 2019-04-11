import operator
from itertools import *
def add_mineral(table, name, value, weight):
    table.append([name, value, weight])

minerals = []
n = input("numero di minerals= ")
for x in range(int(n)):
    print(x+1, "minerale")
    value = int(input("valore in euro = "))
    weight = int(input("peso in kg = "))
    n_mineral = "m" + str(x+1)
    add_mineral(minerals, n_mineral, value, weight)
'''
add_mineral(minerals, "m1", 120, 620)
add_mineral(minerals, "m2", 340, 140)
add_mineral(minerals, "m3", 180, 240)
add_mineral(minerals, "m4", 398, 180)
add_mineral(minerals, "m5", 260, 560)
add_mineral(minerals, "m6", 280, 189)
'''

comb = []
for i in combinations(minerals, 3):
    name = ""
    value = 0
    weight = 0
    for n in range(3):
        name += i[n][0]
        value += i[n][1]
        weight += i[n][2]
    
    comb.append([name, value, weight])
print()

minweight = int(input("minweight= "))
maxweight = int(input("maxweight= "))

output = ["", 0 , 0]
for i in comb :
    if i[1] > output[1] and minweight < i[2] <=maxweight :
        output[0] = i[0]
        output[1] = i[1]
        output[2] = i[2]
print()
print(output)
