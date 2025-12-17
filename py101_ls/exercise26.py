def print_in_box(s):
    size = len(s)
    not_empty= '+' + '-' * 2 + ('-' * size) + '+'
    empty_line = '|' + ' ' * 2 + (' ' * size) + '|'
    middle = '|' + ' ' + s + ' ' + '|'
    box = "\n".join([not_empty, empty_line, middle, empty_line, not_empty])
    print(box)
    
    
print_in_box('To boldly go where no one has gone before.')
print_in_box('')