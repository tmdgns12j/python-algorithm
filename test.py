#팩토리얼
def factorial(i) :
    if i<=1:
        print("1")
        return 1
    print(i,'*',end=" ")
    return i*factorial(i-1)
print(factorial(5))