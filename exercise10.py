def multisum(num):
    total = set(range(3, num + 1, 3)) | set(range(5, num + 1, 5))
    return sum(total)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)