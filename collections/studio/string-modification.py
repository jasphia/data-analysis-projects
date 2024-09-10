my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
cut = my_string[0:3]
# print(cut)
# my_string[0:3]
# my_string += cut
# print(my_string[len(my_string)-1])
my_new_string = my_string.replace("Lau", "")
#look up how to remove before you hard code it

print(my_new_string+cut)

# Use a template literal to print the original and modified string in a descriptive phrase.
print("old: {1} new: {0}", my_string.format(my_string, my_new_string))


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
user = input("enter:")
print("enter #",user)

cut = my_string[0:user]
print(cut)
# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
