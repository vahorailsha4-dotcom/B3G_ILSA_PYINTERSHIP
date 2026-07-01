def make_validator(min_value):
    def validate(num):
        return num>=min_value
    return validate
validator10=make_validator(10)
validator50=make_validator(50)
print(validator10(5))
print(validator10(15))
print(validator10(20))
print(validator50(20))
print(validator50(50))
print(validator50(75))