#A four-digit integer is given. Find the sum of even digits in it.

#A four-digit integer is given. Find the sum of even digits in it.
var_int = 2346
#Create a variable "sum_even" and assign it 0.
sum_even = 0

x1 = var_int % 10 + 1
sum_even += x1 % 2 * (x1 - 1)
var_int //= 10

x2 = var_int % 10 + 1
sum_even += x2 % 2 * (x2 - 1)
var_int //= 10

x3 = var_int % 10 + 1
sum_even += x3 % 2 * (x3 - 1)
var_int //= 10

x4 = var_int % 10 + 1
sum_even += x4 % 2 * (x4 - 1)
#Find the sum of the even digits in the variable "var_int".
print(sum_even)