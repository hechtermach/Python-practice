list_a=[1,2,3,"abc",["d","e","f"]]
for i in list_a:
    print (i)
    if i==2:
        break
        continue
    print("~~~~~~~~~~~")


for i in range (0,10):
    for j in range (0,10):
        print (i**j)
        if j==5:
            break
s=0
for i in range (1,101):
    s=s+i
    if i==101:
        print (s)
