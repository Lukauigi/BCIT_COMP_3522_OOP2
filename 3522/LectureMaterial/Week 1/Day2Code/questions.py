# how to have curly braces as variables and as literal {}.
# Add extra curly braces{{}}
my_string = 'hello {0} {{0}}, it is the year {1}'.format('class', 2020.123)
print(my_string)

# how to indicate decimal places: add .2 before f. Or {1:.2f}
name = 'COMP 3522'
room = 655.05555
print('Course %s is in %.2f\n' % (name, room))  # decimal places with .2f

# mixing conversion specifier (%) with string format ({})
print('Course %s {0} is in %.2f\n' % (name, room))

# explain __name__
# __name__ is a variable loaded automatically into every module which is the module's name. If the module is ran,
# __name__ becomes __main__ to indicate that this module is running the program.
