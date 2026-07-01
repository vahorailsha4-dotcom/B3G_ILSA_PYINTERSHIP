def require_positive(func):
    def wrapper(*args):
        for arg in args:
            if arg<=0:
                print("Error:Both Number are Positive")
            return
        return func(*args)
    return wrapper
@require_positive
def divide(a,b):
        print("Division Result=",a/b)
divide(4,5)
divide(-2,5)