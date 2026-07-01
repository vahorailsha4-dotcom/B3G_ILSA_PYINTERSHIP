class InvalidAgeError(Exception):
    pass
def register_user(age):
    if age<0 or age>120:
        raise InvalidAgeError("Invalid Age!!Enter Between 0 to 120")
    print("Successfully")
try:
    register_user(10)
    register_user(121)
except InvalidAgeError as e:
    print(e)