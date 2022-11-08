n = int(input('Podaj n: '))

result = 0
for element in range(n + 1):
    result += element

# other solution
# numbers = list(range(0, n + 1))
# print(sum(numbers))

print(result)
