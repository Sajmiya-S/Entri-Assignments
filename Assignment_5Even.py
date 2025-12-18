# Write a generator function even_numbers(n) that yields the first n even numbers starting from 2

def even_numbers(n):
    for i in range(n):
        yield 2 * (i + 1)

n = int(input('Enter a number: '))
even = even_numbers(n)
print(f'The First {n} even numbers :')

for i in range(n):
    print(next(even))


