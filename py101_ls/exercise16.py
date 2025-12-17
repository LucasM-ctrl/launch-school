num1 = float(input('==> Enter the first number: '))
num2 = float(input('==> Enter the second number: '))

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')

#can use a match case

#def calculate(first, second, operator):
#    match operator:
#        case '+':  return first + second
#        case '-':  return first - second
#        case '*':  return first * second
#        case '/':  return first / second
#        case '//': return first // second
#        case '%':  return first % second
#        case '**': return first ** second
    
#for operator in ['+', '-', '*', '/', '//', '%', '**']:
#    operation = f"{num1} {operator} {num2}"
#    result = calculate(num1, num2, operator)
#   print(f"==> {operation} = {result}")