def build_invoice(cust_name,*args,**kwargs):
    total=sum(args)

    print("Customer Name:",cust_name)
    print("Price:",total)

    print("Extra details:")
    for key, value in kwargs.items():
         print(key,":",value)

build_invoice("Ilsa Vahora",10000,20000,40000,discount=20,tax=10)



    