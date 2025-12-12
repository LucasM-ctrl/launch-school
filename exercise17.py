def penultimate(word):
    split = word.split()
    result = split[-2]
    return result

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")