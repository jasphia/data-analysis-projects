# Part 1 A -- Make a Line

def make_line(num):
    line=""
    for i in range(num):
        line+="#"
    return line

print(make_line(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

def make_square(size):
    square = ""
    for i in range(size-1):
        square += make_line(size) + "\n"
    square+=make_line(size)
    return square

print(make_square(5))




# Part 1 C -- Make a Rectangle

def make_rectangle(width, height):
    rect = ""
    for i in range(height):
       rect += make_line(width) +"\n"

    return rect

print (make_rectangle(5,3))


# Part 2 A -- Make a Stairs

def make_downward_stairs(height):
    stairs = ""
    for i in range(height):
        #i starts at 1 and then accumulates with the for loop
        stairs += make_line(i+1) +"\n"
    return stairs

print(make_downward_stairs(5))



# Part 2 B -- Make Space-Line 

def make_space_line(numSpaces, numChars):
    char = ""
    space = ""
    for i in range(numChars):
        char += "#"
    for i in range(numSpaces):
        space += " "
    return space+char+space

print(make_space_line(3,5))


# Part 2 C -- Make Isosceles Triangle

def make_iso_triangle(height):
    tri = ""
    for i in range(height):
        tri += make_space_line(height - i - 1, 2*i +1) +"\n"
    return tri

print(make_iso_triangle(5))




# Part 3 -- Make a Diamond

def make_diamond(height):
    dimond = ""
    triangle = make_iso_triangle(height)
    dimond += triangle[:1]
    for i in range(len(triangle)-1,-1,-1):
        dimond += triangle[i]
    return dimond

print(make_diamond(5))




