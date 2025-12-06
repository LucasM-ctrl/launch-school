def area_room(length,width):
    return length * width 

ft = 10.7639
    
    

length = float(input('What is the length of the room in Meters? '))
width = float(input('What is the width of the room in Meters? '))

area = area_room(length, width)
area_ft = area * ft

print(f'In m2 {area:.2f}'
      f' and in ft2 {area_ft:.2f}')
