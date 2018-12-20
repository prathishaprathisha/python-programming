Zname = input("Enter file name: ")
num_lines = 0
with open(Zname, 'r') as Z:
    for line in Z:
        num_lines += 1
print("Number of lines:")
print(num_lines)
