list = []
new = 'false'

new_elements = [1, 2, 3, 4,]
for element in new_elements:
    list.append(element)


string = "".join(str(element) for element in list)

print(list)
print(string)
