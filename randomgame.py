import random

player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")

s1 = 10
s2 = 10

d1 = random.randint(1, 10)
d2 = random.randint(1, 10)

print("---Player 1 Turn---")
while (True):
    g1 = int(input("Enter your guess: "))
    s1 = s1 - 1
    if g1 == d1:
        break

print("---Player 2 Turn---")
while (True):
    g2 = int(input("Enter your guess: "))
    s2 = s2 - 1
    if g2 == d2:
        break

print("---Summary---")
print("{} : {}".format(player1, s1))
print("{} : {}".format(player2, s2))

print("---Result---")
if s1 > s2:
    print("{} is winner".format(player1))
elif s2 > s1:
    print("{} is winner".format(player2))
else:
    print("Match Draw")