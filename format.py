# the Use of "repr() and str()"
 
s = 'Hello, World.'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is' + repr(x) + ', and y is ' + repr(y) + '...'

# print(str(s))
# print(repr(s))

# The repr() of a string adds string quotes and backslashes:
hello = 'Hello, world\n'
# print(hello) this will output: Hello, world

hellos = repr(hello)
# print(hellos) this will output: 'Hello, world\n'