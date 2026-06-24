s=[]

s.append(("Riya",88))
s.append(("Aman",95))
s.append(("Sara",72))
s.append(("Ali",85))
s.append(("Zara",90))

print("Before Removing:",s)
for s1 in s:
     print("=",s)
    
s.remove(("Sara",72))
s.remove(("Ali",85))

for s in s:
    print("After Removing:",s)
