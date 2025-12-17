bill = float(input('What is the bill? '))
tip = float(input('What is the tip percentage? '))
 
tip_result = bill * (tip / 100)
total = tip_result + bill

print(f'The tip is ${tip_result:.2f}.\n' 
      f'The total is ${total:.2f}.')