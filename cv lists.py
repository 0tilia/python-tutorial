
friends = ["Filip", "Andreea", "Dana", "Alexandra"]

print(friends[3])
print(friends[-4])
print(friends[1:4])

friends[1] = "eu"
print(friends [1])

lucky_numbers = [4, 6, 8, 16, 23, 3]
friends = ["Filip", "Andreea", "Dana", "Dana", "Alexandra"]
friends.append("Cristi")
friends.insert(1, "Oti")
friends.remove("Alexandra")
friends.remove("Cristi")

friends.extend(lucky_numbers)

lucky_numbers.sort()
print(friends.index("Andreea"))
print(friends.count("Dana"))
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)