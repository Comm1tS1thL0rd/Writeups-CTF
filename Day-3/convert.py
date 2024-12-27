a = 'pikachu.txt'
b = 'pokemon.jpeg'

with open(a, 'r') as infile:
    hex_data = infile.read().strip()

image_data = bytes.fromhex(hex_data)

with open(b, 'wb') as outfile:
    outfile.write(image_data)
