def clean_up(phrase):
    clean = ''
    for char in phrase:
        if char.isalpha() == True:
            clean += char
        else:
            if clean == '' or clean[-1] != ' ':
                clean += ' '
    return (clean)
        
            
            
print(clean_up("---what's my +*& line?") == " what s my line ")
# True