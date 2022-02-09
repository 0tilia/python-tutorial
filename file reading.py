
# in ghilimele punem numele fisierului
# a = add info
# r+ = read and write
# r = read
# w = write
names_file = open("names.txt", "r+")

print(names_file.readable())

print(names_file.read())

# the first two lines of the file
print(names_file.readline())
print(names_file.readline()[1])

# le aranjeaza in lista, daca pui [1] citeste primul rand

print(names_file.readlines())

names_file = open("names.txt", "a")
for friend in names_file.readlines():
    print(friend)

# close it when it's done (good practice)

names_file.close()
