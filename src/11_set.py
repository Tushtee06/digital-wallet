a={1,2,3,4,1}
#a={} #this syntax will create an empty dictionary not an empty set
print(type(a))
print(a)
b=set() #an empty set created using this syntax
print(type(b))
#adding values to empty set
b.add(2)
b.add(3)
b.add(4)
b.add((3,4,5))#add tuple in the list
b.add(2)#adding a value repeatedly does not changes a set
#b.add({4:5}) cannot add list or dictionary to sets
print(b)
print(len(b)) #count the elements present in set
b.remove(3)#removes 3 from set b
print(b.pop())
print(b)
print(a.union(b))
print(a.intersection(b))