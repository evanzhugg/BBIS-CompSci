list1 = [8, 9, 10]
list1[1] = 17

list1.extend([4, 5, 6])
list1.pop(0)
list1.sort()



# Double the list
list2 = list1 * 2
print(list2)


# Double the entries in the list
list3 = []
for i in list1:
    list3.append(i*2)
print(list3)
list3.insert(3,25)
print(list3)