def square(n):
    return n * n

num = int(input("enter number you want here: "))

print( "square of ", num, "is", square(num))

def error_message():
    print("error please try again")


def add(a , b):
    return a + b

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("sum: ", add(num1, num2))

def factoral (n):
    if n==0:
        return 1
    else:
        return n * factoral(n-1)
num = int(input("enter a number: "))
print("factorial of", num, "is", factoral(num))

#Using functions with parameters and return values makes code more flexible, reusable, and organized. Parameters allow you to pass different data into a function, so the same function can work in many situations without rewriting code. Return values let the function send results back, making it easy to use the output in other parts of a program. For example, in a grade calculator program, a function could take a student’s test scores as parameters and return the final average, which can then be displayed or used to determine a letter grade.

def calulate_average(numbers):
    return sum(numbers) / len(numbers)

nums = [float(x) for x in  input("enter number separated by space: ").split()] 
print("the average is", calulate_average(nums))