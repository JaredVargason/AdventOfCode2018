import re

iterations = 20

def sum(rule : str):
    return int('0b' + rule.replace('#', '1').replace('.','0'))

with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]
    plants = {i: (True if obj == '#' else False) for i, obj in enumerate(lines[0].split(' ')[2])}
    print(plants)

    ruleStrings = [line.split(' => ') for line in lines[2:]]
    for i, string in enumerate(ruleStrings):

    print(ruleStrings)

    #indices = [int('0b' + i.replace('#', '1')('.','0')) for i in ruleStrings[0]] 

for i in range(iterations):
    pass