a = "bulbasaur.txt"
b = "squirtle.txt"

with open(a, "r") as infile, open(b, "w") as outfile:
    for line in infile:
        if len(line) > 84:
            outfile.write(line[84:])
        else:
            outfile.write("\n")
