mode="Global"
def outer():
    mode="Outer"
    def inner():
        mode="Inner"
        print("Inside inner():",mode)
    inner()
    print("Inside outer():",mode)
outer()
print("Global:",mode)