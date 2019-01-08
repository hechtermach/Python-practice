#dict:{keys:values}
name={1:"a",2:"b",3:"c"}
print (name[1])
print (name.values())
print (name.keys())
print (name.get(4))
name[4]="d"
print (name)

#set:dict without values
set_a=set(['a','b'])
print (set_a)
set_b=set(['b','c'])
set_a.add('c')
print (set_a)
print (set_a and set_b)
