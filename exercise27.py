def stringy(i):
    result = ''
    for idx in range(i):
        if idx % 2 == 1:
            result += '0'
        else:
            result += '1'
    return result
  
        
    
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True