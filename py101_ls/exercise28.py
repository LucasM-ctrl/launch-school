def triangle(size):
    for num in range(1, size + 1):
        spaces = size - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')
        
triangle(9)