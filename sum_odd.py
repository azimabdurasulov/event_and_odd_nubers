#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 1789
#Create a variable "sum_even" and assign it 0.
sum_even = 0

x1 = var_int % 10
sum_even += x1 % 2 * x1
var_int //= 10

x2 = var_int % 10
sum_even += x2 % 2 * x2
var_int //= 10

x3 = var_int % 10
sum_even += x3 % 2 * x3
var_int //= 10

x4 = var_int % 10
sum_even += x4 % 2 * x4
#Find the sum of the odd digits in the variable "var_int".
print(sum_even)