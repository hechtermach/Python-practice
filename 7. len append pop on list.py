list_a=[1,2,3,["a","b","c"],"def"]
print (len(list_a))
print (list_a[3])

list_a.append(["g","h","i"])
list_a.insert(3,[4,5,6])
print (list_a)

list_a.pop()
print (list_a)

list_a.pop(3)
print (list_a)
