a=2026
b=[int(i) for i in str(a)] #converts the integer a to a string, iterates over each character in the string, converts it back to an integer, and creates a list of these integers
print(sum(b))