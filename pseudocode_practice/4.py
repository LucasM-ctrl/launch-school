# a function that determines the index of the 3rd occurrence of a given character in a string. 
# For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). 
# If the given character does not occur at least 3 times, return None.

START 

SET count = 0 

LOOK TROUGH string to determine how many times we see the target:
    add times to count variable
    IF COUNT >= 3 
        RETURN WHERE THE 3rd 'target' is indexed in string 
    IF COUNT < 3:
        RETURN NONE 
