# Fatto da Davide Barbini

import operator
from itertools import *

def calculate(tab=[], maxkg=0, times=2):
    output = []
    # Crea tutte le possibili combinazioni
    for comb in combinations(tab, times):
        # Unisce le combinazioni in una singola lista
        union = ["", 0, 0]
        for n in range(times):
            union[0] += comb[n][0]
            union[1] += comb[n][1]
            union[2] += comb[n][2]

        if union[2] <= maxkg:
            output.append(union)

    sout = sorted(output, key=operator.itemgetter(1))
    return sout

def add_mineral(table, name="m?", value=0, weight=0):
    table.append([name, value, weight])

minerals = []

# Utilizzo: add_mineral(lista_minerali, nome, valore, peso)

add_mineral(minerals, "m1", 39, 58)
add_mineral(minerals, "m2", 42, 64)
add_mineral(minerals, "m3", 40, 65)
add_mineral(minerals, "m4", 38, 59)
add_mineral(minerals, "m5", 37, 61)
add_mineral(minerals, "m6", 42, 62)

max_pes = 180
res = calculate(minerals, max_pes, 3)
# Attenzione, stampare res UCCIDE la performance
#print(res)
for i in res:
    print(i)
