# Python Docstrings
# Last Updated :
# 19 Sep, 2025
# Docstrings (Documentation Strings) are special strings used to document Python code. They provide a description of what a module, class, function or method does.

# Declared using triple quotes (' ' ' or " " ").
# Written just below the definition of a function, class, or module.
# Unlike comments (#), docstrings can be accessed at runtime using __doc__ or help().

def greet(name):
    """This function greets the user by their name."""
    return f"Hello, {name}!"

def rectangle(l,b):
    '''Please enter the lenght or breadth of the rectangel.'''  #''' something program in this.

    print(l*b)
    
rectangle(5,9)

print(rectangle.__doc__)#print(doc-string)__doc__string





# def function for Square 

def square(s):
    '''the square of number is upword'''
    
    print(s*s)

square(90)
print(square.__doc__)
