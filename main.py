3# Put your function here
def factorial(num):
    if num > 1:
        num * factorial(num - 1)
    
    if num == 1:
        return(1)
    

# testing
num = int(input())
print(factorial(num))