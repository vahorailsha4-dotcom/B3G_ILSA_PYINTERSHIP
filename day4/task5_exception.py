class InvalidNumberError(Exception):
    pass
while True:
    try:
        num=int(input("Enter Number between 1 to 10:"))
        if num<1 or num>10:
            raise InvalidNumberError("Number must be between 1 to 10")
        print("Enter valid number:",num)
        break
    except ValueError:
        print("Error:Enter Numeric Value")
    except InvalidNumberError as e:
        print(e)