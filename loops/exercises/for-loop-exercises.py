# Exercise #1: Construct for loops that accomplish the following tasks:
    # a. Print the numbers 0 - 20, one number per line.
    # b. Print only the ODD values from 3 - 29, one number per line.
    # c. Print the EVEN numbers 12 to -14 in descending order, one number per line.
    # d. Challenge - Print the numbers 50 - 20 in descending order, but only if the numbers are multiples of 3. (Your code should work even if you replace 50 or 20 with other numbers).

for i in range (21):
    print(i)

#i = 0
for i in range(0, 30):
    if i != (i % 2) != 0:
        print(i)

for i in range(12, -15, -1):
    print(i)

