coordinates = (10, 20)
print(coordinates)
# coordinates[0]=50
# print(coordinates)

list1=list(coordinates)
list1[0]=50
coordinates=tuple(list1)
print(coordinates)

# corlist = list(coordinates)
# corlist[0] = 50
# coordinates = tuple(corlist)
# print(coordinates)