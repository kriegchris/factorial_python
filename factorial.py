import sys

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def main(args):
    print("Welcome to the Factorial Calulator!")
    num = -1
    cont = "y"
    while (cont == "y") :
        while (num < 1 or num > 10) :
            num = input("enter an Integer that's greater than 0, but less than 10: ")
            num = int(num)
        result = factorial(num)
        print("the factorial of " + str(num) + " is " + str(result))
        cont = input("Continue? (y/n): ")
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
