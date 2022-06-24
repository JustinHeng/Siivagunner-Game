#HOW TO USE:
#Run the program and copy and paste the links as input
#The output is printed and can be copy and pasted directly into the excel sheet
print("Paste Youtube links below:")

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

for x in range(0, len(lines)):
    lines[x] = "https://www.youtube.com/embed/" + lines[x][32:43] + "?controls=0"
    print(lines[x])
