numbers = [12, 45, 7, 89, 34, 89, 56]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print("Second largest number:", second_largest)
