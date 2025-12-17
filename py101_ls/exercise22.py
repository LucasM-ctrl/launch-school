def center_of(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 0:
        return s[middle -1 : middle + 1]
    else:
        return s[middle]
    
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True