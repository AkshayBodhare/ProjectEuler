"""Solution to the 14th problem on Project Euler."""

# Generate a Collatz sequence.
def collatz(n, count=1):
    """Generate a collatz sequence."""
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count

def main():
    """find the number of terms in the sequence and find the longest."""
    max_term = [0, 0]
    for i in range(1000000):
        c = collatz(i)
        if c > max_term[0]:
            max_term[0] = c
            max_term[1] = i
    print("found {} at length {}".format(max_term[1], max_term[0]))

if __name__ == '__main__':
    main()
