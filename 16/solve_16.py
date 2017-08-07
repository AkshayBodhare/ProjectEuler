"""Solution to the 16th problem on Project Euler."""

def sum_of_digits(number):
    """find the sum of digits in a number."""
    _ = 0
    while number:
        _, number = _ + number%10, number // 10
    return _

def main():
    """Soultion."""
    print(sum_of_digits(2**1000))

if __name__ == '__main__':
    main()
