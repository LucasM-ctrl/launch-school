def xor(val1, val2):
    if (val1 and not val2):
        return True
    elif (val2 and not val1):
        return True
    elif (not val1 and not val2):
        return False
    elif (val1 and val2):
        return False

#could use return bool(val1) != bool(val2)
    
   
    
    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)