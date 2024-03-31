from random import randrange as rand
up=input("Enter an upper number: ")
print("Here's a smaller number:",end=" ")
num=rand(int(up)); print(num)
print('The variable "up" = ',up,'.',sep="")
print("The type of", up, "is", type(up))
print('So doing "rand(up)" an error:')
print(rand(up))#up is a string, but it represents a number
