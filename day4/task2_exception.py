def a(list,index):
    try:
        return list[index]
    except IndexError:
        return None
b=[10,20,30,40]
print(a(b,3))
print(a(b,4))