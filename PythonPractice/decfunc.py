def decorator(f):  # renamed to avoid conflict
    a = int(input("Enter Number 1 : "))#values are passed 
    b = int(input("Enter Number 2 : "))

    def wrapper():
        f()
        result = a + b #operations are done 
        return result
    return wrapper

@decorator
def result_is():
    pass

# Call the decorated function and get the return value
final_result = result_is()
print("The final result is:", final_result)



