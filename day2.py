#!/usr/bin/env python3
# Samuel Horovatin, December 2022

MatchScoreInitial = {
    'A' : lambda a: 6 if a == 'Y' else (a == 'X') * 3, #ROCK
    'B' : lambda b: 6 if b == 'Z' else (b == 'Y') * 3, #PAPER
    'C' : lambda c: 6 if c == 'X' else (c == 'Z') * 3  #SCISSORS
}
    
HadScoreInitial = {
    'X' : 1, #ROCK
    'Y' : 2, #PAPER
    'Z' : 3 #SCISSORS
}

score = 0
for line in open("./input/day2.txt", "r"):
    score = score + MatchScoreInitial[line[0]](line[2]) + HadScoreInitial[line[2]]

print(f"Total Initial Score: {score}")
input("Press Enter to continue...")

MatchScoreEnhanced = lambda result: 6 if result == 'Z' else (result == 'Y') * 3

HadScoreEnhanced = {
    'A' : lambda result: 2 if result == 'Z' else (1 if result == 'Y' else 3), # B(2) for Win, A(1) for tie, C(3) for loss
    'B' : lambda result: 3 if result == 'Z' else (2 if result == 'Y' else 1), # C(3) for Win, B(2) for tie, A(1) for loss
    'C' : lambda result: 1 if result == 'Z' else (3 if result == 'Y' else 2)  # A(1) for Win, C(3) for tie, B(2) for loss
}

score = 0
for line in open("./input/day2.txt", "r"):
    score = score + MatchScoreEnhanced(line[2]) + HadScoreEnhanced[line[0]](line[2])

print(f"Total Enhanced Score: {score}")