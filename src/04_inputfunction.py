'''only allows the user to take a input as a string.
output of the string is always also a string'''

a=input("Enter a number: ")
a=int(a)
print(type(a))
print(a)
#avg of two numbers
b=input("Enter first number : ")
c=input("Enter second number : ")
b = int(b)
c= int(c)
avg = (b+c)/2
print("Average of two number is :",avg)