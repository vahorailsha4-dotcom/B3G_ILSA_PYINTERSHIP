def safe_division(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Error:Divided by zero is not allowed")
        except TypeError:
             print("Error:Both Values must be Numbers")
print(safe_division(15,10))
print(safe_division(15,0))
print(safe_division(15,"10"))