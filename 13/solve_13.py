"""Solution to the 13th problem on Project Euler."""

def main():
    """Input the file and sum all the numbers and find the first 10 digits."""
    with open('13.txt') as file:
        result = str(sum([int(x) for x in file.readlines()]))[:10]
        print(result)

if __name__ == '__main__':
    main()
