num = int(input('Please enter an integer greater than 0: '))
s_or_p = input('Enter "s" to compute the sum, or "p" to compute the product. ')

if s_or_p == 's':
    print(f'The sum of the integers 1 and {num} is {sum(range(1, (num + 1)))}.')

total = 1

if s_or_p == 'p':
    for i in range(1, (num + 1)):
        total *= i
    print(f'The product of the integers between 1 and {num} is {total}.')