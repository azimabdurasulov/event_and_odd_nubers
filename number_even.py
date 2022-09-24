#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 2168

counter = 0

x1 = var_int % 10 + 1
counter += x1 % 2
var_int //= 10

x2 = var_int % 10 + 1
counter += x2 % 2
var_int //= 10

x3 = var_int % 10 + 1
counter += x3 % 2
var_int //= 10

x4 = var_int % 10 + 1
counter += x4 % 2
#Print the number of even digits in the variable "var_int".
var_int = counter
print(var_int)