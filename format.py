# the Use of "repr() and str()"
 
s = 'Hello, World.'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is' + repr(x) + ', and y is ' + repr(y) + '...'
# The repr() of a string adds string quotes and backslashes:

hello = 'Hello, world\n'
hellos = repr(hello)
# s = str(1/7)
# print(str(s))
# print(repr(s))
# print(hello) this will output: Hello, world
# print(hellos) this will output: 'Hello, world\n'