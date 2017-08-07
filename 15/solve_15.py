"""Solution to the 15th problem using combinatorics."""

def factorial(number):
    """Find the factorial of a number."""
    if number == 1:
        return 1
    else:
        return factorial(number-1)*number

def main():
    """The number of paths in a nxn grid is 2n!/n!^2."""
    print(factorial(40)/factorial(20)**2)

if __name__ == '__main__':
    main()
