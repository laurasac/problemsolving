# Fatto da Davide Barbini

import statistics as stats

def average(nlist=[]):
    return stats.mean(nlist)

def mode(nlist=[]):
    return stats.mode(nlist)

def median(nlist=[]):
    return stats.median(nlist)


nlist = [1,10,1,11,12]

print(mode(nlist))
print(median(nlist))
print(average(nlist))
print('stai attento all\'ordine delle requestssss')