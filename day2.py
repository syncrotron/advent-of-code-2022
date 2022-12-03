#!/usr/bin/env python3
from re import A

MatchScore = {
    'A' : lambda a: 6 if a == 'Y' else int(a == 'X') * 3, #ROCK
    'B' : lambda b: 6 if b == 'Z' else int(b == 'Y') * 3, #PAPER
    'C' : lambda c: 6 if c == 'X' else int(c == 'Z') * 3  #SCISSORS
}
    
HadScore = {
    'X' : 1, #ROCK
    'Y' : 2, #PAPER
    'Z' : 3 #SCISSORS
}

score = 0
for line in open("./input/day2.txt", "r"):
    score = score + MatchScore[line[0]](line[2]) + HadScore[line[2]]

print(f"Total Score: {score}")