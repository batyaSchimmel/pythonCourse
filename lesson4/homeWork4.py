numbers = list(range(1, 17))
index15 = numbers.pop(-1)

index0 = numbers.pop(0)

index12 = numbers.pop(12)

index7 = numbers.pop(7)

print(f'numbers= {numbers}')
print(f'sum_of_removed= {index15 + index0 + index12 + index7}')
