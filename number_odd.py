#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 1237

counter = 0

x1 = var_int % 10
counter += x1 % 2
var_int //= 10

x2 = var_int % 10
counter += x2 % 2
var_int //= 10

x3 = var_int % 10
counter += x3 % 2
var_int //= 10

x4 = var_int % 10
counter += x4 % 2
var_int //= 10
#Print the number of odd digits in the variable "var_int".
print(counter)