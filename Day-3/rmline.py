def remove_first_line(a, b):
    with open(a, "r") as infile:
        lines = infile.readlines()

    with open(b, "w") as outfile:
        outfile.writelines(lines[1:])

if __name__ == "__main__":
    a = "squirtle.txt"
    b = "charmander.txt"

    remove_first_line(a, b)
