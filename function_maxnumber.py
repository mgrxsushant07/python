# Write a function in Dart called maxNumber that takes three numbers as arguments and returns the largest number.

#using max()
def maxNumber(a, b, c):
    return max(a, b, c)  

# Example usage
print(maxNumber(3, 7, 5))  # Output: 7
print(maxNumber(10, 2, 10))  # Output: 10
print(maxNumber(-1, -5, -3))  # Output: -1

#without using max()
def maxNumber(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage
print(maxNumber(3, 7, 5))  # Output: 7
print(maxNumber(10, 2, 10))  # Output: 10
print(maxNumber(-1, -5, -3))  # Output: -1
