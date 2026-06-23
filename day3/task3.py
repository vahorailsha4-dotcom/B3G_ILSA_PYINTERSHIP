numbers = [12, 45, 12, 78, 45, 90, 23, 78, 11, 23, 56, 90, 34, 11, 67]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)