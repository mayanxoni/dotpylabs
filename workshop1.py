print("-----LIST = []-----") #Same as arrays
print("\n")

list = [1, 2, 3]
print("List: ", list)


list2 = [4, 5, 6]
print("List2: ", str(list2))


list.extend(list2)
print("Extended list: ", list)


list.insert(7, 7)
# insert works at index value
print("List after insert: ", list)


list.remove(7)
print("List after remove: ", list)


list.pop(5)
print("List after pop: ", list)


print("Index of 3 in the list: ", list.index(3))


list.insert(8, 1)
list.count(1)
print("Count of 1 in the list: ", list.count(1))


print("Values from 1 to 4 in the list: ", list[1:4])


print("\n")
print("-----TUPLES = ()-----") #Data remains unchanged, fastest for accessing data
print("\n")

tuple = (1, 2, 3, "Four")
print(tuple)


print("\n")
print("-----SETS = {}-----") #No duplicates
print("\n")


set = {1, 2, 3, 4, 4}
print("Values in the set: ", set)


print("\n")
print("-----DICTIONARY-----") #Unordered, changeable, indexed, and no duplicates
print("\n")

# dictionary = {
#     key: value
# }


dict = {"name": "Mayank", "marks": "PASS"}
print("Values in the dictionary: ", dict["name"])



list3 = [{}, {}, {}]
list3.append(dict)
print("Value at the -1 index with the name 'name': ", list3[-1]["name"])

print("\n")
print("-----for loop-----")
print("\n")


print("Table of 2:")

for i in range(2, 22, 2):
    print(i)


print("\n")
print("-----while loop-----")
print("\n")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

limit = 9
while limit >= 0:
    print(list[limit])
    limit -= 1 


print("\n")
print("-----function()-----")
print("\n")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(new_list):
    print(new_list)
    return len(new_list)


def func2(new_list = 'This is default'):
    print(new_list)
    return len(new_list)


var = func(list)
func2(list)
print(var)


print("\n")
print("-----lambda function()-----")
print("\n")


var = lambda a, b : a * b
print("Multiplication of 4 and 5:", var(4, 5))


square = lambda num, pow : num ** pow
print("2 raise to 3:", square(2, 3))