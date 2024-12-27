a = 'charmander.txt'
b = 'pikachu.txt'

with open(a, 'r') as infile:
    lines = infile.readlines()

content = ''.join(line.strip() for line in lines)

with open(b, 'w') as outfile:
    outfile.write(content)
