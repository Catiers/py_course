# Creating empty list & add 3 members in another list.
beatles = []
names_in_groups = ["John Lennon", "Paul McCartney", "George Harrison"]

# Add all names in list.
beatles = [name for name in names_in_groups]

# Add 2 members in list.
for i in range(2):
    members_in_groups = input("Добавьте ещё двух участников группы: ")
    beatles.append(members_in_groups)

print(beatles)  # Print result members in list beatles.

# Delete two last members.
beatles.pop()
beatles.pop()

# Add one member in the top of the list.
beatles.insert(0, "Ringo Starr")

# Print lenght list(beatles) & members in list.
print(len(beatles))
print(beatles)