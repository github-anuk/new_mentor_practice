liste = ["apple","banana","orange"]
print(liste)
numl = []

x = int(input("no of items you want in the list: "))

for i in range(x):
    inp = int(input("number for the list: "))
    numl.append(inp)

print(numl)


y = int(input("number needed to be found ? "))
found = 1

for i in range(len(numl)):
    if y == numl[i]:
        found = 0
        break

if found == 0:
    print("yes the number is found at index", i)
else:
    print("number not found")