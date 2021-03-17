"""
Problem Euler
Sum square difference
Solved By Ahmet Acarer
Iterative Solution 
2021

"""
#1^2 + 2^2...+100^2 = 338350
def sum_of_squares(n):
  total = 0
  for x in range(1, n+1):
    total += x**2
  return total

# (1 + 2 ... + 100)^2 = 25502500
def square_sum(n):
  total = 0
  for x in range(1, n+1):
    total += x
  return total**2

#creating object

sum_of_squares = sum_of_squares(100)
square_sum = square_sum(100)
print("Sum of squares: ",sum_of_squares)
print("Square sum: ",square_sum)
print("difference between both: ", square_sum - sum_of_squares)
