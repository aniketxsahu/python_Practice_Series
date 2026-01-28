# WAP to demonstrate various list operations in Python

list1=[1, 2, 3, 4, 5]
list2=['a', 'b', 'c', 'd', 'e']

print(list1 + list2) # concatenation of list1 and list2
print(list1 * 3) # prints list1 three times
print(len(list1)) # prints the length of list1

print(list1[0]) # prints the first element of list1
print(list1[-1]) # prints the last element of list1
print(list1[1:4]) # prints elements from index 1 to 3 of list1
print(list1[1:5:2]) # prints every second element of list1
print(list1[::-1]) # reverses list1
print(list1[::2]) # prints every second element of list1

list1.append(6) # appends 6 to the end of list1
print(list1)
list1.insert(0, 0) # inserts 0 at index 0 of list1
print(list1)
list1.remove(3) # removes the first occurrence of 3 from list1
print(list1)
list1.sort() # sorts list1 in ascending order
print(list1)
list1.reverse() # reverses list1
print(list1)
list3 = list1.copy() # creates a copy of list1
print(list3)
list1.clear() # clears all elements from list1
print(list1)
print(list1.pop(1)) # removes and returns the element at index 1 of list2
print(list1)
print(list1.index(4)) # finds the index of 4 in list1
print(list1.count(2)) # counts occurrences of 2 in list1


list2.extend(['f', 'g', 'h']) # extends list2 by adding elements from another list
print(list1.sort(reverse=True)) # sorts list2 in descending order




