__author__ = 'Kevin'
# Sample python file
# the contents walk through syntax and basics of python

#This is a comment
print("hello world!")

#variables don't need any specification
add = 0
print(add)

#sample arithmetic
print((add + 2 - 1) * 8)

#function in python
def adding (input,input2):
    return input+input2
    print (adding(1,2))

#simple class
#classes don't need getters/ setters, methods organize functionality
#and members organize information
class myclass :
    myString = "simple class content"
    def f(self):
        return 'simple class member content'

x = myclass
print(x.myString)
print(x.f(x))

#sample for loop, essentially does for each implicitly
for num in range(0,3):
    print(num)

#sample while and if and increment
i = 0
while i<10:
    if i == 8:
        print(i)
    i += 1
