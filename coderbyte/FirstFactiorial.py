"""First Factorial
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it.
 For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases,
 the range will be between 1 and 18 and the input will always be an integer.
Examples
Input: 4
Output: 24
Input: 8
Output: 40320 """

def FirstFactorial(num):
    if num <= 1:
        return 1
    else:
        return num * FirstFactorial(num-1)


# print
print(FirstFactorial(4))
print(FirstFactorial(8))
print(FirstFactorial(1))
print(FirstFactorial(0))
